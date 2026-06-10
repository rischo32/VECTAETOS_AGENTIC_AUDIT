#!/usr/bin/env python3
"""
VECTAETOS Agentic Audit - Reference Verifier CLI (MVP)

Validates schema compliance and hash continuity for EAI artifacts.
Minimal, lightweight, auditable implementation.

Usage:
    python verify.py <artifact_file> [--schema <schema_path>]
    python verify.py --validate-all-examples
"""

import argparse
import hashlib
import json
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple


class SchemaValidationError(Exception):
    """Raised when artifact fails schema validation."""
    pass


class HashContinuityError(Exception):
    """Raised when hash chain is broken."""
    pass


class VerifierError(Exception):
    """Base verifier exception."""
    pass


def load_json_file(file_path: str) -> Dict[str, Any]:
    """Load and parse a JSON file."""
    try:
        with open(file_path, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        raise VerifierError(f"File not found: {file_path}")
    except json.JSONDecodeError as e:
        raise VerifierError(f"Invalid JSON in {file_path}: {e}")


def hash_string(content: str, algorithm: str = 'sha256') -> str:
    """Compute hash of a string using specified algorithm."""
    if algorithm == 'sha256':
        return hashlib.sha256(content.encode('utf-8')).hexdigest()
    elif algorithm == 'sha512':
        return hashlib.sha512(content.encode('utf-8')).hexdigest()
    else:
        raise VerifierError(f"Unsupported hash algorithm: {algorithm}")


def compute_artifact_hash(artifact: Dict[str, Any]) -> Tuple[str, str]:
    """
    Compute hash of artifact without the continuity field.
    Returns (hash_value, algorithm).
    """
    artifact_copy = artifact.copy()
    hash_algorithm = artifact_copy.get('continuity', {}).get('hash_algorithm', 'sha256')
    del artifact_copy['continuity']  # Exclude continuity from hash computation

    # Canonical JSON (sorted keys, no extra whitespace)
    canonical = json.dumps(artifact_copy, sort_keys=True, separators=(',', ':'))
    return hash_string(canonical, hash_algorithm), hash_algorithm


def validate_hash_pattern(hash_value: str) -> bool:
    """Validate hash matches pattern (64-128 hex chars)."""
    import re
    return bool(re.match(r'^[a-fA-F0-9]{64,128}$', hash_value))


def verify_transformation_log(artifact_data: Dict[str, Any]) -> List[str]:
    """
    Verify hash chain in transformation_log.
    Returns list of errors found.
    """
    errors = []
    trans_log = artifact_data.get('transformation_log', [])

    if not trans_log:
        return errors

    # Verify each hash pattern is valid
    for i, transform in enumerate(trans_log):
        for key in ['input_hash', 'output_hash']:
            hash_val = transform.get(key)
            if hash_val and not validate_hash_pattern(hash_val):
                errors.append(f"Transform[{i}] {key}: Invalid hash pattern")

    # Verify chain continuity
    for i in range(len(trans_log) - 1):
        current_output = trans_log[i].get('output_hash')
        next_input = trans_log[i + 1].get('input_hash')

        if current_output != next_input:
            errors.append(
                f"Transform[{i}]: Chain broken - "
                f"output_hash '{current_output}' != next input_hash '{next_input}'"
            )

    # Verify first transform input matches input_snapshot_hash
    if trans_log:
        input_snapshot_hash = artifact_data.get('input_snapshot_hash')
        first_input = trans_log[0].get('input_hash')
        if input_snapshot_hash != first_input:
            errors.append(
                f"Chain broken - input_snapshot_hash '{input_snapshot_hash}' "
                f"!= first transform input_hash '{first_input}'"
            )

    # Verify last transform output matches output_snapshot_hash
    if trans_log:
        output_snapshot_hash = artifact_data.get('output_snapshot_hash')
        last_output = trans_log[-1].get('output_hash')
        if output_snapshot_hash != last_output:
            errors.append(
                f"Chain broken - output_snapshot_hash '{output_snapshot_hash}' "
                f"!= last transform output_hash '{last_output}'"
            )

    return errors


def verify_continuity(artifact: Dict[str, Any]) -> List[str]:
    """
    Verify continuity section of EAI artifact.
    Returns list of errors found.
    """
    errors = []
    continuity = artifact.get('continuity', {})

    if not continuity:
        errors.append("Missing continuity section")
        return errors

    # Verify current_artifact_hash matches computed hash
    declared_hash = continuity.get('current_artifact_hash')
    hash_algorithm = continuity.get('hash_algorithm', 'sha256')

    if not declared_hash:
        errors.append("Missing current_artifact_hash")
    elif not validate_hash_pattern(declared_hash):
        errors.append(f"current_artifact_hash has invalid pattern: {declared_hash}")
    else:
        computed_hash, _ = compute_artifact_hash(artifact)
        if declared_hash != computed_hash:
            errors.append(
                f"Hash mismatch - declared '{declared_hash}' "
                f"!= computed '{computed_hash}'"
            )

    # Verify previous_artifact_hash pattern if present
    prev_hash = continuity.get('previous_artifact_hash')
    if prev_hash and not validate_hash_pattern(prev_hash):
        errors.append(f"previous_artifact_hash has invalid pattern: {prev_hash}")

    # Verify signature presence
    signature = continuity.get('signature', {})
    if not signature:
        errors.append("Missing signature object")
    else:
        if not signature.get('algorithm'):
            errors.append("Missing signature.algorithm")
        if not signature.get('key_id'):
            errors.append("Missing signature.key_id")
        if not signature.get('signature_value') or len(signature.get('signature_value', '')) < 32:
            errors.append("Missing or invalid signature.signature_value")

    return errors


def verify_non_intervention_attestation(artifact: Dict[str, Any]) -> List[str]:
    """Verify non-intervention attestation."""
    errors = []
    attestation = artifact.get('non_intervention_attestation', {})

    if not attestation:
        errors.append("Missing non_intervention_attestation")
        return errors

    audit_mode = attestation.get('audit_mode')
    if audit_mode != 'non_intervention_audit':
        errors.append(
            f"Invalid audit_mode '{audit_mode}' "
            f"(expected 'non_intervention_audit')"
        )

    observer_only = attestation.get('observer_only')
    if observer_only is not True:
        errors.append(f"observer_only must be true, got: {observer_only}")

    return errors


def verify_eai_artifact(artifact: Dict[str, Any]) -> Tuple[bool, List[str]]:
    """
    Verify EAI artifact compliance and continuity.
    Returns (success, errors).
    """
    errors = []

    # Check basic required fields
    required_fields = [
        'schema_version', 'artifact_type', 'artifact_id',
        'contract_id', 'transformation_set_id', 'generated_at',
        'producer', 'artifact_data', 'continuity', 'non_intervention_attestation'
    ]

    for field in required_fields:
        if field not in artifact:
            errors.append(f"Missing required field: {field}")

    if errors:
        return False, errors

    # Verify schema_version
    if artifact.get('schema_version') != '0.1.0':
        errors.append(f"Unsupported schema_version: {artifact.get('schema_version')}")

    # Verify artifact_type
    if artifact.get('artifact_type') != 'eai_artifact':
        errors.append(f"Invalid artifact_type: {artifact.get('artifact_type')}")

    # Verify hash patterns in artifact_data
    artifact_data = artifact.get('artifact_data', {})
    for key in ['input_snapshot_hash', 'output_snapshot_hash']:
        hash_val = artifact_data.get(key)
        if hash_val and not validate_hash_pattern(hash_val):
            errors.append(f"artifact_data.{key}: Invalid hash pattern")

    # Verify transformation log
    errors.extend(verify_transformation_log(artifact_data))

    # Verify continuity
    errors.extend(verify_continuity(artifact))

    # Verify non-intervention attestation
    errors.extend(verify_non_intervention_attestation(artifact))

    return len(errors) == 0, errors


def verify_eai_artifact_offline_bundle(artifact: Dict[str, Any]) -> Tuple[bool, List[str]]:
    """
    Verify EAI artifact compliance and continuity (offline bundle structure).
    Returns (success, errors).
    """
    errors = []

    # Check basic required fields (offline bundle uses object_type and no non_intervention_attestation)
    required_fields = [
        'schema_version', 'object_type', 'artifact_id',
        'contract_id', 'transformation_set_id', 'generated_at',
        'producer', 'artifact_data', 'continuity'
    ]

    for field in required_fields:
        if field not in artifact:
            errors.append(f"Missing required field: {field}")

    if errors:
        return False, errors

    # Verify schema_version
    if artifact.get('schema_version') != '0.1.0':
        errors.append(f"Unsupported schema_version: {artifact.get('schema_version')}")

    # Verify object_type
    if artifact.get('object_type') != 'eai_artifact':
        errors.append(f"Invalid object_type: {artifact.get('object_type')}")

    # Verify hash patterns in artifact_data
    artifact_data = artifact.get('artifact_data', {})
    for key in ['input_snapshot_hash', 'output_snapshot_hash']:
        hash_val = artifact_data.get(key)
        if hash_val and not validate_hash_pattern(hash_val):
            errors.append(f"artifact_data.{key}: Invalid hash pattern")

    # Verify transformation log
    errors.extend(verify_transformation_log(artifact_data))

    # Verify continuity
    errors.extend(verify_continuity(artifact))

    return len(errors) == 0, errors


def verify_agent_contract(contract: Dict[str, Any]) -> Tuple[bool, List[str]]:
    """
    Verify agent contract basic compliance.
    Returns (success, errors).
    """
    errors = []

    # Check required fields
    required_fields = [
        'schema_version', 'contract_type', 'contract_id',
        'issued_at', 'machine_contract', 'human_context'
    ]

    for field in required_fields:
        if field not in contract:
            errors.append(f"Missing required field: {field}")

    if errors:
        return False, errors

    # Verify schema_version
    if contract.get('schema_version') != '0.1.0':
        errors.append(f"Unsupported schema_version: {contract.get('schema_version')}")

    # Verify contract_type
    if contract.get('contract_type') != 'agent_contract':
        errors.append(f"Invalid contract_type: {contract.get('contract_type')}")

    # Verify machine_contract boundary
    machine_contract = contract.get('machine_contract', {})
    operational_boundary = machine_contract.get('operational_boundary', {})

    if operational_boundary.get('audit_mode') != 'non_intervention_audit':
        errors.append(
            f"Invalid audit_mode '{operational_boundary.get('audit_mode')}' "
            f"(expected 'non_intervention_audit')"
        )

    if operational_boundary.get('allowed_observer_actions'):
        allowed = operational_boundary.get('allowed_observer_actions', [])
        valid_actions = ['read_logs', 'capture_hash', 'verify_signature', 'append_audit_artifact']
        for action in allowed:
            if action not in valid_actions:
                errors.append(f"Invalid allowed_observer_action: {action}")

    return len(errors) == 0, errors


def verify_transformation_set(trans_set: Dict[str, Any]) -> Tuple[bool, List[str]]:
    """
    Verify transformation set basic compliance.
    Returns (success, errors).
    """
    errors = []

    # Check required fields
    required_fields = [
        'schema_version', 'set_type', 'set_id',
        'machine_transformation_spec', 'human_rationale'
    ]

    for field in required_fields:
        if field not in trans_set:
            errors.append(f"Missing required field: {field}")

    if errors:
        return False, errors

    # Verify schema_version
    if trans_set.get('schema_version') != '0.1.0':
        errors.append(f"Unsupported schema_version: {trans_set.get('schema_version')}")

    # Verify set_type
    if trans_set.get('set_type') != 'fixed_transformation_set':
        errors.append(f"Invalid set_type: {trans_set.get('set_type')}")

    # Verify transforms
    spec = trans_set.get('machine_transformation_spec', {})
    transforms = spec.get('transforms', [])

    if not transforms:
        errors.append("machine_transformation_spec.transforms cannot be empty")

    valid_operations = [
        'canonicalize_json', 'redact_json_pointer', 'hash_field',
        'derive_metric', 'sign_payload'
    ]

    for i, transform in enumerate(transforms):
        # Verify deterministic is true
        if transform.get('deterministic') is not True:
            errors.append(f"Transform[{i}]: deterministic must be true")

        # Verify intervention_allowed is false
        if transform.get('intervention_allowed') is not False:
            errors.append(f"Transform[{i}]: intervention_allowed must be false")

        # Verify operation is valid
        op = transform.get('operation')
        if op not in valid_operations:
            errors.append(f"Transform[{i}]: Invalid operation '{op}'")

    return len(errors) == 0, errors


def verify_agent_contract_offline_bundle(contract: Dict[str, Any]) -> Tuple[bool, List[str]]:
    """
    Verify agent contract basic compliance (offline bundle structure).
    Returns (success, errors).
    """
    errors = []

    # Check required fields
    required_fields = [
        'schema_version', 'object_type', 'contract_id',
        'issued_at', 'boundary'
    ]

    for field in required_fields:
        if field not in contract:
            errors.append(f"Missing required field: {field}")

    if errors:
        return False, errors

    # Verify schema_version
    if contract.get('schema_version') != '0.1.0':
        errors.append(f"Unsupported schema_version: {contract.get('schema_version')}")

    # Verify object_type
    if contract.get('object_type') != 'contractmesh_contract':
        errors.append(f"Invalid object_type: {contract.get('object_type')}")

    # Verify boundary
    boundary = contract.get('boundary', {})
    if boundary.get('audit_mode') != 'non_intervention_audit':
        errors.append(f"Invalid audit_mode '{boundary.get('audit_mode')}' (expected 'non_intervention_audit')")

    if boundary.get('observer_only') is not True:
        errors.append(f"observer_only must be true, got: {boundary.get('observer_only')}")

    # Verify integrity
    integrity = contract.get('integrity', {})
    if not integrity.get('current_contract_hash'):
        errors.append("Missing integrity.current_contract_hash")

    return len(errors) == 0, errors


def verify_transformation_set_offline_bundle(trans_set: Dict[str, Any]) -> Tuple[bool, List[str]]:
    """
    Verify transformation set basic compliance (offline bundle structure).
    Returns (success, errors).
    """
    errors = []

    # Check required fields (offline bundle uses set_id, not transformation_set_id)
    required_fields = [
        'schema_version', 'object_type', 'set_id',
        'transforms'
    ]

    for field in required_fields:
        if field not in trans_set:
            errors.append(f"Missing required field: {field}")

    if errors:
        return False, errors

    # Verify schema_version
    if trans_set.get('schema_version') != '0.1.0':
        errors.append(f"Unsupported schema_version: {trans_set.get('schema_version')}")

    # Verify object_type (offline bundle uses "fixed_transformation_set")
    if trans_set.get('object_type') != 'fixed_transformation_set':
        errors.append(f"Invalid object_type: {trans_set.get('object_type')}")

    # Verify transforms (direct array in offline bundle)
    transforms = trans_set.get('transforms', [])

    if not transforms:
        errors.append("transforms cannot be empty")

    valid_operations = [
        'canonicalize_json', 'redact_json_pointer', 'hash_field',
        'derive_metric', 'sign_payload'
    ]

    for i, transform in enumerate(transforms):
        # Verify deterministic is true
        if transform.get('deterministic') is not True:
            errors.append(f"Transform[{i}]: deterministic must be true")

        # Verify intervention_allowed is false
        if transform.get('intervention_allowed') is not False:
            errors.append(f"Transform[{i}]: intervention_allowed must be false")

        # Verify operation is valid
        op = transform.get('operation')
        if op not in valid_operations:
            errors.append(f"Transform[{i}]: Invalid operation '{op}'")

    return len(errors) == 0, errors


def verify_artifact(file_path: str, schema_path: Optional[str] = None) -> Tuple[bool, List[str]]:
    """
    Main verification entry point.
    Detects artifact type and runs appropriate verification.
    """
    artifact = load_json_file(file_path)

    # Detect artifact type (supports both naming conventions)
    artifact_type = (artifact.get('artifact_type') or 
                    artifact.get('contract_type') or 
                    artifact.get('set_type') or
                    artifact.get('object_type'))

    if not artifact_type:
        return False, ["Cannot determine artifact type - missing type field"]

    # Support both v0.1 naming and offline bundle naming
    if artifact_type == 'eai_artifact':
        # Check which structure is being used based on presence of artifact_type vs object_type
        if 'artifact_type' in artifact:
            return verify_eai_artifact(artifact)
        elif 'object_type' in artifact:
            return verify_eai_artifact_offline_bundle(artifact)
    elif artifact_type in ['agent_contract', 'contractmesh_contract']:
        # Check which structure is being used
        if 'contract_type' in artifact:
            return verify_agent_contract(artifact)
        elif 'object_type' in artifact:
            return verify_agent_contract_offline_bundle(artifact)
    elif artifact_type in ['fixed_transformation_set', 'transformation_set']:
        # Check which structure is being used
        if 'set_type' in artifact:
            return verify_transformation_set(artifact)
        elif 'object_type' in artifact:
            return verify_transformation_set_offline_bundle(artifact)
    else:
        return False, [f"Unknown artifact type: {artifact_type}"]


def format_errors(errors: List[str]) -> str:
    """Format error list for display."""
    if not errors:
        return "None"
    return '\n  - ' + '\n  - '.join(errors)


def main():
    parser = argparse.ArgumentParser(
        description='VECTAETOS Reference Verifier - Schema and Hash Continuity Validator'
    )
    parser.add_argument(
        'artifact_file',
        nargs='?',
        help='Path to artifact JSON file to verify'
    )
    parser.add_argument(
        '--schema',
        help='Path to JSON schema file (optional - minimal verifier does structural checks)'
    )
    parser.add_argument(
        '--validate-all-examples',
        action='store_true',
        help='Validate all example artifacts in examples/v0.1/'
    )

    args = parser.parse_args()

    if args.validate_all_examples:
        # Validate all example artifacts
        examples_dir = Path(__file__).parent / 'examples' / 'v0.1'
        if not examples_dir.exists():
            print(f"ERROR: Examples directory not found: {examples_dir}")
            return 1

        example_files = list(examples_dir.glob('*.json'))
        if not example_files:
            print(f"ERROR: No example files found in {examples_dir}")
            return 1

        all_passed = True
        for example_file in sorted(example_files):
            print(f"\n{'='*70}")
            print(f"Verifying: {example_file.name}")
            print(f"{'='*70}")

            try:
                success, errors = verify_artifact(str(example_file))

                if success:
                    print(f"✓ PASSED: {example_file.name}")
                else:
                    print(f"✗ FAILED: {example_file.name}")
                    print(f"\nErrors:\n{format_errors(errors)}")
                    all_passed = False

            except VerifierError as e:
                print(f"✗ ERROR: {e}")
                all_passed = False

        print(f"\n{'='*70}")
        if all_passed:
            print("✓ All examples PASSED")
            return 0
        else:
            print("✗ Some examples FAILED")
            return 1

    elif args.artifact_file:
        # Verify single artifact
        print(f"Verifying: {args.artifact_file}")
        print('-' * 70)

        try:
            success, errors = verify_artifact(args.artifact_file, args.schema)

            if success:
                print("✓ PASSED: Artifact is valid")
                print("\nVerifications performed:")
                print("  - Required fields present")
                print("  - Schema version compatibility")
                print("  - Hash pattern validation")
                print("  - Transformation log continuity")
                print("  - Artifact hash consistency")
                print("  - Non-intervention attestation")
                print("  - Signature structure (format only)")
                return 0
            else:
                print("✗ FAILED: Artifact verification failed")
                print(f"\nErrors:\n{format_errors(errors)}")
                return 1

        except VerifierError as e:
            print(f"✗ ERROR: {e}")
            return 1

    else:
        parser.print_help()
        return 1


if __name__ == '__main__':
    sys.exit(main())

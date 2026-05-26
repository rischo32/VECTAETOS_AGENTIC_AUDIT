from __future__ import annotations

from dataclasses import dataclass
from hashlib import sha256
from typing import Dict, List, Optional, Sequence, Tuple

import numpy as np

NODES: Tuple[str, ...] = ("INT", "LEX", "VER", "LIB", "UNI", "REL", "WIS", "CRE")
NODE_COUNT = 8


@dataclass(frozen=True)
class Phi:
    sigma: np.ndarray
    R: np.ndarray


@dataclass(frozen=True)
class StateRecord:
    sigma: np.ndarray
    label: str


@dataclass(frozen=True)
class Trajectory:
    states: Tuple[StateRecord, ...]


@dataclass(frozen=True)
class SimulationResult:
    trajectories: Tuple[Trajectory, ...]
    topology_hash: str


def _validate_sigma(sigma: np.ndarray) -> np.ndarray:
    arr = np.asarray(sigma, dtype=float)
    if arr.shape != (NODE_COUNT,):
        raise ValueError("sigma shape must be (8,)")
    return arr


def _validate_R(R: np.ndarray) -> np.ndarray:
    arr = np.asarray(R, dtype=float)
    if arr.shape != (NODE_COUNT, NODE_COUNT):
        raise ValueError("R shape must be (8, 8)")
    if not np.allclose(arr, -arr.T):
        raise ValueError("R must be antisymmetric")
    return arr


def build_phi(sigma: Sequence[float], R: Sequence[Sequence[float]]) -> Phi:
    return Phi(sigma=_validate_sigma(np.array(sigma, dtype=float)), R=_validate_R(np.array(R, dtype=float)))


def _hash_sigma(sigma: np.ndarray) -> str:
    payload = ",".join(f"{x:.12g}" for x in sigma.tolist())
    return sha256(payload.encode("utf-8")).hexdigest()


def _topology_hash(R: np.ndarray) -> str:
    payload = ",".join(f"{x:.12g}" for x in R.reshape(-1).tolist())
    return sha256(payload.encode("utf-8")).hexdigest()


def _sample_perturbations(rng: np.random.Generator, count: int, scale: float) -> np.ndarray:
    if count <= 0:
        raise ValueError("perturbation_count must be > 0")
    return rng.normal(0.0, scale, size=(count, NODE_COUNT))


def _realizable_transition(sigma: np.ndarray, R: np.ndarray, perturbation: np.ndarray) -> Optional[np.ndarray]:
    candidate = sigma + (R @ perturbation)
    if not np.isfinite(candidate).all():
        return None
    if np.allclose(candidate, sigma):
        return None
    return candidate


def _evolve_one_step(
    phi: Phi,
    perturbation_count: int,
    perturbation_scale: float,
    rng: np.random.Generator,
) -> Tuple[Optional[np.ndarray], bool]:
    perturbations = _sample_perturbations(rng, perturbation_count, perturbation_scale)
    realizable: List[np.ndarray] = []
    for p in perturbations:
        next_sigma = _realizable_transition(phi.sigma, phi.R, p)
        if next_sigma is not None:
            realizable.append(next_sigma)
    if not realizable:
        return None, True
    selected = realizable[0]
    return selected, False


def generate_trajectories(
    phi: Phi,
    trajectory_count: int,
    max_steps: int,
    perturbation_count: int,
    perturbation_scale: float = 1.0,
    seed: Optional[int] = None,
) -> SimulationResult:
    if trajectory_count <= 0:
        raise ValueError("trajectory_count must be > 0")
    if max_steps <= 0:
        raise ValueError("max_steps must be > 0")

    base_rng = np.random.default_rng(seed)
    trajectories: List[Trajectory] = []

    for _ in range(trajectory_count):
        local_seed = int(base_rng.integers(0, 2**63 - 1))
        rng = np.random.default_rng(local_seed)

        current_sigma = phi.sigma.copy()
        records: List[StateRecord] = [StateRecord(sigma=current_sigma.copy(), label="REALIZABLE")]

        for _step in range(max_steps):
            next_sigma, qe = _evolve_one_step(
                Phi(sigma=current_sigma, R=phi.R),
                perturbation_count=perturbation_count,
                perturbation_scale=perturbation_scale,
                rng=rng,
            )
            if qe:
                records.append(StateRecord(sigma=current_sigma.copy(), label="QE"))
                break
            current_sigma = next_sigma
            records.append(StateRecord(sigma=current_sigma.copy(), label="REALIZABLE"))

        trajectories.append(Trajectory(states=tuple(records)))

    return SimulationResult(trajectories=tuple(trajectories), topology_hash=_topology_hash(phi.R))


def serialize_result(result: SimulationResult) -> Dict[str, object]:
    serialized_trajectories: List[Dict[str, object]] = []
    for trajectory in result.trajectories:
        states: List[Dict[str, object]] = []
        for state in trajectory.states:
            states.append(
                {
                    "sigma": state.sigma.tolist(),
                    "sigma_hash": _hash_sigma(state.sigma),
                    "label": state.label,
                }
            )
        serialized_trajectories.append({"states": states})

    return {
        "nodes": list(NODES),
        "trajectories": serialized_trajectories,
        "topology_hash": result.topology_hash,
    }


# TODO: Add external I/O wrapper if required by calling environment.

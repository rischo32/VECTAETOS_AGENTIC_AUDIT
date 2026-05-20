# EAT LEDGER — Google Sheets Setup
# VECTAETOS ContractMesh v1.0

## 1. Zaloz Google Sheet

Nazov sheetu: EAT_Ledger

Stlpce (presne v tomto poradi, riadok 1):
| A         | B           | C      | D                | E            | F      |
|-----------|-------------|--------|------------------|--------------|--------|
| timestamp | contract_id | source | original_message | agent_report | status |

Pravidla:
- NIKDY nevymaz zaznam
- NIKDY neopravuj stary zaznam
- Ak treba opravit — pridaj novy zaznam s poznamkou

---

## 2. Ziskaj Sheet ID

URL tvojho sheetu vyzera takto:
https://docs.google.com/spreadsheets/d/TOTO_JE_TVOJE_ID/edit

Skopiruj ID a vloz do n8n nodu "EAT Ledger — Google Sheets"

---

## 3. Pripoj Google Sheets v n8n

n8n > Credentials > Add > Google Sheets OAuth2
Postupuj podla n8n pruvodcu — potrebujes Google Cloud projekt s Sheets API.

---

## 4. Nastavenia sheetu pre immutabilitu

V Google Sheets:
Nastroje > Chranit harch a rozsahy > Chranit cely sheet
Nastav: len ty mas pravo menit strukturu, automatizacia moze len pridat riadky.

---

## 5. Volitelne — lokalne hashovanie zaznamov

Ak chces pridat EK hash ku kazdemu zaznamu,
pridaj v n8n pred Google Sheets nod tento Code nod:

--- CODE NOD (JavaScript) ---

const crypto = require('crypto');

const entry = {
  timestamp: $json.processed_at,
  contract_id: $json.contract_id,
  source: $json.source,
  original_message: $json.original_message,
  agent_report: $json.agent_report
};

const serialized = JSON.stringify(entry, Object.keys(entry).sort());
const hash = crypto.createHash('sha256').update(serialized).digest('hex');

return {
  ...$json,
  eat_hash: 'sha256:' + hash
};

--- KONIEC CODE NODU ---

Potom pridaj stlpec "eat_hash" do Google Sheets nodu.
Kazdy zaznam bude mat kryptograficky odtlacok.

---

## 6. Overenie integrity (volitelne, Python)

import json, hashlib

def verify_entry(entry: dict) -> str:
    fields = ['timestamp', 'contract_id', 'source', 'original_message', 'agent_report']
    payload = {k: entry[k] for k in fields}
    serialized = json.dumps(payload, sort_keys=True)
    return 'sha256:' + hashlib.sha256(serialized.encode()).hexdigest()

# Pouzitie:
# expected = verify_entry(row_from_sheet)
# assert expected == row_from_sheet['eat_hash']

---

## Poznamka

EAT Ledger nie je rozhodovaci nastroj.
Je to tamper-evident stopa — ak sa nieco zmenilo, je to viditelne.
Toto je aplikovana Epistemicka Kryptografia v praxi.

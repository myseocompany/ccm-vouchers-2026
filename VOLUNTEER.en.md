# Volunteer guide (English)

Welcome. This repository operates the CCM Vouchers Digitales 2026 program: implementing AriCRM Plan Crecer in 10 restaurants in Manizales, Colombia. Contract CT-239-26-3 between MY SEO COMPANY S.A.S. (contractor) and the Manizales Chamber of Commerce.

**Language rule**: Spanish is the source of truth. The contract, deliverables, communications with the Chamber and with restaurants are all in Spanish. This file exists so you can operate the harness without needing to read every Spanish document.

---

## What this repo is

An operating harness (not code). Each file coordinates work: who does what, when, with what evidence, mapped to specific contractual obligations. The AriCRM product code lives in a separate repo (`../velo_wa/`) and is not modified from here.

## What you must read first

1. **`POLICIES.md`** — the "Datos y secretos" section applies to you literally. English summary below.
2. **`AGENTS.md`** — operating rules for anyone working in the repo.
3. The workflow you're about to execute (in `workflows/`).
4. The client folder for the restaurant you're helping (`clientes/<slug>/`).

## Hard rules (from POLICIES.md — do not break these)

- **Never** send messages, emails or calls to the Chamber or to any restaurant without explicit human approval from Nicolás.
- **Never** modify AriCRM production settings without approval (creating tenants, adding users, connecting WhatsApp numbers, uploading contacts).
- **Never** publish or send any deliverable (report, dashboard) to the Chamber. Only Nicolás signs.
- **Never** share client data across restaurants or with third parties.
- **Never** commit `.env` files, credentials, tokens or end-customer personal data.
- **Never** use end-customer contact data (the ~2000 contacts each restaurant has) as examples, test cases, or for anything outside the contract's purpose.
- **Never** create modules/products named "Vouchers" or "CCM" inside AriCRM — this would put our IP at risk (see IP note below).

## What you can do without asking

- Read anything in this repo (except files listed under "never" above).
- Draft reports, meeting minutes, checklists, workflow updates, English translations of workflow steps.
- Run local scripts in `scripts/` (they are non-destructive by design).
- Reference AriCRM code in `../velo_wa/` (read-only).
- Improve documentation for other volunteers.

## The 10 restaurants

Each has a folder in `clientes/`:
`la-megachuleta`, `la-patateria`, `manuelina`, `friends-chicken-cable`, `arepas-rellenas-samu`, `pizzas-beto`, `el-efecto-barbacoa`, `trattorias-y-pastificios`, `cheesecake-pizza-milan`, `indecente`.

Each folder contains 5 files:
- `clientes/<slug>/CLIENTE.md` — the restaurant's identity, contacts, contract scope.
- `clientes/<slug>/CARACTERIZACION.md` — initial diagnostic (contract obligation 2).
- `clientes/<slug>/TASKS.md` — that restaurant's task list (canonical status).
- `clientes/<slug>/PROGRESS.md` — chronological log with evidence.
- `clientes/<slug>/INFORME.md` — draft of the individual report we owe to the Chamber (obligation 15).

## Workflows

Located in `workflows/`, numbered 01–08, each mapped to a contractual obligation. Execute them in order per restaurant. Each has: prerequisites, steps, acceptance criteria.

| # | Purpose | Contract obligation |
|---|---------|---------------------|
| 01 | Characterization session with the restaurant | 2 |
| 02 | Create and configure AriCRM tenant (3 users, 3 WhatsApp lines, 2000 contacts) | 3, 6 |
| 03 | Activate restaurants vertical (digital menu, orders, reservations) | 4 |
| 04 | AI agent + human escalation | 5 |
| 05 | Training | 7 |
| 06 | Activation and go-live support | 8 |
| 07 | 4-month priority support SLA | 10, 11 |
| 08 | Reports and deliverables | 12–16 |

## IP note (why this matters)

Contract clause 17 assigns to the Chamber the patrimonial rights of "works created in the exercise of contracted functions". Clause 17 §2 preserves pre-existing IP. **AriCRM is pre-existing IP of MY SEO** and must always be treated as such. Any work you do is either:
- Configuration/parameterization of pre-existing AriCRM, or
- Documents specifically for the Chamber (reports, minutes, dashboards) — which are ceded.

Never create anything that could be interpreted as a new product built for this contract.

## Where to write things

- New task for a restaurant → `clientes/<slug>/TASKS.md`.
- Something happened worth logging → `clientes/<slug>/PROGRESS.md`.
- Program-wide task → root `TASKS.md`.
- Decision approved by Nicolás → root `DECISIONS.md`.
- Reusable lesson learned → root `MEMORY.md` (index) + a dedicated file.
- Evidence file (screenshot, log, note) → `evidencias/<slug>/...`.
- Signed final deliverables (to be sent to Chamber) → `entregables/...`.

## When in doubt, ask Nicolás

The contract has a financial penalty of 20% of total value ($1,047,200 COP) for breach, and the Chamber can terminate the contract for data-protection non-compliance. When something feels ambiguous, ask before acting.

Contact: nicolas@myseocompany.co

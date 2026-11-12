# FLA Task 2 – Finite Automata for Real-Time Application Validators

**Course:** 21CSC301T – Formal Language and Automata  
**Assessment:** CLA-2 – Assessment Task 2  
**SDG:** SDG 9 – Industry, Innovation and Infrastructure

## Applications
1. ATM PIN Verification
2. Password Format Validation
3. Email Format Validation

## Objective
Design finite-automata based validators for real-time application input formats.

The project distinguishes:
- **Syntax validation:** whether an input follows a defined regular-language pattern.
- **Semantic/business validation:** whether the input is actually valid in the real application.

## Structure
```text
FLA-Task2-Finite-Automata-Validators/
├── fa_validators/
│   ├── __init__.py
│   ├── automata.py
│   ├── validators.py
│   └── cli.py
├── tests/
│   └── test_validators.py
├── docs/
│   ├── design_note.md
│   ├── state_diagrams.txt
│   └── transition_tables.md
├── app.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Run
```bash
python app.py
```

Interactive mode:
```bash
python -m fa_validators.cli
```

Tests:
```bash
python -m unittest discover -s tests -v
```

## Examples
```text
ATM PIN: 1234 -> ACCEPTED
ATM PIN: 12345 -> REJECTED

Password: Abcd123! -> ACCEPTED
Password: abcdef12 -> REJECTED

Email: student@gmail.com -> ACCEPTED
Email: studentgmail.com -> REJECTED
```

## Academic note
These validators focus on regular-language syntax. A finite automaton cannot verify business meaning such as whether an ATM PIN matches a customer's stored PIN or whether an email account actually exists.

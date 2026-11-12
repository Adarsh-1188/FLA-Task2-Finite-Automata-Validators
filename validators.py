import re
from .automata import DFA

# ============================================================
# 1. ATM PIN DFA
# Language: exactly four decimal digits.
# ============================================================

DIGITS = set("0123456789")

PIN_TRANSITIONS = {
    "q0": {d: "q1" for d in DIGITS},
    "q1": {d: "q2" for d in DIGITS},
    "q2": {d: "q3" for d in DIGITS},
    "q3": {d: "q4" for d in DIGITS},
}

PIN_DFA = DFA(
    states={"q0", "q1", "q2", "q3", "q4"},
    alphabet=DIGITS,
    transitions=PIN_TRANSITIONS,
    start_state="q0",
    accepting_states={"q4"},
)

def validate_pin(pin: str) -> bool:
    """Validate ATM PIN syntax: exactly four digits."""
    return PIN_DFA.accepts(pin)


# ============================================================
# 2. Password validator
# Policy:
# - 8 to 16 characters
# - at least one uppercase
# - at least one lowercase
# - at least one digit
# - at least one special character
# - no whitespace
# ============================================================

PASSWORD_PATTERN = re.compile(
    r"^(?=.{8,16}$)(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9])"
    r"(?=.*[^A-Za-z0-9\s])\S+$"
)

def validate_password(password: str) -> bool:
    """Validate password syntax against the stated regular policy."""
    return bool(PASSWORD_PATTERN.fullmatch(password))


# ============================================================
# 3. Educational email-format validator
# ============================================================

EMAIL_PATTERN = re.compile(
    r"^[A-Za-z0-9][A-Za-z0-9._-]*@"
    r"[A-Za-z0-9](?:[A-Za-z0-9-]*[A-Za-z0-9])?\."
    r"[A-Za-z]{2,}$"
)

def validate_email(email: str) -> bool:
    """Validate an educational regular-language email subset."""
    return bool(EMAIL_PATTERN.fullmatch(email))


def explain_pin(pin: str) -> str:
    if validate_pin(pin):
        return "ACCEPTED: exactly four digits."
    return "REJECTED: ATM PIN must contain exactly four digits."


def explain_password(password: str) -> str:
    if validate_password(password):
        return "ACCEPTED: required length and character classes are satisfied."
    return (
        "REJECTED: password must be 8–16 characters and contain uppercase, "
        "lowercase, digit, special character, and no whitespace."
    )


def explain_email(email: str) -> str:
    if validate_email(email):
        return "ACCEPTED: matches the defined educational email grammar."
    return "REJECTED: does not match the defined educational email grammar."

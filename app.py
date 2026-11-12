from fa_validators.validators import (
    validate_pin, validate_password, validate_email,
    explain_pin, explain_password, explain_email,
)

def show_result(label, value, validator, explanation):
    result = "ACCEPTED" if validator(value) else "REJECTED"
    print(f"{label}: {value!r} -> {result}")
    print(f"  {explanation(value)}")

def main():
    print("=" * 58)
    print(" FLA TASK 2 - FINITE AUTOMATA VALIDATION DEMO")
    print("=" * 58)

    pin_cases = [
        "1234", "0000", "5721", "2468", "9876",
        "123", "12345", "12A4", "abcd", "12 4"
    ]
    password_cases = [
        "Abcd123!", "Strong9@", "A1b2c3$4", "Password1!", "Zx9#abcd",
        "abcdef12", "ABCDEFG!", "Abcdefgh", "Ab1!", "Abcd 123!"
    ]
    email_cases = [
        "student@gmail.com", "a.b@college.edu", "user_123@test.org",
        "hello-world@example.co", "name@domain.in",
        "studentgmail.com", "student@.com", "@gmail.com",
        "user@domain", "user@@gmail.com"
    ]

    print("\n--- ATM PIN ---")
    for value in pin_cases:
        show_result("ATM PIN", value, validate_pin, explain_pin)

    print("\n--- PASSWORD ---")
    for value in password_cases:
        show_result("Password", value, validate_password, explain_password)

    print("\n--- EMAIL ---")
    for value in email_cases:
        show_result("Email", value, validate_email, explain_email)

    print("\nRun 'python -m fa_validators.cli' for interactive validation.")

if __name__ == "__main__":
    main()

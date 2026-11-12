from .validators import (
    validate_pin, validate_password, validate_email,
    explain_pin, explain_password, explain_email,
)

def main():
    print("\n=== FLA Task 2: Finite Automata Validators ===")
    print("1. ATM PIN")
    print("2. Password")
    print("3. Email")
    print("4. Exit")

    while True:
        choice = input("\nChoose an option: ").strip()

        if choice == "1":
            value = input("Enter ATM PIN: ")
            print(explain_pin(value))
        elif choice == "2":
            value = input("Enter password: ")
            print(explain_password(value))
        elif choice == "3":
            value = input("Enter email: ")
            print(explain_email(value))
        elif choice == "4":
            print("Exiting.")
            break
        else:
            print("Invalid menu option.")

if __name__ == "__main__":
    main()

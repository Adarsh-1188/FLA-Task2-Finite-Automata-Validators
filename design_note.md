# Design Note – Finite Automata for Real-Time Application Validators

## 1. Problem statement
Real-time applications need predictable checks for user input. This project models format validation using finite-automata concepts.

## 2. ATM PIN

### Alphabet
Σ = {0,1,2,3,4,5,6,7,8,9}

### Language
L_PIN = { w ∈ Σ* | |w| = 4 }

### States
- q0: no digit read
- q1: one digit read
- q2: two digits read
- q3: three digits read
- q4: exactly four digits read (accepting)

### Transition idea
q0 --digit--> q1 --digit--> q2 --digit--> q3 --digit--> q4

Accepted:
1234, 0000, 5721, 2468, 9876

Rejected:
123, 12345, 12A4, abcd, 12 4

## 3. Password

Policy:
- 8–16 characters
- at least one uppercase
- at least one lowercase
- at least one digit
- at least one special character
- no whitespace

Accepted:
Abcd123!, Strong9@, A1b2c3$4, Password1!, Zx9#abcd

Rejected:
abcdef12, ABCDEFG!, Abcdefgh, Ab1!, Abcd 123!

A full product DFA can track the required character classes and length. The implementation uses an equivalent regular-expression check for clarity.

## 4. Email

Educational grammar:
LOCAL @ DOMAIN . TLD

LOCAL:
- starts with alphanumeric
- may contain letters, digits, '.', '_' and '-'

DOMAIN:
- starts and ends with alphanumeric
- may contain letters, digits and '-'

TLD:
- at least two letters

Accepted:
student@gmail.com
a.b@college.edu
user_123@test.org
hello-world@example.co
name@domain.in

Rejected:
studentgmail.com
student@.com
@gmail.com
user@domain
user@@gmail.com

## 5. Syntax versus semantics

Finite automata are suitable for syntax/format validation.

They cannot by themselves determine:
- whether an ATM PIN is the real PIN stored for a customer;
- whether an email account exists;
- whether a password is present in a leaked-password database;
- whether an account is authorized for a transaction.

Those require additional application/business processing.

## 6. Limitations
1. The email validator is an educational subset, not every RFC email rule.
2. A format-valid PIN may still be incorrect for a user account.
3. A syntactically valid password may still be insecure.
4. Finite automata are pattern recognizers, not general business-rule engines.

## 7. SDG 9
SDG 9 – Industry, Innovation and Infrastructure is addressed through automated, repeatable validation that can be integrated into dependable software infrastructure.

## 8. Five-minute demonstration
1. Explain the problem.
2. Show alphabet and language of the PIN DFA.
3. Demonstrate accepted/rejected PINs.
4. Demonstrate password validation.
5. Demonstrate email validation.
6. Explain syntax vs semantics.
7. Run the automated tests.
8. Explain limitations and SDG 9.

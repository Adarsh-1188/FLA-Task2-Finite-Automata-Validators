# Transition Tables

## ATM PIN DFA

| Current state | Input | Next state |
|---|---|---|
| q0 | digit | q1 |
| q1 | digit | q2 |
| q2 | digit | q3 |
| q3 | digit | q4 |
| q4 | digit | reject |

Accepting state: q4.

## Password
A complete product DFA uses states encoding:
- length;
- uppercase seen/not seen;
- lowercase seen/not seen;
- digit seen/not seen;
- special character seen/not seen;
- invalid/whitespace condition.

## Email

| Stage | Expected input |
|---|---|
| Local start | Alphanumeric |
| Local continuation | Alphanumeric, ., _, - |
| Separator | @ |
| Domain start | Alphanumeric |
| Domain continuation | Alphanumeric, - |
| TLD separator | . |
| TLD | 2+ letters |
| Final | Accept |

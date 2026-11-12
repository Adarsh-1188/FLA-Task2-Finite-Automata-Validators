class DFA:
    """A small deterministic finite automaton implementation."""

    def __init__(self, states, alphabet, transitions, start_state, accepting_states):
        self.states = set(states)
        self.alphabet = set(alphabet)
        self.transitions = transitions
        self.start_state = start_state
        self.accepting_states = set(accepting_states)

    def accepts(self, string):
        """Return True when the complete input is accepted by the DFA."""
        state = self.start_state

        for symbol in string:
            if symbol not in self.alphabet:
                return False

            next_state = self.transitions.get(state, {}).get(symbol)
            if next_state is None:
                return False

            state = next_state

        return state in self.accepting_states

    def trace(self, string):
        """Return the states visited while reading the input."""
        state = self.start_state
        visited = [state]

        for symbol in string:
            next_state = self.transitions.get(state, {}).get(symbol)
            if next_state is None:
                visited.append("DEAD")
                return visited

            state = next_state
            visited.append(state)

        return visited

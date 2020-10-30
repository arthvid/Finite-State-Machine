#!/usr/bin/env python3
from state import State

class FiniteState:

    def __init__(self, states, alphabet, start_state, accept_states):
        """ Args:
                states (array): Contains State objects
         """

        self.states = states

        self.state_mapping = {}
        for state in states:
            self.state_mapping[state.stateId] = state

        self.alphabet = alphabet
        self.start_state = start_state
        self.accept_states = accept_states
        self.characters = []
        self.count = 0



    def run(self, input_string):
        """ Args:
                input_string (string): String being passed into the FSM
        """

        for char in input_string:
            if char not in alphabet:
                print(f"Error: String contains the character {current_char} that doesn't belong to the alphabet of this finite state machine.")
                return 0
            self.characters.append(char)

        terminate = False
        counter = 0
        current_state = self.start_state
        while not terminate:
            char = self.characters[counter]
            current_state = self.state_mapping[current_state.compute_next(char)]
            counter += 1
            self.count += 1

            if self.count == len(self.characters):
                terminate = True

        if current_state in self.accept_states:
            print("FSM terminates successfully - string in language of machine.")
            return 1
        else:
            print("FSM terminates unsuccesfully - string not in language of machine.")
            return 0


if __name__ == "__main__":
    q1 = State(stateId="q1", transition={"0": "q1", "1": "q2"})
    q2 = State(stateId="q2", transition={"0": "q3", "1": "q2"})
    q3 = State(stateId="q3", transition={"0": "q2", "1": "q2"})

    states = [q1, q2, q3]
    accept_states = [q2]
    alphabet = ["0", "1"]
    start_state = q2

    fsm = FiniteState(states, alphabet, start_state, accept_states)
    fsm.run("1001010")

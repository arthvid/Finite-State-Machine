#!/usr/bin/env python3

class State():

    def __init__(self, stateId, transition):

        self.stateId = stateId
        self.transition = transition


    def compute_next(self, character):
        next_state = self.transition[character]
        return next_state

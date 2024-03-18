#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence is None:
        return None
    return len(sentence), sentence[0]

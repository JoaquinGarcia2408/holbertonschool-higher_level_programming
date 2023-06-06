#!/usr/bin/python3
def multiple_returns(sentence):
    long = len(sentence)
    if len(sentence) == 0:
        tup = (long , None)
    else:
        tup = (long, sentence[0])
    return tup
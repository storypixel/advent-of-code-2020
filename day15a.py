#!/usr/bin/env python

import fileinput
from adventils import stacked2list


# lsi is last spoken index
# an lsi of -1 means this number hasn't been spoken before
# si is spoken index
def memory_game(past, targ_turn):
    turn = len(past)
    record = {n: {'lsi': -1, 'si': i+1} for i, n in enumerate(past)}
    ls = past[-1]

    while turn < targ_turn:
        turn = turn + 1
        if record[ls].get('lsi') < 0:
            nS = 0
            lsi = record[nS]["si"]
        else:
            # we are assured by the rules of the game that lsi is defined here
            # next spoken number is last turn minus whatever turn the number had been last spoken
            nS = (turn - 1) - lsi
            try:
                # if this next number has been spoken before, make spoken index the last spoken index to remember for next time
                lsi = record[nS]["si"]
            except KeyError:
                lsi = -1  # this next spoken has not been spoken before now, so last spoken index doesn't exist aka is -1

        # this was convoluted on paper but we just update the record for next spoken
        record[nS] = {'lsi': lsi, 'si': turn}
        if turn == targ_turn:
            print('spoken number is', nS)

        ls = nS


def solve(inp):
    rules = stacked2list(inp, str)
    rules = [int(r) for r in rules[0].split(',')]
    memory_game(rules, 2020)
    memory_game(rules,  30000000)


if __name__ == '__main__':
    # memory_game
    print(solve(fileinput.input()))

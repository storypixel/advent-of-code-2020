#!/usr/bin/env python

import fileinput
from adventils import stacked2list
import numpy
from functools import reduce


# obviously the chinese algorithm stuff isn't mine https://rosettacode.org/wiki/Chinese_remainder_theorem#Functional
def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a*b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod


def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1:
        return 1
    while a > 1:
        q = a // b
        a, b = b, a % b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += b0
    return x1


def solvep1(earliest, busids):
    busids = [int(busid) for busid in busids if busid.isnumeric()]

    fpput = earliest  # fpput first possible pick up time
    while True:
        matches = [busid for busid in busids if fpput % busid == 0]
        if len(matches) > 0:
            break
        fpput = fpput + 1

    wait_time = fpput - earliest
    return wait_time * matches.pop()


def solvep2(busids):
    busids = [int(busid) if busid.isnumeric() else 'x' for busid in busids]
    remainders = []
    for i, b in enumerate(busids):
        if type(b) == int:
            # making it faster to refer to the index which we use to calc stuff
            remainders.append(b - i)

    busids = [int(busid) for busid in busids if type(busid) == int]
    return chinese_remainder(busids, remainders)


def solve(inp):
    rules = stacked2list(inp, str)
    rules = [r.strip() for r in rules]
    earliest = int(rules[0])
    busids = rules[1].split(',')

    p1 = solvep1(earliest, busids)
    print('p1 answer', p1)

    p2 = solvep2(busids)
    print('p1 answer', p2)


if __name__ == '__main__':
    # part1
    print(solve(fileinput.input()))
    # part2

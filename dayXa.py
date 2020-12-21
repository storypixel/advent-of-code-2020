#!/usr/bin/env python

import fileinput
from adventils import stacked2list


def solve(inp):
    rules = stacked2list(inp, str)
    for ru in rules:
        print(ru)


if __name__ == '__main__':
    # part1
    print(solve(fileinput.input()))
    # part2

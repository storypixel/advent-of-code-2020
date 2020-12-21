#!/usr/bin/env python

import fileinput
from adventils import stacked2list
from adventils import strip_newlines


def part1(rules):
    mask = ""
    for r in rules:
        if "mask =" in r:
            mask = r[7:]
            print("mask is now", mask)


def solve(inp):
    rules = stacked2list(inp, str)
    rules = strip_newlines(rules)

    for ru in rules:
        print(ru)

    part1(rules)


if __name__ == '__main__':
    # part1
    print(solve(fileinput.input()))
    # part2

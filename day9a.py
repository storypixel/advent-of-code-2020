#!/usr/bin/env python

import fileinput
from adventils import stacked2list
from itertools import combinations


def solve(inp, preamble_length):
    rules = stacked2list(inp, int)
    for ru in rules:
        ru = ru
        # print(ru)

    pa_len = preamble_length
    i = pa_len
    m = 0
    n = i
    # print(rules[m:n])

    # print('perm', perm)

    while n < len(rules):
        # print(rules[n])
        sub_rules = rules[m:n]
        combos = combinations(sub_rules, 2)
        next_value = rules[n]
        print("next value is", next_value)

        match = None
        for [x, y] in combos:
            sum = x + y
            if sum == next_value:
                match = [x, y]
                break
        if match == None:
            print("the problem number is ", next_value)
            return next_value

        i = i + 1
        m = m + 1
        n = n + 1


def solve2(inp, invalid_number):
    rules = stacked2list(inp, int)
    for ru in rules:
        ru = ru
        # print(ru)

    i = 0
    while i < len(rules):
        total = 0
        span = 2
        while total < invalid_number:
            sub_rules = rules[i:i+span]
            total = sum(sub_rules)
            if total == invalid_number:
                print("eureka found numbers", sub_rules)
                #       sub_rules[0] + sub_rules[-1])
                src = sub_rules.copy()
                src.sort()
                return src[0] + src[-1]
            span = span + 1
        i = i + 1


if __name__ == '__main__':
    # part1
    # print(solve(fileinput.input(), 25))
    # part2
    print(solve2(fileinput.input(), 25918798))
    # part2

#!/usr/bin/env python

import fileinput
from adventils import stacked2list


def check_for_buddy(x, num_list):
    # find a number from num_list such that x + _num_ == 2020
    for i in num_list:
        # print('sum is', i + x)
        if i + x == 2020:
            return (i, x)
    return (0, 0)


def find_match_of_2(inp):
    num_list = stacked2list(inp)
    for i in num_list:
        res = check_for_buddy(i, num_list)
        if res[0] + res[1] > 0:
            break
    return res[0] * res[1]


def find_match_of_3(inp):
    num_list = stacked2list(inp)
    for i in num_list:
        for j in num_list:
            for k in num_list:
                if i + j + k == 2020:
                    return i * j * k


if __name__ == '__main__':
    # part1
    print(find_match_of_2(fileinput.input()))
    # part2
    print(find_match_of_3(fileinput.input()))

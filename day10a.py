#!/usr/bin/env python

import fileinput
from adventils import stacked2list
import itertools
import numpy  # installed numpy with 'conda' and 'conda activate py3' which i installed with 'conda create --name py3 python=3.5`


# subset will look like(1, 5, 6) or (1, 2, 4, 5, 8)
# invalid and valid respectively
def subset_is_valid(subset):
    last_num = 0
    # if there is a gap in this sequence greater than 3 it's invalid sequence for us
    for num in subset:
        if num > last_num + 3:
            return False
        last_num = num
    return True


# the diff_string looks like
# ['1111', '', '111', '1111', '111', '11', '111', '11', '', '111', '', '11', '', '1111', '111', '11', '11', '111', '111', '', '1111', '11', '1111', '', '1111', '', '111', '1', '1', '', '', '1111', '1111', '111', '']
def get_multi_from_shit(diff_str):
    if diff_str == '':
        return []
    stuff = range(1, len(diff_str) + 1)
    last_el = stuff[-1]
    good_ones = []
    for L in range(0, len(stuff)+1):
        for subset in itertools.combinations(stuff, L):
            if last_el in subset and subset_is_valid(subset):
                # print(subset)
                good_ones.append(subset)
            else:
                last_el = last_el
                # print(subset, ' is illegal')

    return good_ones


def solve(inp):
    i = 0
    diffs = []
    kolts = stacked2list(inp, int)
    kolts = sorted(kolts)
    kolts = [0] + kolts + [kolts[-1] + 3]

    while i < (len(kolts) - 1):
        diff = kolts[i + 1] - kolts[i]
        diffs.append(diff)
        i = i + 1

    # part 1 stuff
    dict_diffs = {}

    for _, val in enumerate(diffs):
        try:
            dict_diffs[val] = dict_diffs[val] + 1
        except KeyError:
            dict_diffs[val] = 1

    # part 2 stuff
    diffs = ''.join([str(n) for n in diffs])
    # diffs = ['13113111311113111113111111']
    diffs = diffs.split('3')
    # diffs = ['1', '11', '111', '1111', '11111', '111111']

    # collect some multiples that we can multiply together to get the answer of possible combos
    multis = []
    for big_pile in diffs:
        if big_pile != '':
            multi = get_multi_from_shit(big_pile)
            multis.append(len(multi))

    # multiply all of the numbers from the '1111' and '11'
    prod = numpy.prod(multis)

    return (dict_diffs.get(3) * dict_diffs.get(1), prod)


if __name__ == '__main__':
    # part1, part2
    print(solve(fileinput.input()))

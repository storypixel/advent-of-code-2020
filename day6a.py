#!/usr/bin/env python

import fileinput
from adventils import blanks2list


def find_num_common_yesses(form):
    lines = [set([*line]) for line in form.split('\n')]
    common_yesses = set.intersection(*lines)
    return len(common_yesses)


def get_custdec_data_intersections(inp):
    forms = blanks2list(inp)  # returns dict
    yesses = 0
    for f in forms:
        yesses = yesses + find_num_common_yesses(f)
    return (yesses)


def get_custdec_data(inp):
    forms = blanks2list(inp)  # returns dict
    yesses = 0
    for f in forms:
        f = f.replace('\n', '')
        f = (set([*f]))
        yesses = yesses + len(f)

    return (yesses)


if __name__ == '__main__':
    # part1
    print(get_custdec_data(fileinput.input()))
    # part2
    print(get_custdec_data_intersections(fileinput.input()))

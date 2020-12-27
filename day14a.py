#!/usr/bin/env python

import fileinput
import re
import numpy
import itertools
from adventils import stacked2list
from adventils import strip_newlines


def process_with_mask(val, mask):
    mask = [*mask]
    val = numpy.binary_repr(val, width=36)
    val = [*val]

    for i, m in enumerate(mask):
        if m == 'X':
            continue
        if m == '0' or '1':
            val[i] = m

    return ''.join(val)  # e.g. '001000000100110100101011110000000010'


# When this program goes to write to memory address 42, it first applies the bitmask:

# address: 000000000000000000000000000000101010  (decimal 42)
# mask:    000000000000000000000000000000X1001X
# result:  000000000000000000000000000000X1101X
def process_with_mask2(val, mask):
    # If the bitmask bit is 0, the corresponding memory address bit is unchanged.
    # If the bitmask bit is 1, the corresponding memory address bit is overwritten with 1.
    # If the bitmask bit is X, the corresponding memory address bit is floating.
    mask = [*mask]
    val = numpy.binary_repr(val, width=36)
    val = [*val]

    for i, m in enumerate(mask):
        if m == 'X':
            val[i] = 'X'
        if m == '0':
            continue
        if m == '1':
            val[i] = '1'

    num_floats = val.count('X')

    if num_floats == 0:
        return [val]

    values = [0, 1]
    potents = itertools.product(values, repeat=num_floats)

    mask = ''.join(mask)
    val = ''.join(val)
    results = []
    for p in potents:
        p = list(p)
        res = re.sub('X', '{}', val).format(*p)
        results.append(res)

    # print("results for val", len(results), "\n", '\n'.join(results))
    return results


def part2(rules):

    # print('study', list(per))

    # re.sub('X', '{}', line).format(*list)

    mask = ""
    register = {}
    for r in rules:
        if "mask =" in r:
            mask = r[7:]
            # print("mask is now", mask)
        else:
            addr, val = r.split('=')
            # excavate the numbers from the strings for address and value
            res = re.findall('\d+', addr)
            addr = int(res[0])
            res = re.findall('\d+', val)
            val = int(res[0])
            mems = process_with_mask2(addr, mask)
            # print(addr, val)
            for addr in mems:
                converted = int(addr, base=2)
                # print("writing to address", addr, ":", converted)
                register[converted] = val

    # print('final', register)

    total = sum(register.values())

    print('answer2', total)


def part1(rules):
    mask = ""
    register = {}
    for r in rules:
        if "mask =" in r:
            mask = r[7:]
            # print("mask is now", mask)
        else:
            addr, val = r.split('=')
            # excavate the numbers from the strings for address and value
            res = re.findall('\d+', addr)
            addr = int(res[0])
            res = re.findall('\d+', val)
            val = int(res[0])
            val = process_with_mask(val, mask)
            # print(addr, val)
            register[addr] = int(val, base=2)

    # print('final', register)

    total = sum(register.values())

    print('answer1', total)


def solve(inp):
    rules = stacked2list(inp, str)
    rules = strip_newlines(rules)

    # for ru in rules:
    #     print(ru)

    part1(rules)
    part2(rules)


if __name__ == '__main__':
    # part1
    print(solve(fileinput.input()))
    # part2

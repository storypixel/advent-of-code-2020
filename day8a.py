#!/usr/bin/env python

import fileinput
from adventils import stacked2list


def acc(rules, delta, accumulator, index):
    accumulator = accumulator + delta
    index = index + 1
    print('acc', delta, accumulator, index)
    return (accumulator, index)


def jmp(rules, delta, accumulator, index):
    index = index + delta
    print('jmp', delta, accumulator, index)
    return (accumulator, index)


def nop(rules, delta, accumulator, index):
    index = index + 1
    print('nop', delta, accumulator, index)
    return (accumulator, index)


def isFinished(rules, index):
    return index >= len(rules)


def solve(inp):
    ops = {
        'acc': acc,
        'jmp': jmp,
        'nop': nop,
    }

    accumulator = 0
    index = 0
    rules = stacked2list(inp, str)
    rules = [ru.rstrip() for ru in rules]
    used_rules = {}
    print(rules)
    while True:
        if used_rules.get(index):
            print("about to repeat, breaking instead")
            break
        rule = rules[index]
        used_rules[index] = rule
        instruction, delta = rule.split(' ')
        delta = int(delta)
        accumulator, index = ops.get(instruction)(
            rules, delta, accumulator, index)
        print('instruction and delta', instruction, delta)
        print('index is', accumulator, index)

    print('final values for accumulator and index', accumulator, index)
    # print("used rules", used_rules)


# change a rule at the index from acc to jmp or vice versa
def change_rules(rules, index):
    rule = rules[index]
    rule_copy = rule

    rule = rule.replace("jmp", "nop")
    print("rule after jmp replaced by nop ", rule)
    if rule != rule_copy:
        rules[index] = rule
        return rules

    rule_copy = rule_copy.replace("nop", "jmp")
    rules[index] = rule_copy

    return rules


def solve2(inp):
    ops = {
        'acc': acc,
        'jmp': jmp,
        'nop': nop,
    }

    accumulator = 0
    index = 0
    rules = stacked2list(inp, str)
    rules = [ru.rstrip() for ru in rules]
    orig_rules = rules.copy()
    print("orig rules", orig_rules[0])
    used_rules = {}
    # print(rules)
    changed_index = 0
    while True:
        if index >= len(rules):
            print("it terminated!!! made it! ", accumulator, index)
            break
        if used_rules.get(index):
            print("rules were", rules)
            rules = change_rules(orig_rules.copy(), changed_index)
            print("rules are now", rules)
            used_rules = {}
            accumulator = 0
            index = 0
            changed_index = changed_index + 1
            print("about to repeat, breaking instead",
                  changed_index, len(rules))
            continue
        rule = rules[index]
        used_rules[index] = rule
        instruction, delta = rule.split(' ')
        delta = int(delta)
        accumulator, index = ops.get(instruction)(
            rules, delta, accumulator, index)
        print('instruction and delta', instruction, delta)
        print('index is', accumulator, index)


if __name__ == '__main__':
    # part1
    # print(solve(fileinput.input()))
    # part2
    print(solve2(fileinput.input()))

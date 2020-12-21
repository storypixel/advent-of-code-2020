#!/usr/bin/env python

import fileinput
import sys
from adventils import stacked2list


def password_is_valid_by_count(rule, letter, pw):
    mini, maxi = rule
    how_many = pw.count(letter)
    return int(mini) <= how_many <= int(maxi)


def password_is_valid_by_pos(rule, letter, pw):
    mini, maxi = rule
    mini = int(mini)
    maxi = int(maxi)
    mpw = " "+pw  # lazy convert to 1-index
    matches = int(mpw[mini] == letter) + int(mpw[maxi] == letter)
    return matches == 1


def find_num_valid_passwords_by_count(passwords):
    num_valids = 0
    for line in passwords:
        rule, letter, pw = line.strip().split(" ")
        rule = rule.split('-')
        letter = letter[0]
        if (password_is_valid_by_count(rule, letter, pw)):
            num_valids = num_valids + 1
    return num_valids


def find_num_valid_passwords_by_pos(passwords):
    num_valids = 0
    for line in passwords:
        rule, letter, pw = line.strip().split(" ")
        rule = rule.split('-')
        letter = letter[0]
        if (password_is_valid_by_pos(rule, letter, pw)):
            num_valids = num_valids + 1
    return num_valids


if __name__ == '__main__':
    passwords = stacked2list(fileinput.input(), str)
    # part1
    print(find_num_valid_passwords_by_count(passwords))
    # part2
    print(find_num_valid_passwords_by_pos(passwords))
    # print(find_match_of_3(fileinput.input()))

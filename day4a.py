#!/usr/bin/env python
import sys
import re

import fileinput
from adventils import stacked2list
from itertools import groupby

FIELDS = {
    'byr',  # (Birth Year)
    'iyr',  # (Issue Year)
    'eyr',  # (Expiration Year)
    'hgt',  # (Height)
    'hcl',  # (Hair Color)
    'ecl',  # (Eye Color)
    'pid',  # (Passport ID)
    # not req -> 'cid',  # (Country ID)
}

FIELDS_REGEX = {
    'byr':  '^(19[2-8][0-9]|199[0-9]|20[01][0-9]|2020)$',  # (Birth Year)
    'iyr':  '^(201[0-9]|2020)$',  # (Issue Year)
    'eyr':  '^(202[0-9]|2030)$',  # (Expiration Year)
    # (Height)
    'hgt':  '(^(1[5-8][0-9]|19[0-3])+cm$)' + '|' + '(^(59|6[0-9]|7[0-6])+in$)',
    'hcl':  '^#([0-9]|[a-f]){6}$',  # (Hair Color)
    'ecl':  '^(amb|blu|brn|gry|grn|hzl|oth)$',  # (Eye Color)
    'pid':  '^[0-9]{9}$',  # (Passport ID)
    # not req -> 'cid',  # (Country ID)
}
# byr (Birth Year) - four digits; at least 1920 and at most 2002.
# iyr (Issue Year) - four digits; at least 2010 and at most 2020.
# eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
# hgt (Height) - a number followed by either cm or in:
# If cm, the number must be at least 150 and at most 193.
# If in, the number must be at least 59 and at most 76.
# hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
# ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
# pid (Passport ID) - a nine-digit number, including leading zeroes.
# cid (Country ID) - ignored, missing or not.


def validate_passport(passport):
    # print('validating fields', passport)
    print('##########')
    for key, rule in FIELDS_REGEX.items():
        pp_value = passport.get(key)
        print(bool(re.match(rule, str(pp_value))), 'with', key, ':',
              passport.get(key), '-???-', rule)
        if bool(re.match(rule, str(pp_value))) == False:
            print("%%FAILED VALIDATION")
            return False
    return True


def normalize_passports(passports):
    passports = ''.join(list(str(line) for line in passports)).split('\n\n')
    passports = map(lambda pp: pp.replace('\n', ' '), passports)
    passports = map(lambda p: p.split(' '), passports)
    passports = map(process_fields, passports)
    # passports = map(lambda pp: pp.split(' '), passports))
    return passports


def process_fields(fields):
    # an array of tuples can be used to initiate a dict
    return dict([tuple(f.split(":"))
                 for f in fields
                 ])
    # res = []
    # for f in fields:
    #     print('field is', f)
    #     # res.insert(tuple(f.split(":")), 0)
    # print(res)
    # return res


def find_valid_passports(inp):
    passports = normalize_passports(inp)  # returns dict
    matches = 0
    validated_matches = 0
    for pp in passports:
        pp_fields = set(pp.keys())
        pp_fields.discard("cid")
        validated = validate_passport(pp)
        if pp_fields == FIELDS:
            matches = matches + 1
        if validated:
            validated_matches = validated_matches + 1

    return (matches, validated_matches)


if __name__ == '__main__':
    # part1
    # day 2, part 2 i got 159 but the right answer is 158 one of my regexes is off
    print(find_valid_passports(fileinput.input()))
    # part2
    # print('oh', re.match(  '^[0-9]{6}$', '001192'))

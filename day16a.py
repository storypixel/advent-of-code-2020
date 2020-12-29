#!/usr/bin/env python

import fileinput
from adventils import stacked2list
from adventils import flatten
import numpy


def get_error_rate(rulesets, ticks):
    combined_rules = [rs.get('range') for rs in rulesets]
    combined_rules = list(flatten(combined_rules))
    combined_ticket_values = [t for t in ticks]
    combined_ticket_values = list(flatten(combined_ticket_values))
    combined_ticket_values = list(map(int, combined_ticket_values))
    exclusions = [
        item for item in combined_ticket_values if item not in combined_rules]
    return exclusions


def filter_out_bad_ticks(rulesets, ticks):
    valid_ticks = []
    combined_rules = [rs.get('range') for rs in rulesets]
    combined_rules = list(flatten(combined_rules))
    for tick in ticks:
        exclusions = [
            item for item in tick if int(item) not in combined_rules]
        # print('exlcusioins are', exclusions)
        if len(exclusions) == 0:
            valid_ticks.append(tick)

    return valid_ticks


def solve(inp):
    rules, ticks, nby_ticks = ''.join(list(str(line)
                                           for line in inp)).split('\n\n')

    # 1. process the data
    rules = rules.split('\n')
    rules = [r.split(' ') for r in rules]
    rulesets = []
    for r in rules:
        *label, range1, _, range2 = r
        label = ' '.join(label)  # account for labels of >1 word

        # label = label.rstrip(':')
        range1 = [int(n) for n in range1.split('-')]
        range2 = [int(n) for n in range2.split('-')]
        rulesets.append({
            'label': label,
            'range': list(range(range1[0], range1[1] + 1)) + list(range(range2[0], range2[1] + 1))
        })

    ticks = ticks.split('\n')
    del ticks[0]
    ticks = [t.split(',') for t in ticks]
    nby_ticks = nby_ticks.split('\n')
    del nby_ticks[0]
    nby_ticks = [t.split(',') for t in nby_ticks]

    # 2. Solve
    # a) part 1 solve
    array_of_exceptions = get_error_rate(rulesets, nby_ticks)
    total = sum(array_of_exceptions)
    print("final part 1 total is", total)

    # b) part 2 solve
    nby_ticks = filter_out_bad_ticks(rulesets, nby_ticks)
    # print("valid ticks", nby_ticks)
    stats = zip(*nby_ticks)
    stats = [list(s) for s in stats]
    stat_matches = list(range(len(rulesets)))
    stat_matches = [list() for i in stat_matches]
    for i, stat in enumerate(stats):
        # print("\n\nlooking at stat", i, stat)

        for k, rs in enumerate(rulesets):
            nrange = rs.get('range')
            nlabel = rs.get('label')
            exclusions = [
                item for item in stat if int(item) not in nrange]
            if len(exclusions) == 0:
                stat_matches[i].append(nlabel)

    stat_match_scaffold = stat_matches.copy()
    stat_match_scaffold = sorted(stat_match_scaffold, key=len)
    stat_match_scaffold = list(reversed(stat_match_scaffold))

    # lista = [['a', 'b', 'c', 'd'],  ['a', 'b'], ['a'], ['a', 'b', 'c']]
    lista = stat_matches
    record = list(range(len(lista)))

    while True:
        filtered = [item for item in lista if len(item) == 1]
        if len(filtered) == 0:
            break
        filtered = filtered[0]
        filtered_index = lista.index(filtered)
        filtered = filtered[0]
        record[filtered_index] = filtered
        for i, item in enumerate(lista):
            if filtered in lista[i]:
                lista[i].remove(filtered)

    ticks = flatten(ticks)
    recomposed_ticket = list(zip(record, ticks))

    departure_related = [
        item for item in recomposed_ticket if 'departure' in item[0]]
    departure_related = [
        int(item[1]) for item in recomposed_ticket if 'departure' in item[0]]
    prod = numpy.prod(departure_related)
    print("part2 answer is", departure_related, prod)
    # your ticket, class is 12, row is 11, and seat is 13.


if __name__ == '__main__':
    # part1
    print(solve(fileinput.input()))
    # part2

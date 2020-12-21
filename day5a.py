#!/usr/bin/env python
import sys
import re

import fileinput
from adventils import stacked2list


def calc_id(r, c):
    return r * 8 + c


def find_seats(inp):
    seats = map(lambda s: s.strip(), stacked2list(inp, str))

    highest_seat_id = 0
    seat_list = []
    for s in seats:
        row_num = s[:7].replace('F', '0').replace('B', '1')
        row_num = (int(row_num, 2))
        col_num = s[7:].replace('L', '0').replace('R', '1')
        col_num = (int(col_num, 2))
        seat_id = calc_id(row_num, col_num)
        # part 1
        highest_seat_id = seat_id if seat_id > highest_seat_id else highest_seat_id
        seat_list.append(seat_id)
        # print("row is ", row_num, " col is ", col_num, " seat id ", seat_id)

    seat_list = sorted(seat_list)

    # part 2
    # note i manually select 48 to save time, it could be written more dynamically but it saved me 20 minutes so i did it the lazy way
    # my seat num is assumed to be length 1
    my_seat_num = list(set([*range(48, 819)]) - set(seat_list)).pop()

    return (highest_seat_id, my_seat_num)


if __name__ == '__main__':
    # part1 and part2 as tuple
    print(find_seats(fileinput.input()))

#!/usr/bin/env python

import fileinput
import sys
import operator
from adventils import grid2dict

TREE = '#'
NONTREE = '.'


def get_pos(val, max):
    return val % max


def get_new_seat2(grid, locus, seat):
    # similar to get_new_seat but for part 2. there is a lot of redundancy that could be optimized but ya know

    # let's find out how far we need to 'look' in a direction
    w = (max(grid, key=operator.itemgetter(0)))[0] + 1

    STATES = {
        '.': 'FLOOR',
        'L': 'EMPTY',
        '#': 'OCCUPIED',
    }

    # look in these directions. for part 2 we end up 'scaling' this search
    seat_shifts = [
        (0, 1),  # to the right... scale this to (0, 2) then (0, 3) and (0, n) until we look off edge or find a seat
        (0, -1),  # left
        (1, 0),  # above
        (-1, 0),  # below
        (-1, -1),  # top left
        (-1, 1),  # bottom left
        (1, -1),  # top right
        (1, 1),  # bottom right
    ]

    # horribly inefficient but easy to program:
    survey = {'FLOOR': 0, 'EMPTY': 0, 'OCCUPIED': 0}

    for shift in seat_shifts:
        for scalar in range(1, w+1):
            nearby_locus = tuple(
                map(operator.add, locus, scale_shift(shift, scalar)))
            nearby_seat = grid.get(nearby_locus)
            # print('adding tuples', new_locus, 'was', locus)
            if nearby_seat != '.':
                if nearby_seat == 'L' or nearby_seat == '#':
                    # a real seat type
                    dist_key = STATES.get(nearby_seat)
                    survey[dist_key] = survey[dist_key] + 1
                    break
                if nearby_seat == None:
                    # off the edge
                    break
    # If a seat is empty (L) and there are no occupied seats adjacent to it, the seat becomes occupied.
    # If a seat is occupied (#) and five or more seats adjacent to it are also occupied, the seat becomes empty.
    # Otherwise, the seat's state does not change.
    if seat == 'L' and survey.get('OCCUPIED') == 0:
        return (locus, '#')

    if seat == '#' and survey.get('OCCUPIED') >= 5:
        return (locus, 'L')

    return (locus, seat)


def scale_shift(shift, scalar):
    return tuple(map(operator.mul, shift, (scalar, scalar)))


def get_new_seat(grid, locus, seat):
    # w = (max(grid, key=operator.itemgetter(0)))[0] + 1
    # h = (max(grid, key=operator.itemgetter(1)))[1] + 1

    STATES = {
        '.': 'FLOOR',
        'L': 'EMPTY',
        '#': 'OCCUPIED',
    }

    seat_shifts = [
        (0, 1),  # to the right
        (0, -1),  # left
        (1, 0),  # above
        (-1, 0),  # below
        (-1, -1),  # top left
        (-1, 1),  # bottom left
        (1, -1),  # top right
        (1, 1),  # bottom right
    ]

    survey = {'FLOOR': 0, 'EMPTY': 0, 'OCCUPIED': 0}

    # look around thiis chair and gather stats
    for shift in seat_shifts:
        nearby_locus = tuple(map(operator.add, locus, shift))
        nearby_seat = grid.get(nearby_locus)
        # print('adding tuples', new_locus, 'was', locus)
        if nearby_seat != None:
            dist_key = STATES.get(nearby_seat)
            survey[dist_key] = survey[dist_key] + 1
        # print('locus and seat tuples', nearby_locus, ':', nearby_seat)

    # print("distribution are", survey)

    # If a seat is empty (L) and there are no occupied seats adjacent to it, the seat becomes occupied.
    # If a seat is occupied (#) and four or more seats adjacent to it are also occupied, the seat becomes empty.
    # Otherwise, the seat's state does not change.
    if seat == 'L' and survey.get('OCCUPIED') == 0:
        return (locus, '#')

    if seat == '#' and survey.get('OCCUPIED') >= 4:
        return (locus, 'L')

    return (locus, seat)


def get_num_occupied_seats(grid, part):
    w = (max(grid, key=operator.itemgetter(0)))[0] + 1
    h = (max(grid, key=operator.itemgetter(1)))[1] + 1
    print('dims are', (w, h))

    if part == 1:
        get_seat = get_new_seat
    elif part == 2:
        get_seat = get_new_seat2

    next_grid = {}
    while True:
        for locus in grid:
            seat = grid.get(locus)
            next_locus, next_seat = get_seat(grid, locus, seat)
            next_grid[next_locus] = next_seat
        if next_grid == grid:
            break
        grid = next_grid.copy()

    # print('done with grid changes', grid)
    num_occupied_seats = sum(val == '#' for val in grid.values())

    return num_occupied_seats


if __name__ == '__main__':
    grid = grid2dict(fileinput.input())
    # part1
    # print(get_num_occupied_seats(grid, 1))
    # part2
    print(get_num_occupied_seats(grid, 2))

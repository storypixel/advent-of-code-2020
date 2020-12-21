#!/usr/bin/env python

import fileinput
import operator
import math
from adventils import stacked2list


def scale_shift(shift, scalar):
    return tuple(map(operator.mul, shift, (scalar, scalar)))


def add_shift(shift, position):
    return tuple(map(operator.add, shift, position))

# Almost all of the actions indicate how to move a waypoint which is relative to the ship's position:

# Action N means to move the waypoint north by the given value.
# Action S means to move the waypoint south by the given value.
# Action E means to move the waypoint east by the given value.
# Action W means to move the waypoint west by the given value.
# Action L means to rotate the waypoint around the ship left (counter-clockwise) the given number of degrees.
# Action R means to rotate the waypoint around the ship right (clockwise) the given number of degrees.
# Action F means to move forward to the waypoint a number of times equal to the given value.
# The waypoint starts 10 units east and 1 unit north relative to the ship. The waypoint is relative to the ship; that is, if the ship moves, the waypoint moves with it.

# For example, using the same instructions as above:

# F10 moves the ship to the waypoint 10 times (a total of 100 units east and 10 units north), leaving the ship at east 100, north 10. The waypoint stays 10 units east and 1 unit north of the ship.
# N3 moves the waypoint 3 units north to 10 units east and 4 units north of the ship. The ship remains at east 100, north 10.
# F7 moves the ship to the waypoint 7 times (a total of 70 units east and 28 units north), leaving the ship at east 170, north 38. The waypoint stays 10 units east and 4 units north of the ship.
# R90 rotates the waypoint around the ship clockwise 90 degrees, moving it to 4 units east and 10 units south of the ship. The ship remains at east 170, north 38.
# F11 moves the ship to the waypoint 11 times (a total of 44 units east and 110 units south), leaving the ship at east 214, south 72. The waypoint stays 4 units east and 10 units south of the ship.
# After these operations, the ship's Manhattan distance from its starting position is 214 + 72 = 286.


def make_trail_part2(rules):

    position = (0, 0)  # start from center
    waypoint = (10, 1)

    vectors = [
        (0, 1),
        (1, 0),  # East
        (0, -1),
        (-1, 0),
    ]

    # i don't fucking know python well enough to make this better
    guide = {
        'N': 0,
        'E': 1,
        'S': 2,
        'W': 3,
    }

    shift = (0, 0)
    for r in rules:
        # print('rule is ', r)
        action = r.get('action')
        value = r.get('value')

        if action in guide.keys():  # N, E, S, W
            # print("directional", action)
            waypoint = add_shift(waypoint, scale_shift(
                vectors[guide.get(action)], value))
            shift = (0, 0)
            # print("waypoint is now", waypoint)
        elif action in ['L', 'R']:
            scalar = 1 if action == 'R' else -1
            # ori_idx = int(ori_idx + scalar * value /
            #               90) % len(vectors)
            # vector = vectors[ori_idx]

            theta = math.radians(scalar * value)
            waypoint = rotate_origin_only(waypoint, theta)
            # waypoint = scale_shift(vector, waypoint)
            shift = (0, 0)  # just change orientation don't move
        elif action == 'F':
            vector = waypoint
            shift = scale_shift(vector, value)
            # print("shift is now", shift)

        position = tuple(map(operator.add, position, shift))
        # print("position after", r, "is now", position, '\n\n')
    return position


def make_trail(rules):

    position = (0, 0)  # start from center
    ori_idx = 1  # East

    vectors = [
        (0, 1),
        (1, 0),  # East
        (0, -1),
        (-1, 0),
    ]

    # i don't fucking know python well enough to make this better
    guide = {
        'N': 0,
        'E': 1,
        'S': 2,
        'W': 3,
    }

    shift = (0, 0)
    for r in rules:
        action = r.get('action')
        value = r.get('value')

        if action in guide.keys():  # N, E, S, W
            shift = scale_shift(vectors[guide.get(action)], value)
        elif action in ['L', 'R']:
            scalar = 1 if action == 'R' else -1
            ori_idx = int(ori_idx + scalar * value /
                          90) % len(vectors)
            shift = (0, 0)  # just change orientation don't move
        elif action == 'F':
            vector = vectors[ori_idx]
            shift = scale_shift(vector, value)

        position = tuple(map(operator.add, position, shift))
    return position


def rotate_origin_only(xy, radians):
    """Only rotate a point around the origin (0, 0)."""
    x, y = xy
    xx = x * math.cos(radians) + y * math.sin(radians)
    yy = -x * math.sin(radians) + y * math.cos(radians)

    return xx, yy


def solve(inp):
    rules = stacked2list(inp, str)
    rules = [r.strip() for r in rules]
    rules = [{'action': r[0], 'value': int(r[1:])}
             for r in rules
             ]

    final_pos = make_trail(rules)  # part 1

    answer1 = abs(final_pos[0]) + abs(final_pos[1])
    print('answer for part 1 is ', answer1)

    final_pos = make_trail_part2(rules)  # part 1
    answer2 = abs(final_pos[0]) + abs(final_pos[1])

    print('answer for part 2 is ', int(answer2))


if __name__ == '__main__':
    # part1
    print(solve(fileinput.input()))
    # part2

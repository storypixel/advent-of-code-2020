#!/usr/bin/env python

import fileinput
import sys
from operator import itemgetter
from adventils import grid2dict

TREE = '#'
NONTREE = '.'


def get_pos(val, max):
    return val % max


def find_tree_path(grid, rs=3, ds=1):
    # grid is a dict of trees
    # rs is right step amount
    # ds is down step amount
    w = (max(grid, key=itemgetter(0)))[0] + 1
    h = (max(grid, key=itemgetter(1)))[1] + 1
    print('dims are', (w, h))
    s = 1  # step
    i = 1

    num_trees = 0
    while s < h:
        xi = get_pos(i * rs, w)  # x index
        yi = get_pos(i * ds, h)  # y index
        val = grid.get((xi, yi))  # get value at (xi, yi)
        print('step ', s, ' (xi, yi) ', (xi, yi), 'val of', val)
        if val == TREE:
            num_trees = num_trees + 1
        s = s + ds
        i = i + 1

    # for el in grid:
    # print(el, grid.get(el))
    # print(grid.get((i, 0)))
    return num_trees


def find_tree_paths_product(grid):
    # Right 1, down 1.
    # Right 3, down 1. (This is the slope you already checked.)
    # Right 5, down 1.
    # Right 7, down 1.
    # Right 1, down 2.
    paths = [
        {'rs': 1, 'ds': 1},
        {'rs': 3, 'ds': 1},
        {'rs': 5, 'ds': 1},
        {'rs': 7, 'ds': 1},
        {'rs': 1, 'ds': 2},
    ]

    product = 1
    for slope in paths:
        product = product * \
            find_tree_path(grid, slope.get('rs'), slope.get('ds'))

    return product


if __name__ == '__main__':
    tree_grid = grid2dict(fileinput.input())
    # part1
    print(find_tree_path(tree_grid))
    # part2
    print(find_tree_paths_product(tree_grid))
    # print(find_num_valid_passwords_by_pos(passwords))
    # print(find_match_of_3(fileinput.input()))

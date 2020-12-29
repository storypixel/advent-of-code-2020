

import fileinput
import itertools
import operator
from adventils import stacked2list


def grid4dict(inp, type=str):
    grid = {
        (x, y, 0, 0): v
        for y, row in enumerate(inp)
        for x, v in enumerate(row.strip())
    }
    return grid


def grid3dict(inp, type=str):
    grid = {
        (x, y, 0): v
        for y, row in enumerate(inp)
        for x, v in enumerate(row.strip())
    }
    return grid


def get_cube(grid, locus, cube, shifts):

    STATES = {
        '.': 'INACTIVE',
        '#': 'ACTIVE',
    }

    survey = {'INACTIVE': 0, 'ACTIVE': 0}

    # look around this chair and gather stats
    for shift in shifts:
        nearby_locus = tuple(map(operator.add, locus, shift))
        nearby_cube = grid.get(nearby_locus)

        if nearby_cube != None:
            dist_key = STATES.get(nearby_cube)
            survey[dist_key] = survey[dist_key] + 1
    # print('locus and cube tuples', nearby_locus, ':', nearby_cube)

    # During a cycle, all cubes simultaneously change their state according to the following rules:
    if cube == '#':
        # If a cube is active
        if survey.get('ACTIVE') == 2 or survey.get('ACTIVE') == 3:
            # and exactly 2 or 3 of its neighbors are also active, the cube remains active.
            return (locus, '#')
        else:
            # Otherwise, the cube becomes inactive.
            return (locus, '.')
    if cube == '.':
        # If a cube is inactive
        if survey.get('ACTIVE') == 3:
            # but exactly 3 of its neighbors are active, the cube becomes active.
            return (locus, '#')
        else:
            # Otherwise, the cube remains inactive.
            return (locus, '.')

    return (locus, cube)


def pretty_print_grid(grid):
    mw = (min(grid, key=operator.itemgetter(0)))[0]
    mh = (min(grid, key=operator.itemgetter(1)))[1]
    md = (min(grid, key=operator.itemgetter(2)))[2]
    w = (max(grid, key=operator.itemgetter(0)))[0] + 1
    h = (max(grid, key=operator.itemgetter(1)))[1] + 1
    d = (max(grid, key=operator.itemgetter(2)))[2] + 1
    # print("min, max", mw, mh, md, w, h, d)
    # print("grid", grid)
    for z in range(md, d):
        print("\n\nz of ", z)
        for y in range(mh, h):
            line = ''
            for x in range(mw, w):
                line = line + grid[(x, y, z)]
            print(line)


def part1(grid, shifts):
    next_grid = {}
    cycle = 0
    cycle_max = 6

    w = (max(grid, key=operator.itemgetter(0)))[0] + 1
    h = (max(grid, key=operator.itemgetter(1)))[1] + 1
    d = (max(grid, key=operator.itemgetter(2)))[2] + 1

    # just make the grid big enough for expansion now
    w_pot = cycle_max + 1
    h_pot = cycle_max + 1
    d_pot = cycle_max + 1

    padding = {}
    padding = {
        (x, y, z): '.'
        for z in range(-d_pot, d_pot + d)
        for y in range(-h_pot, h_pot + h)
        for x in range(-w_pot, w_pot + w)
    }

    # print("pretty print padding")
    # pretty_print_grid(padding)

    # expand the grid enough to handle bleed up front to avoid dynamic growing
    grid = padding | grid

    while cycle < cycle_max:
        # pretty_print_grid(grid)
        for locus in grid:
            cube = grid.get(locus)
            next_locus, next_cube = get_cube(grid, locus, cube, shifts)
            next_grid[next_locus] = next_cube
        if next_grid == grid:
            break
        grid = next_grid.copy()
        cycle = cycle + 1

    pretty_print_grid(grid)
    num_active = sum(val == '#' for val in grid.values())
    print('part1: left in active state', num_active)

# If a cube is active and exactly 2 or 3 of its neighbors are also active, the cube remains active. Otherwise, the cube becomes inactive.
# If a cube is inactive but exactly 3 of its neighbors are active, the cube becomes active. Otherwise, the cube remains inactive.


def part2(grid, shifts):
    next_grid = {}
    cycle = 0
    cycle_max = 6

    w = (max(grid, key=operator.itemgetter(0)))[0] + 1
    h = (max(grid, key=operator.itemgetter(1)))[1] + 1
    d = (max(grid, key=operator.itemgetter(2)))[2] + 1
    t = (max(grid, key=operator.itemgetter(3)))[3] + 1

    # just make the grid big enough for expansion now
    w_pot = cycle_max + 1
    h_pot = cycle_max + 1
    d_pot = cycle_max + 1
    t_pot = cycle_max + 1
    print("pots", w_pot, h_pot, d_pot, t_pot)

    padding = {}
    padding = {
        (x, y, z, ww): '.'
        for z in range(-d_pot, d_pot + d)
        for y in range(-h_pot, h_pot + h)
        for x in range(-w_pot, w_pot + w)
        for ww in range(-t_pot, t_pot + t)
    }

    # print("pretty print padding")
    # pretty_print_grid(padding)

    # expand the grid enough to handle bleed up front to avoid dynamic growing
    grid = padding | grid

    while cycle < cycle_max:
        # pretty_print_grid(grid)
        for locus in grid:
            cube = grid.get(locus)
            next_locus, next_cube = get_cube(grid, locus, cube, shifts)
            next_grid[next_locus] = next_cube
        if next_grid == grid:
            break
        grid = next_grid.copy()
        cycle = cycle + 1

    # pretty_print_grid(grid)
    num_active = sum(val == '#' for val in grid.values())
    print('part2: left in active state', num_active)


def solve(inp, inp4):

    values = [0, 1, -1]
    # part 1
    # for a cube, its neighbords in 3d space = 3^3 - 1 = 27 - 1 = 26
    shifts = list(itertools.product(values, repeat=3))
    shifts.remove((0, 0, 0))
    grid = grid3dict(inp)
    part1(grid, shifts)

    # part 2
    grid4 = grid4dict(inp4)
    shifts4 = list(itertools.product(values, repeat=4))
    shifts4.remove((0, 0, 0, 0))
    part2(grid4, shifts4)


if __name__ == '__main__':
    # part1
    print(solve(fileinput.input(), fileinput.input()))

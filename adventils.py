#!/usr/bin/env python

def stacked2list(inp, type=int):
    return list(type(line) for line in inp)


def strip_newlines(inp):
    return [r.strip() for r in inp]


def grid2dict(inp, type=str):
    grid = {
        (x, y): v
        for y, row in enumerate(inp)
        for x, v in enumerate(row.strip())
    }
    return grid


def blanks2list(inp, type=str):
    return ''.join(list(str(line) for line in inp)).split('\n\n')

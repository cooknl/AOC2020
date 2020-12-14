from aocd import data, submit
from aocd_setup import get_test_data, get_test_answer
import numpy as np
from itertools import product

def test_convert_charnum():
    assert convert_charnum('L') == 0
    assert convert_charnum('#') == 1
    assert convert_charnum('.') == -1
    assert convert_charnum(0)  == 'L'
    assert convert_charnum(1)  == '#'
    assert convert_charnum(-1) == '.'
    assert convert_charnum('') == None

def test_answer():
    assert answer(
                    input_data=get_test_data(part='a', fname=__file__)
    )['a'] == get_test_answer(part='a', fname=__file__)
    assert answer(
                    input_data=get_test_data(part='a', fname=__file__)
    )['b'] == get_test_answer(part='b', fname=__file__)
    assert answer(data)['a'] == 2438
    assert answer(data)['b'] == 2174

def convert_charnum(element):
    if element == 'L': return 0
    if element == '#': return 1
    if element == '.': return -1
    if element == 0: return 'L'
    if element == 1: return '#'
    if element == -1: return '.'
    return None

def gen_grid(txt):
    return np.pad(
                  np.array(
                      [ 
                          [convert_charnum(e) for e in l] 
                          for l in txt.split('\n') 
                          if l
                      ]
                  ), 1, constant_values = (-1,)
           )

def get_neighborhood_a(grid,row,col):
    hood = grid[row-1:row+2, col-1:col+2].reshape(1,-1)
    adjacents = np.concatenate((hood[0,:4],hood[0,5:]))
    return {'seat': grid[row,col], 
            'adj': np.where(adjacents >= 0, adjacents, 0).sum()}

def get_neighborhood_b(grid,row,col):
    directions = list(product((-1,0,1), repeat=2))
    rows, cols = grid.shape
    directions.remove((0,0))
    adjacents = []
    for dir in directions:
        r = row
        c = col
        while (0 < r < rows-1) and (0 < c < cols-1):
            r += dir[0]
            c += dir[1]
            if grid[r,c] >= 0:
                adjacents.append(grid[r,c])
                break
    return {'seat': grid[row,col], 
            'adj': sum(adjacents)}


def answer(input_data=data):
    grid = gen_grid(input_data)
    rows, cols = grid.shape
    last_grid = grid.copy()
    next_grid = last_grid.copy()
    while True:
        for row in range(1,rows-1):
            for col in range(1, cols-1):
                if last_grid[row, col] >= 0:
                    hood = get_neighborhood_a(last_grid,row,col)
                    if (hood['seat'] == 1) and (hood['adj'] >= 4):
                        next_grid[row,col] = 0
                    elif (hood['seat'] == 0) and (hood['adj'] == 0):
                        next_grid[row,col] = 1
        if np.array_equal(last_grid,next_grid):
            answer_a = np.where(last_grid >= 0, last_grid, 0).sum()
            break
        last_grid = next_grid.copy()
    last_grid = grid.copy()
    next_grid = last_grid.copy()
    while True:
        for row in range(1,rows-1):
            for col in range(1, cols-1):
                if last_grid[row, col] >= 0:
                    hood = get_neighborhood_b(last_grid,row,col)
                    if (hood['seat'] == 1) and (hood['adj'] >= 5):
                        next_grid[row,col] = 0
                    elif (hood['seat'] == 0) and (hood['adj'] == 0):
                        next_grid[row,col] = 1
        if np.array_equal(last_grid,next_grid):
            answer_b = np.where(last_grid >= 0, last_grid, 0).sum()
            break
        last_grid = next_grid.copy()
    return {'a': answer_a, 'b': answer_b}


submit(answer(data)['a'], part='a')
submit(answer(data)['b'], part='b')
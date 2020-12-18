from aocd import data, submit

# https://adventofcode.com/2020/day/17

# active (#) or inactive (.)

#-----------TEST CODE

def test_gen_search_ranges():
    assert gen_search_ranges(
        {(0,1,0,0): 1, (1,2,0,0): 1, (2,0,0,0): 1, (2,1,0,0): 1, (2,2,0,0): 1},
        dims=3
    ) == [(-1, 4), (-1, 4), (-1, 2), (0, 1)]
    assert gen_search_ranges(
        {
        (0,0,-1,0): 1, (1,2,-1,0): 1, (2,1,-1,0): 1,
        (0,0,0,0): 1, (0,2,0,0): 1, (1,1,0,0): 1, (1,2,0,0): 1, (2,1,0,0): 1,
        (0,0,1,0): 1, (1,2,1,0): 1, (2,1,1,0): 1
    }, dims=3 ) == [(-1, 4), (-1, 4), (-2, 3), (0, 1)]

def test_apply_rules():
    assert apply_rules(
        {(0,1,0,0): 1, (1,2,0,0): 1, (2,0,0,0): 1, (2,1,0,0): 1, (2,2,0,0): 1},
        3
    ) == {
        (1,0,-1,0): 1, (2,2,-1,0): 1, (3,1,-1,0): 1,
        (1,0,0,0): 1, (1,2,0,0): 1, (2,1,0,0): 1, (2,2,0,0): 1, (3,1,0,0): 1,
        (1,0,1,0): 1, (2,2,1,0): 1, (3,1,1,0): 1
    }

def test_gen_neighbors():
    assert len(gen_neighbors((0,0,0,0), dims=3)) == 26

def test_answer():
    test_data_a = '''.#.
..#
###
'''
    assert answer(test_data_a, cycles=6, dims=3) == 112
    assert answer(data, cycles=6, dims=3) == 359
    assert answer(test_data_a, cycles=6, dims=4) == 848
    assert answer(data, cycles=6, dims=4) == 2228

#-------------BIZNESS LOGIK

def apply_rules(state, dims):
    search_ranges = gen_search_ranges(state, dims)
    search_grid = []
    for i in range(*search_ranges[0]):
        for j in range(*search_ranges[1]):
            for k in range(*search_ranges[2]):
                for l in range(*search_ranges[3]):
                    search_grid.append((i,j,k,l))
    next_state = {}
    for coord in search_grid:
        neighbors = gen_neighbors(coord, dims)
        active_sum = sum([1 for n in neighbors if n in state])
        if (
            (coord in state) and (active_sum in [2,3]) 
           ) or (
            (coord not in state) and (active_sum == 3)
           ):
            next_state[coord] = 1
        # Only active states are passed to the next_state, states go inactive (not recorded) by default
    return next_state

def gen_neighbors(coords, dims):
    x, y, z, w = coords
    neighbors = []
    for i in range(x-1, x+2):
        for j in range(y-1, y+2):
            for k in range(z-1, z+2):
                if dims ==3:
                    l = 0
                    if ((i,j,k,l) != (x,y,z,w)):
                        neighbors.append((i,j,k,l))
                else:
                    for l in range(w-1, w+2):
                        if ((i,j,k,l) != (x,y,z,w)):
                            neighbors.append((i,j,k,l))
    return neighbors

def gen_search_ranges(state,dims):
    coords = state.keys()
    search_ranges = []
    for _ in range(4):
        search_ranges.append((0,1))
    for c in coords:
        for n, d in enumerate(c):
            search_ranges[n] = ( min(search_ranges[n][0], d-1),
                                 max(search_ranges[n][1], d+2) )
    if dims == 3:
        search_ranges[3] = (0,1)
    return search_ranges

def gen_input(input_data):
    state = {}
    for i, line in enumerate(input_data.split('\n')):
        for j, cell in enumerate(line):
            if cell == "#":
                state[(i,j,0,0)] = 1 # Only keeping active cells, inactive are not kept and assumed to exist as 0
    return state

def answer(input_data, cycles, dims):
    state = gen_input(input_data)
    for _ in range(cycles):
        state = apply_rules(state, dims)
    return len(state)

if __name__ == "__main__":
    submit(answer(data, cycles=6, dims=3), part='a')
    submit(answer(data, cycles=6, dims=4), part='b')

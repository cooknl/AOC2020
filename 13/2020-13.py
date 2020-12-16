from aocd import data, submit
from aocd_setup import get_test_data, get_test_answer
from math import prod

def test_solve_for_t():
    inp = [(0,17),(2,13),(3,19)]; ans = 3417; 
    assert solve_for_t(inp) == ans

    inp = [(0,67),(1,7),(2,59),(3,61)]; ans = 754018; 
    assert solve_for_t(inp) == ans
    
    inp = [(0,67),(2,7),(3,59),(4,61)]; ans = 779210; 
    assert solve_for_t(inp) == ans
    assert solve_for_t([(0,67),(2,7),(3,59),(4,61)]) == 779210
    assert solve_for_t([(0,67),(1,7),(3,59),(4,61)]) == 1261476
    assert solve_for_t([(0,1789),(1,37),(2,47),(3,1889)]) == 1202161486

def test_answer():
    assert answer(
                    input_data=get_test_data(part='a', fname=__file__)
    )['a'] == get_test_answer(part='a', fname=__file__)
    assert answer(data)['a'] == 161

    assert answer(
                    input_data=get_test_data(part='a', fname=__file__)
    )['b'] == get_test_answer(part='b', fname=__file__)
    assert answer(data)['b'] == 213890632230818

def generate_input(input_data):
    first_split = input_data.split('\n')
    time = int(first_split[0])
    bus_ids = first_split[1].split(',')
    return {'time':time, 'bus_ids':bus_ids}

# https://joepitts.co.uk/blog/advent-of-code-day-13.html  

def solve_for_t(buses):
    # NAIVE approach which takes forever, even accounting for different counters
    # count_setup = [abs(b[0] - b[1]) for b in buses]
    # counters = []
    # for c in count_setup:
    #     temp_count = count_setup.copy()
    #     temp_count.remove(c)
    #     counters.append(prod(temp_count)//c)
    # bus_sets = [set() for b in buses]
    # while not set.intersection(*bus_sets):
    #     for i in range(len(bus_sets)):
    #         bus_sets[i].add(counters[i] * buses[i][1] - buses[i][0])
    #     counters = [x + 1 for x in counters]
    # ans = set.intersection(*bus_sets).pop()
    jump = buses[0][1] # first bus id is the first jump size
    time_stamp = 0 # start at t=0
    for i, bus_id in buses[1:]: # for remaining buses
        while (time_stamp + i) % bus_id != 0: # increase the time_stamp by jump until time_stamp plus the index is a multiple of the next bus_id
            time_stamp += jump
        jump *= bus_id # now multiply by bus_id, since correct time_stamp will be multiple of each bus_id, corrected for index
    return time_stamp

def answer(input_data=data):
    input = generate_input(input_data)
    buses_a = [int(b) for b in input['bus_ids'] if b not in 'x']
    answer_a = prod(min([(b, b - input['time']%b) for b in buses_a], key = lambda t: t[1]))

    buses_b = [(i, int(b)) for i, b in enumerate(input['bus_ids']) if b not in 'x']
    answer_b = solve_for_t(buses_b)
    return {'a':answer_a, 'b':answer_b}

# submit(answer(data)['a'], part='a')
submit(answer(data)['b'], part='b')
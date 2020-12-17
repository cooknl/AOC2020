from aocd import data, submit

# https://adventofcode.com/2020/day/17

print(data)

def test_answer():
    test_data_a = '''.#.
..#
###
'''
    assert answer(test_data_a, cycles=6) == 112

def answer(input_data, cycles):
    return 0

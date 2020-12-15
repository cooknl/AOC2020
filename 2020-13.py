from aocd import data, submit
from aocd_setup import get_test_data, get_test_answer
from math import prod

def test_answer():
    assert answer(
                    input_data=get_test_data(part='a', fname=__file__)
    )['a'] == get_test_answer(part='a', fname=__file__)
    assert answer(data)['a'] == 161

    # assert answer(
    #                 input_data=get_test_data(part='a', fname=__file__)
    # )['b'] == get_test_answer(part='b', fname=__file__)
    # assert answer(data)['b'] == 28885

def generate_input(input_data):
    first_split = input_data.split('\n')
    time = int(first_split[0])
    buses = [int(b) for b in first_split[1].split(',') if b not in 'x']
    return {'time':time, 'buses':buses}

def answer(input_data=data):
    input = generate_input(input_data)
    answer_a = prod(min([(b, b - input['time']%b) for b in input['buses']], key = lambda t: t[1]))
    return {'a':answer_a, 'b':0}

# submit(answer(data)['a'], part='a')
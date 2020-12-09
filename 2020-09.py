from aocd import data, submit
from itertools import combinations

from aocd_setup import get_test_data, get_test_answer

def test_a():
    assert answer_a(
                    input_data=get_test_data(part='a', fname=__file__),
                    preamble=5
    ) == get_test_answer(part='a', fname=__file__)

def test_actual_a():
    assert answer_a(data, 25) == 88311122

def generate_data_iterator(data_string):
    return tuple(int(d) for d in data_string.split('\n'))

def answer_a(input_data=data, preamble=5):
    data_iter = generate_data_iterator(input_data)
    for line, d in enumerate(data_iter[preamble:]):
        if d not in [
                        sum(c) for c in 
                            combinations(data_iter[line:(line + preamble)],2)
                    ]:
            return d
    return 0

submit(answer_a(data, 25), part='a')
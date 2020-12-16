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

def test_b():
    assert answer_b(
                    input_data=get_test_data(part='a', fname=__file__),
                    preamble=5
    ) == get_test_answer(part='b', fname=__file__)

def test_actual_b():
    assert answer_b(data, 25) == 13549369

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

def answer_b(input_data=data, preamble=5):
    ans_a = answer_a(input_data, preamble)
    data_iter = generate_data_iterator(input_data)
    for line in range(len(data_iter[preamble:])):
        for start, end in combinations(range(0,preamble),2):
            seq = data_iter[line + start: line + end]
            if ans_a == sum(seq):
                return min(seq) + max(seq)
    return 0

# submit(answer_a(data, 25), part='a')
# submit(answer_b(data, 25), part='b')
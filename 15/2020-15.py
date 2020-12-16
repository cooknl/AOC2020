from aocd import data, submit
from aocd_setup import get_test_data, get_test_answer
import numpy as np

# https://adventofcode.com/2020/day/15

# def test_answer_a():
#     # assert answer_a('0,3,6', 2020) == 436
#     # assert answer_a('1,3,2', 2020) == 1
#     # assert answer_a('2,1,3', 2020) == 10
#     # assert answer_a('1,2,3', 2020) == 27
#     # assert answer_a('2,3,1', 2020) == 78
#     # assert answer_a('3,2,1', 2020) == 438
#     # assert answer_a('3,1,2', 2020) == 1836
#     assert answer_a(data, 2020) == 475

# def test_answer_b():
    # assert answer_b(data, 2020) == 475
    # assert answer_b('0,3,6', 30000000) == 175594
    # assert answer_b('1,3,2', 30000000) == 2578
    # assert answer_b('2,1,3', 30000000) == 3544142
    # assert answer_b('1,2,3', 30000000) == 261214
    # assert answer_b('2,3,1', 30000000) == 6895259
    # assert answer_b('3,2,1', 30000000) == 18
    # assert answer_b('3,1,2', 30000000) == 362
    # assert answer_b(data, 30000000) == 0


# https://numpy.org/doc/stable/reference/generated/numpy.fromstring.html

def generate_input_a(input_data):
    return np.fromstring(input_data, dtype=int, sep=',')

def answer_a(input_data, epoch):
    inputs = generate_input_a(input_data)
    sequence = np.zeros(epoch, dtype=int)
    sequence[:len(inputs)] = inputs
    for i in range(len(inputs), epoch):
        idxs = np.where(sequence[:i-1] == sequence[i-1])[0]
        if idxs.size:
            sequence[i] = i - idxs[-1] - 1
        else:
            sequence[i] = 0
    return sequence[-1]

def generate_input_b(input_data):
    split_chars = input_data.split(',')
    zero_filter = list(filter(lambda x: x[1] == '0', enumerate(input_data.split(','))))
    if zero_filter:
        last_zero = max(zero_filter, key = lambda z: z[0])[0]
    else:
        last_zero = None
    return (len(split_chars), {k: int(v) for k, v in enumerate(input_data.split(',')) if v != '0'},last_zero)

def answer_b(input_data, epoch):
    ans = 0
    length, sparse_sequence, zero = generate_input_b(input_data)
    zero_index = (zero, None)
    for i in range(length,epoch):
        if (i-1) in sparse_sequence.keys(): # The previous value was non-zero
            matches = dict(filter(lambda elem: elem[1] == sparse_sequence[i-1], 
                                  sparse_sequence.items()))
            if len(matches) == 1: # If it only exists once in the sparse seq, then update zero_index
                zero_index = (i, zero_index[0])
            else:
                sorted_keys = sorted(list(matches.keys()))
                sparse_sequence[i] = sorted_keys[-1] - sorted_keys[-2]
                sparse_sequence.pop(sorted_keys[-2])
        else: # The previous value was zero, so take the difference in zero_index as new value
            sparse_sequence[i] = zero_index[0] - zero_index[1]
    if max(sparse_sequence.keys()) == epoch-1: # If the final value is non-zero return it
        ans = sparse_sequence[epoch-1]
    return ans

# submit(answer_a(data,2020),part='a')
submit(answer_b(data,30000000),part='b')
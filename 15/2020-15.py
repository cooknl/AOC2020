from aocd import data, submit
import numpy as np
import timeit

# https://adventofcode.com/2020/day/15

def test_answer_a():
    assert answer_a('0,3,6', 2020) == 436
#     # assert answer_a('1,3,2', 2020) == 1
#     # assert answer_a('2,1,3', 2020) == 10
#     # assert answer_a('1,2,3', 2020) == 27
#     # assert answer_a('2,3,1', 2020) == 78
#     # assert answer_a('3,2,1', 2020) == 438
#     # assert answer_a('3,1,2', 2020) == 1836
#     assert answer_a(data, 2020) == 475

def test_answer_b():
    assert answer_b('0,3,6', 2020) == 436
    # assert answer_b(data, 2020) == 475
    # assert answer_b('0,3,6', 30000000) == 175594
    # assert answer_b('1,3,2', 30000000) == 2578
    # assert answer_b('2,1,3', 30000000) == 3544142
    # assert answer_b('1,2,3', 30000000) == 261214
    # assert answer_b('2,3,1', 30000000) == 6895259
    # assert answer_b('3,2,1', 30000000) == 18
    # assert answer_b('3,1,2', 30000000) == 362
    # assert answer_b(data, 30000000) == 11261


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
    # Try keeping the VALUES as keys and the indices as values, including 0
    num_dict = {}
    for i, n in enumerate(input_data.split(',')):
        if int(n) in num_dict.keys():
            num_dict[int(n)] = (num_dict[int(n)][1], i)
        else:
            num_dict[int(n)] = (None, i)
        length = i
        prev_num = int(n)
    return num_dict, length, prev_num

def answer_b(input_data, epoch):
    num_d, length, prev_num = generate_input_b(input_data)
    for i in range(length+1,epoch):
        # If there's a None in the previous number's index tuple, then it was
        # the first instance and the index for the ZERO will be updated with
        # the current index
        if None in num_d[prev_num]:  
            prev_num = 0
            num_d[prev_num] = (num_d[prev_num][1], i)
        # If not a None, then it's got 2 indices to subtract to calculate the turns
        else:
            turns = num_d[prev_num][1] - num_d[prev_num][0]
            if turns in num_d:
                num_d[turns] = (num_d[turns][1], i)
            else:
                num_d[turns] = (None, i)
            prev_num = turns
    return prev_num

if __name__ == '__main__':
    # submit(answer_a(data,2020),part='a')
    # submit(answer_b(data,30000000),part='b')

    timer_number = 100
    print("Numpy")
    numpy_time = timeit.timeit('answer_a("6,4,12,1,20,0,16",2020)', 
                        setup='from __main__ import answer_a',
                        number=timer_number)
    print("Avg seconds:" + f"{(numpy_time/timer_number)*1000:0.1f} ms")
    print("---")
    print("Dictionary")
    dict_time = timeit.timeit('answer_b("6,4,12,1,20,0,16",2020)', 
                        setup='from __main__ import answer_b',
                        number=timer_number)
    print("Avg seconds:" + f"{(dict_time/timer_number)*1000:0.1f} ms")
    print("---")
    print("Speed multiple:" + f"{(abs(numpy_time - dict_time)/min(numpy_time,dict_time)):0.1f}")

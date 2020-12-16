from aocd import data, submit
from aocd_setup import get_test_data, get_test_answer
import math
from functools import lru_cache

def test_calc_series():
    assert calc_series(0) == 1
    assert calc_series(1) == 1
    assert calc_series(2) == 2
    assert calc_series(3) == 4
    assert calc_series(4) == 7
    assert calc_series(5) == 13

def test_answer():
    assert answer(
                    input_data=get_test_data(part='a1', fname=__file__)
    )['a'] == get_test_answer(part='a1', fname=__file__)
    assert answer(
                    input_data=get_test_data(part='a2', fname=__file__)
    )['a'] == get_test_answer(part='a2', fname=__file__)
    assert answer(
                    input_data=get_test_data(part='a1', fname=__file__)
    )['b'] == get_test_answer(part='b1', fname=__file__)
    assert answer(
                    input_data=get_test_data(part='a2', fname=__file__)
    )['b'] == get_test_answer(part='b2', fname=__file__)
    assert answer(data)['a'] == 2201
    assert answer(data)['b'] == 169255295254528

def generate_data_iterator(data_string):
    return list(int(d) for d in data_string.split('\n'))

@lru_cache
def calc_series(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return calc_series(n-1) + calc_series(n-2) + calc_series(n-3)

def answer(input_data=data):
    data_iter = sorted(generate_data_iterator(input_data))
    data_extended = [0] + data_iter + [data_iter[-1] + 3]
    diff = [j - i for i, j in zip(sorted(data_extended)[: -1], 
                                  sorted(data_extended)[1 :])]
    print(diff)
    one_runs = []
    temp_count = 0
    for el in diff:
        if el == 1:
            temp_count += 1
        elif temp_count >= 2:
            one_runs.append(calc_series(temp_count))
            temp_count = 0
        else:
            temp_count = 0
    return {'a': diff.count(1) * diff.count(3), 'b': math.prod(one_runs)}

'''

n_i = n_{i-1} + n_{i-2} + n_{i-3}

4: 7
0,1,2,3,4,7: 1,1,1,1,3
0,2,3,4,7: 2,1,1,3
0,1,3,4,7: 1,2,1,3
0,1,2,4,7: 1,1,2,3
0,3,4,7: 3,1,3
0,1,4,7: 1,3,3
0,2,4,7: 2,2,3


3: 4
0,1,2,3,6: 1,1,1,3
0,2,3,6: 2,1,3
0,1,3,6: 1,2,3
0,3,6: 3,3

2: 2
0,1,2,5: 1,1,3
0,2,5: 2,3

1: 1
0,1,4: 1,3

0: 1
0,3: 0,3
'''

submit(answer(data)['a'], part='a')
submit(answer(data)['b'], part='b')
from aocd import data, submit
from aocd_setup import get_test_data, get_test_answer
from math import radians as rad
from math import sin, cos

def test_update_ship_state():
    assert update_ship_state({'heading':0, '+N-S':0, '+E-W':0}, ('R',90)) == {'heading':90, '+N-S':0, '+E-W':0}
    assert update_ship_state({'heading':0, '+N-S':0, '+E-W':0}, ('L',90)) == {'heading':270, '+N-S':0, '+E-W':0}
    assert update_ship_state({'heading':0, '+N-S':0, '+E-W':0}, ('F',5)) == {'heading':0, '+N-S':5, '+E-W':0}
    assert update_ship_state({'heading':90, '+N-S':0, '+E-W':0}, ('F',5)) == {'heading':90, '+N-S':0, '+E-W':5}
    assert update_ship_state({'heading':180, '+N-S':0, '+E-W':0}, ('F',5)) == {'heading':180, '+N-S':-5, '+E-W':0}
    assert update_ship_state({'heading':270, '+N-S':0, '+E-W':0}, ('F',5)) == {'heading':270, '+N-S':0, '+E-W':-5}
    assert update_ship_state({'heading':0, '+N-S':0, '+E-W':0}, ('N',5)) == {'heading':0, '+N-S':5, '+E-W':0}
    assert update_ship_state({'heading':0, '+N-S':0, '+E-W':0}, ('S',5)) == {'heading':0, '+N-S':-5, '+E-W':0}
    assert update_ship_state({'heading':0, '+N-S':0, '+E-W':0}, ('E',5)) == {'heading':0, '+N-S':0, '+E-W':5}
    assert update_ship_state({'heading':0, '+N-S':0, '+E-W':0}, ('W',5)) == {'heading':0, '+N-S':0, '+E-W':-5}

def test_update_ship_wpt_state():
    assert update_ship_wpt_state(
        {'heading':0, '+N-S':0, '+E-W':0}, {'+N-S':4, '+E-W':10}, ('R',90)
    ) == (
        {'heading':0, '+N-S':0, '+E-W':0}, {'+N-S':-10, '+E-W':4}
    )
    assert update_ship_wpt_state(
        {'heading':0, '+N-S':0, '+E-W':0}, {'+N-S':4, '+E-W':10}, ('L',90)
    ) == (
        {'heading':0, '+N-S':0, '+E-W':0}, {'+N-S':10, '+E-W':-4}
    )
    assert update_ship_wpt_state(
        {'heading':0, '+N-S':0, '+E-W':0}, {'+N-S':1, '+E-W':10}, ('F',10)
    ) == (
        {'heading':0, '+N-S':10, '+E-W':100}, {'+N-S':1, '+E-W':10}
    )
    assert update_ship_wpt_state(
        {'heading':0, '+N-S':10, '+E-W':100}, {'+N-S':1, '+E-W':10}, ('N',3)
    ) == (
        {'heading':0, '+N-S':10, '+E-W':100}, {'+N-S':4, '+E-W':10}
    )

def test_answer():
    assert answer(
                    input_data=get_test_data(part='a', fname=__file__)
    )['a'] == get_test_answer(part='a', fname=__file__)
    assert answer(data)['a'] == 882

    assert answer(
                    input_data=get_test_data(part='a', fname=__file__)
    )['b'] == get_test_answer(part='b', fname=__file__)
    assert answer(data)['b'] == 28885

def generate_input(input_data):
    inputs = [ ( i[0], int(i[1:]) ) for i in input_data.split('\n') if i]
    return inputs

def update_ship_state(state, instruction):
    if instruction[0] in {'R','L'}:
        if instruction[0] == 'R':
            state['heading'] += +1 * instruction[1]
        else:
            state['heading'] += -1 * instruction[1]
        state['heading'] %= 360
    if instruction[0] == 'F':
        state['+N-S'] += int(cos(rad(state['heading'])) * instruction[1])
        state['+E-W'] += int(sin(rad(state['heading'])) * instruction[1])
    if instruction[0] in {'N','E','S','W'}:
        if instruction[0] == 'N':
            state['+N-S'] += +1 * instruction[1]
        elif instruction[0] == 'S':
            state['+N-S'] += -1 * instruction[1]
        elif instruction[0] == 'E':
            state['+E-W'] += +1 * instruction[1]
        elif instruction[0] == 'W':
            state['+E-W'] += -1 * instruction[1]
    return state

def update_ship_wpt_state(ship_state, wpt_state, instruction):
    if instruction[0] in {'R','L'}:
        ew = wpt_state['+E-W']
        ns = wpt_state['+N-S']
        if instruction[0] == 'R':
            wpt_state['+E-W'] =   int(cos(rad(instruction[1])) * ew) + int(sin(rad(instruction[1])) * ns)
            wpt_state['+N-S'] = - int(sin(rad(instruction[1])) * ew) + int(cos(rad(instruction[1])) * ns)
        else:
            wpt_state['+E-W'] = int(cos(rad(instruction[1])) * ew) - int(sin(rad(instruction[1])) * ns)
            wpt_state['+N-S'] = int(sin(rad(instruction[1])) * ew) + int(cos(rad(instruction[1])) * ns)
    ship_state['heading'] %= 360
    if instruction[0] == 'F':
        ship_state['+N-S'] += wpt_state['+N-S'] * instruction[1]
        ship_state['+E-W'] += wpt_state['+E-W'] * instruction[1]
    if instruction[0] in {'N','E','S','W'}:
        if instruction[0] == 'N':
            wpt_state['+N-S'] += +1 * instruction[1]
        elif instruction[0] == 'S':
            wpt_state['+N-S'] += -1 * instruction[1]
        elif instruction[0] == 'E':
            wpt_state['+E-W'] += +1 * instruction[1]
        elif instruction[0] == 'W':
            wpt_state['+E-W'] += -1 * instruction[1]
    return (ship_state, wpt_state)

def answer(input_data=data):
    inputs = generate_input(input_data)
    ship_state = {'heading': 90,
             '+N-S': 0,
             '+E-W': 0}
    for instruction in inputs:
        update_ship_state(ship_state, instruction)
    answer_a = abs(ship_state['+N-S']) + abs(ship_state['+E-W'])
    ship_state = {'heading': 90,
             '+N-S': 0,
             '+E-W': 0}
    wpt_state = {'+N-S': 1,
                 '+E-W': 10}
    for instruction in inputs:
        update_ship_wpt_state(ship_state, wpt_state, instruction)
    answer_b = abs(ship_state['+N-S']) + abs(ship_state['+E-W'])
    return {'a': answer_a, 'b': answer_b}

# submit(answer(data)['a'], part='a')
# submit(answer(data)['b'], part='b')
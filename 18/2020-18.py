from aocd import data, submit
import sys
from numbers import Integral

# https://adventofcode.com/2020/day/18

def test_operate():
    assert operate(2,3,'*') == 6
    assert operate(2,3,'+') == 5

def test_answer():
    assert answer('1 + 2 * 3 + 4 * 5 + 6')['a'] == 71
    assert answer('1 + (2 * 3) + (4 * (5 + 6))')['a'] == 51
    assert answer('2 * 3 + (4 * 5)')['a'] == 26
    assert answer('5 + (8 * 3 + 9 + 3 * 4 * 3)')['a'] == 437
    assert answer('5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))')['a'] == 12240
    assert answer('((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2')['a'] == 13632
    assert answer(data)['a'] == 12918250417632

    assert answer('1 + 2 * 3 + 4 * 5 + 6')['b'] == 231
    assert answer('1 + (2 * 3) + (4 * (5 + 6))')['b'] == 51
    assert answer('2 * 3 + (4 * 5)')['b'] == 46
    assert answer('5 + (8 * 3 + 9 + 3 * 4 * 3)')['b'] == 1445
    assert answer('5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))')['b'] == 669060
    assert answer('((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2')['b'] == 23340
    assert answer(data)['b'] == 171259538712010

def operate(a, b, op):
    if op == '*':
        return a*b
    if op == '+':
        return a+b
    return None

def parse_line(line):
    tokens = [int(c) if c in '0123456789' else c for c in line if c != ' ']
    return tokens

def token_math_a(tokens, pointer=0):
    # Need to keep track of where in the tokens we are, can't do it with just enumerate
    # # print(tokens)
    num_stack = []
    op_stack = []
    for _ in range(len(tokens)):
        if pointer >= len(tokens):
            return (num_stack[0], pointer)
        t = tokens[pointer]
        # # print("ptr:",pointer,"token:",tokens[pointer])
        if t == '(':
            pointer += 1
            # # print("branching with ", tokens[pointer:])
            return_val, pointer = token_math_a(tokens, pointer)
            num_stack.append(return_val)
        if t == ')':
            pointer += 1
            # # print("returning with ", num_stack)
            return num_stack[0], pointer

        if isinstance(t, Integral):
            # # print("it's a number, so append the num_stack with", str(t))
            num_stack.append(t)
            pointer += 1
        elif t in '+*':
            # # print("it's an operation, so append the op_stack with ", t)
            op_stack.append(t)
            pointer += 1

        if (len(num_stack) >= 2) and (len(op_stack) >= 1):
            # # print("time to do an operation with ", num_stack[-2:], "and", op_stack[-1])
            num_stack.append(operate(num_stack.pop(), num_stack.pop(), op_stack.pop()))
        # # print("num:",num_stack, "op:", op_stack)
    return (num_stack[0], pointer)

def token_math_b(tokens, pointer=0):
    # Need to keep track of where in the tokens we are, can't do it with just enumerate
    # print(tokens)
    op_stack = []
    num_stack = []
    for _ in range(len(tokens)):
        if pointer >= len(tokens):
            # return (num_stack[0], pointer)
            continue
        t = tokens[pointer]
        # print("ptr:",pointer,"token:",tokens[pointer])
        if t == '(':
            pointer += 1
            # print("branching with ", tokens[pointer:])
            return_val, pointer = token_math_b(tokens, pointer)
            num_stack.append(return_val)
        if t == ')':
            pointer += 1
            # print("now we should just have multiplications remaining")
            for _ in range(len(op_stack)):
                num_stack.append(operate(num_stack.pop(), num_stack.pop(), op_stack.pop()))
                # print("num:",num_stack, "op:", op_stack)
            # print("returning with ", num_stack)
            return num_stack[0], pointer

        if isinstance(t, Integral):
            # print("it's a number, so append the num_stack with", str(t))
            num_stack.append(t)
            pointer += 1
        elif t in '+*':
            # print("it's an operation, so append the num_stack with", t)
            op_stack.append(t)
            pointer += 1
            # print("now continue to avoid performing the operation, allowing for a lookahead")
            continue

        if (len(num_stack) >= 2) and (len(op_stack) >= 1) and (op_stack[-1] == '+'):
            # print("time to do an operation with ", num_stack[-2:], "and", op_stack[-1])
            num_stack.append(operate(num_stack.pop(), num_stack.pop(), op_stack.pop()))
        # print("num:",num_stack, "op:", op_stack)
    # print("now we should just have multiplications remaining")
    for _ in range(len(op_stack)):
        num_stack.append(operate(num_stack.pop(), num_stack.pop(), op_stack.pop()))
        # print("num:",num_stack, "op:", op_stack)
    return (num_stack[0], pointer)

def get_input(input_data):
    return input_data.split('\n')

def answer(input_data):
    lines = get_input(input_data)
    line_answers = {'a':[], 'b':[]}
    for line in lines:
        tokens = parse_line(line)
        line_answers['a'].append(token_math_a(tokens)[0])
        line_answers['b'].append(token_math_b(tokens)[0])
    return {'a': sum(line_answers['a']), 'b': sum(line_answers['b'])}

if __name__ == '__main__':
    try:
        part = sys.argv[1]
        submit(answer(data)[part], part=part)
    except IndexError:
        raise SystemExit("Usage: Include part as an command line argument\n Examples:\n'python 2020-dd.py a'\n'python 2020-dd.py b'")
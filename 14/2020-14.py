from aocd import data, submit
from aocd_setup import get_test_data, get_test_answer
import re
from itertools import product

# https://adventofcode.com/2020/day/14

# def test_apply_value_mask():
#     mask = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X'
#     assert apply_value_mask(mask, 11) == 73
#     assert apply_value_mask(mask, 101) == 101
#     assert apply_value_mask(mask, 0) == 64

def test_apply_address_mask():
    assert apply_address_mask('000000000000000000000000000000X1001X',42) == [26, 27, 58, 59]
    assert apply_address_mask('00000000000000000000000000000000X0XX',26) == [16, 17, 18, 19, 24, 25, 26, 27]


def test_answer():
    assert answer_a(
                    input_data=get_test_data(part='a', fname=__file__)
    ) == get_test_answer(part='a', fname=__file__)
    assert answer_a(data) == 15514035145260    

    assert answer_b(
                    input_data=get_test_data(part='b', fname=__file__)
    ) == get_test_answer(part='b', fname=__file__)
    assert answer_b(data) == 3926790061594

# https://docs.python.org/3.6/library/stdtypes.html#str.split
# https://docs.python.org/3/library/re.html#re.findall

def generate_input(input_data):
    mask_mem_list = []
    mask_list = input_data.split('mask = ')[1:]
    for each_mask in mask_list:
        mask, mem_str = each_mask.split('\n', maxsplit=1)
        # create tuples with digit place, i, and value to be masked, v, ignoring 'X'
        # reversed to preserve "Endian-ness"
        mems = [(int(i), int(v)) for s in mem_str.split('\n') for i, v in re.findall(r'mem\[(\d+)\] = (\d+)', s)]
        mask_mem_list.append({'mask':mask, 'mems':mems})
    return mask_mem_list

# https://realpython.com/python-bitwise-operators/#setting-a-bit
# https://realpython.com/python-bitwise-operators/#unsetting-a-bit

def apply_value_mask(mask, num):
    value_mask = [(i, int(v)) for i, v in enumerate(mask[::-1]) if v not in 'X']
    new_num = num
    for bit_index, bit_val in value_mask:
        if bit_val: # If bit_val is 1, then set the bit
            new_num |= (1 << bit_index)
        else:       # If bit val is 0, then unset the bit
            new_num &= ~(1 << bit_index)
    return new_num

def apply_address_mask(mask, num):
    num_string = f'{num:0{len(mask)}b}'
    masked_num_list = []
    for m, n in zip(mask, num_string):
        if m in '0':
            masked_num_list.append(n)
        else:
            masked_num_list.append(m)
    masked_num = ''.join(masked_num_list)
    new_num_list = []
    count_of_x = masked_num.count('X')
    for p in product(('0','1'),repeat=count_of_x):
        temp_num = masked_num
        for v in p:
            temp_num = temp_num.replace('X',v,1)
        new_num_list.append(int(temp_num,2))
    return new_num_list


def answer_a(input_data=data):
    inputs = generate_input(input_data)
    memory = {} # Empty dictionary to store memory values and allow overwriting of locations
    for group in inputs:
        for mem in group['mems']:
            memory[mem[0]] = apply_value_mask(group['mask'],mem[1])
    return sum(memory.values())


def answer_b(input_data=data):
    inputs = generate_input(input_data)
    memory = {} # Empty dictionary to store memory values and allow overwriting of locations
    for group in inputs:
        for mem in group['mems']:
            addresses = apply_address_mask(group['mask'],mem[0])
            for address in addresses:
                memory[address] = mem[1]
    return sum(memory.values())

# submit(answer_a(data), part='a')
# submit(answer_b(data), part='b')
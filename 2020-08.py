from aocd import data, submit
from aocd_setup import get_test_data, get_test_answer

def test_a():
    assert answer_a(
                    input_data=get_test_data(part='a', fname=__file__)
    ) == get_test_answer(part='a', fname=__file__)

def test_b():
    assert answer_b(
                    input_data=get_test_data(part='a', fname=__file__)
    ) == get_test_answer(part='b', fname=__file__)

def test_correct_a():
    assert answer_a(input_data=data) == 1586

def test_correct_b():
    assert answer_b(input_data=data) == 703

def test_flip():
    assert flip_operation(('jmp',0)) == ('nop',0)
    assert flip_operation(('nop',1)) == ('jmp',1)
    assert flip_operation(('acc',2)) == ('acc',2)

def test_find_ops():
    test_data_a = create_code_tuple(get_test_data(part='a', fname=__file__))
    assert find_ops(test_data_a, 'nop') == [0]
    assert find_ops(test_data_a, 'jmp') == [2,4,7]
    assert find_ops(test_data_a, ['nop','jmp']) == [0,2,4,7]

def test_insert():
    test_data_a = create_code_tuple(get_test_data(part='a', fname=__file__))
    test_data_nop = create_code_tuple(get_test_data(part='nop', fname=__file__))
    test_data_jmp = create_code_tuple(get_test_data(part='jmp', fname=__file__))
    assert insert_flipped_instruction(test_data_a, find_ops(test_data_a, 'nop')[0]) == test_data_nop
    assert insert_flipped_instruction(test_data_a, find_ops(test_data_a, 'jmp')[1]) == test_data_jmp


def create_code_tuple(data):
    return tuple(
                tuple(
                        [    l.split(" ")[0], 
                         int(l.split(" ")[1])]
                ) for l in data.split("\n")
            )

def flip_operation(instruction):
    if instruction[0] == 'jmp':
        return ('nop', instruction[1])
    elif instruction[0] == 'nop':
        return ('jmp', instruction[1])
    else:
        return instruction

def find_ops(instructions, operations):
    ops_list = []
    for line, instruction in enumerate(instructions):
        if instruction[0] in operations:
            ops_list.append(line)
    return ops_list

def insert_flipped_instruction(instructions, line):
    instruction_list = list(instructions)
    instruction_list[line] = flip_operation(instructions[line])
    return tuple(instruction_list)

def op(state, instruction):
    if instruction[0] == 'nop':
        state["line"] += 1
        return state
    elif instruction[0] == 'acc':
        state["acc"] += instruction[1]
        state["line"] += 1
        return state
    elif instruction[0] == "jmp":
        state["line"] += instruction[1]
        return state

def print_state(state):
    print("acc =", state["acc"], 
          "\nline =", state["line"],
          "\nhistory =", state["history"],
          "\ncondition =", state["condition"])

def increment_history(state):
    state["history"].append(state["line"])
    return state

def keep_going(state):
    return state["line"] not in state["history"]

def run_boot(code_tuple):
    state = {"acc": 0, "line": 0, "history": [], "condition": ""}
    while keep_going(state):
        if state["line"] >= len(code_tuple):
            state["condition"] = "success"
            return state
        state = increment_history(state)
        state = op(state, code_tuple[state["line"]])
    else:
        state["condition"] = "infinite loop"
        return state

def answer_a(input_data=data):
    end_state = run_boot(create_code_tuple(input_data))
    return end_state["acc"]

def answer_b(input_data=data):
    instructions = create_code_tuple(input_data)
    ops_list = find_ops(instructions, ['nop','jmp'])
    for op_line in ops_list:
        trial_op_tuple = insert_flipped_instruction(instructions, op_line)
        end_state = run_boot(trial_op_tuple)
        if end_state["condition"] == "success":
            return end_state["acc"]
    return 0

# submit(answer_a(data), part='a')
# submit(answer_b(data), part='b')
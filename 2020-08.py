from aocd import data, submit
from aocd_setup import get_test_data, get_test_answer

# print(get_test_data(part='a', fname=__file__))
# print(get_test_answer(part='a', fname=__file__))

# print(data)

def test_a():
    assert answer_a(
                    input_data=get_test_data(part='a', fname=__file__)
    ) == get_test_answer(part='a', fname=__file__)

def create_code_tuple(data):
    # print(data.split("\n"))
    # for l in data.split("\n"):
    #     print(l)
    #     for i,o in zip(l.split(" ")):
    #         print(i,o)
    #     # print([tuple(io[0],int(io[1])) for io in l.split(" ")])
    return tuple(
                tuple(
                        [    l.split(" ")[0], 
                         int(l.split(" ")[1])]
                ) for l in data.split("\n")
            )

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
          "\nhistory = ", state["history"])

def increment_history(state):
    state["history"].append(state["line"])
    return state

def keep_going(state):
    return state["line"] not in state["history"]

def run_boot(code_tuple):
    state = {"acc": 0, "line": 0, "history": []}
    while keep_going(state):
        print("in the loop")
        print_state(state)
        state = increment_history(state)
        print_state(state)
        state = op(state, code_tuple[state["line"]])
        print_state(state)
    else:
        return state

def answer_a(input_data=data):
    end_state = run_boot(create_code_tuple(input_data))
    return end_state["acc"]

submit(answer_a(data), part='a')
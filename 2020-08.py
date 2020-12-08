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

def run_boot(code_tuple):
    acc = 0
    line = 0


def answer_a(input_data=data):
    run_boot(create_code_tuple(input_data))
    return 0
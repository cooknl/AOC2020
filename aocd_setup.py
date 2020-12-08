from aocd import get_data, submit
from os.path import isfile

def get_test_data(part,fname=__file__):

    with open(fname[:-3] + "-test-data-" + part + ".txt","r") as f:
        test_data = f.read()

    return test_data

def get_test_answer(part,fname=__file__):

    with open(fname[:-3] + "-test-answer-" + part + ".txt", "r") as f:
        test_answer = f.read()

    return int(test_answer)

def setup_info(file_name):

    fname = file_name[:-3].split(sep="-")

    p = fname[2]
    d = int(fname[1])
    y = int(fname[0])

    data_fname = fname[0] + '-' + fname[1] + '.txt'

    if isfile(data_fname):
        with open(data_fname, 'r') as f:
            data = f.read()
    else:
        data = get_data(day=d, year=y)

        with open(fname[0] + '-' + fname[1] + '.txt','w') as f:
            f.write(data)

    return dict(part = p, day = d, year = y, data = data)

def report(answer, part, day, year):
    submit(answer, part=part, day=day, year=year)
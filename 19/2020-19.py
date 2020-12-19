from aocd import data, submit

def test_answer():
    assert answer(data)['a'] != 0
    assert answer(data)['b'] != 0

def answer(input_data):
    return {'a':0, 'b':0}

if __name__ == "__main__":
    
    try:
        part = sys.argv[1]
        submit(answer(data)[part], part=part)
    except IndexError:
        raise SystemExit("Usage: Include part as an command line argument\n Examples:\n'python 2020-dd.py a'\n'python 2020-dd.py b'")
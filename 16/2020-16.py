from aocd import data, submit
from pathlib import Path
import re

# https://adventofcode.com/2020/day/16

def test_answer():
    assert answer(Path('2020-16-test-data-a.txt').read_text()) == 71
    assert answer(data) == 25961

# https://realpython.com/python-sets/

def generate_input(input_data):
    return re.split(r'\n\nyour ticket:\n|\n\nnearby tickets:\n', input_data)

def answer(input_data=data):
    chunks = generate_input(input_data)
    included = set()
    for line in chunks[0].split('\n'):
        for t in re.findall(r'(\d+)-(\d+)', line):
            t = [int(c) for c in t]
            included.update( list(range(t[0], t[1]+1)))
    nearby = [int(c) for c in re.split('\n|,',chunks[2])]
    not_included = [n for n in nearby if n not in included]
    return sum(not_included)

if __name__ == "__main__":
    submit(answer(data), part='a')
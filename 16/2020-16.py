from aocd import data, submit
from pathlib import Path
import re

# https://adventofcode.com/2020/day/16

def test_answer():
    assert answer(Path('2020-16-test-data-a.txt').read_text()) == 71

def generate_input(input_data):
    chunks = re.split(r'\n\nyour ticket:\n|\n\nnearby tickets:\n', input_data)
    included = set()
    for line in chunks[0].split('\n'):
        print(*re.findall(r'(\d+)-(\d+)', line))
    return 0

def answer(input_data=data):
    print(generate_input(input_data))
    return 0

if __name__ == "__main__":
    answer(data)
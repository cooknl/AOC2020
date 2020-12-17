from aocd import data, submit
from pathlib import Path
import re

# https://adventofcode.com/2020/day/16

def test_answer():
    assert answer(Path('2020-16-test-data-a.txt').read_text())['a'] == 71
    assert answer(data)['a'] == 25961
    assert answer(Path('2020-16-test-data-b.txt').read_text())['b'] != 0
    assert answer(data)['b'] == 603409823791

# https://realpython.com/python-sets/

def generate_input(input_data):
    return re.split(r'\n\nyour ticket:\n|\n\nnearby tickets:\n', input_data)

def field_scan(candidates, fields_confirmed):
    for i, c in enumerate(candidates):
        if len(c) == 1:
            fields_confirmed[i] = c[0]
    for i, f in enumerate(fields_confirmed):
        if f:
            for i, c in enumerate(candidates):
                if f in candidates[i]:
                    candidates[i].remove(f)
    return candidates, fields_confirmed

def answer(input_data=data):
    chunks = generate_input(input_data)
    included = set()
    rules = {}
    for line in chunks[0].split('\n'):
        for f in re.findall(r'(.+):', line):
            rules[f] = []
        for t in re.findall(r'(\d+)-(\d+)', line):
            t = [int(c) for c in t]
            r_list = list(range(t[0], t[1]+1))
            included.update( r_list )
            rules[f].extend( r_list )

    nearby = [[int(c) for c in ticket.split(',')] for ticket in chunks[2].split('\n')]
    not_included = [n for ticket in nearby for n in ticket if n not in included]
    answer_a = sum(not_included)

    valid_tickets = []
    for ticket in nearby:
        if not set(ticket).intersection(not_included):
            valid_tickets.append(ticket)

    available_fields = list(rules.keys())
    ticket_field_candidates = []
    ticket_fields = ['' for _ in range(len(rules))]
    for j in range(len(rules)):
        potential_fields = []
        for r in available_fields:
            this_rule = True
            for i in range(len(valid_tickets)):
                if valid_tickets[i][j] not in rules[r]:
                    this_rule = False
            if this_rule:
                potential_fields.append(r)
        ticket_field_candidates.append(potential_fields)

    while any(ticket_field_candidates):
        ticket_field_candidates, ticket_fields = field_scan(ticket_field_candidates, ticket_fields)

    my_ticket = [int(n) for n in chunks[1].split(',')]

    answer_b = 1
    for f, n in zip(ticket_fields, my_ticket):
       if 'departure' in f:
           answer_b *= n

    return {'a':answer_a, 'b':answer_b}

if __name__ == "__main__":
    # submit(answer(data)['a'], part='a')
    # submit(answer(data)['b'], part='b')
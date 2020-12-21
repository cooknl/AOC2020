from aocd import data, submit
import sys
import re
from numbers import Integral
import itertools

#--------TEST

test_data_a1 = '''0: 1 2
1: "a"
2: 1 3 | 3 1
3: "b"

a
b
aab
aba
'''

test_data_a2 = '''0: 4 1 5
1: 2 3 | 3 2
2: 4 4 | 5 5
3: 4 5 | 5 4
4: "a"
5: "b"

ababbb
bababa
abbbab
aaabbb
aaaabbb
'''

def test_render_pattern():
    assert render_pattern(['a']) == '(a)'
    assert render_pattern(['b']) == '(b)'
    assert render_pattern(['a', [['a', 'b'], ['b', 'a']]]) == '(a((ab)|(ba)))'
    assert render_pattern(['a',
                            [[
                              [['a','a'],['b','b']],
                              [['a','b'],['b','a']]
                              ],
                              [
                              [['a','b'],['b','a']],
                              [['a','a'],['b','b']]
                              ]],
                              'b'
                              ]) == '(a((((aa)|(bb))((ab)|(ba)))|(((ab)|(ba))((aa)|(bb))))b)'

def test_nums_in_this_list():
    assert nums_in_this_list([1])
    assert not nums_in_this_list(['a'])
    assert nums_in_this_list(['a','b',[[3,'b'],['a','a']]])
    assert not nums_in_this_list(['a','b',[['b','b'],['a','a']]])

def test_build_pattern():
    assert build_pattern(gen_input(test_data_a1)['rules'], 
                       'a') == 'a'
    assert build_pattern(gen_input(test_data_a1)['rules'], 
                       'b') == 'b'
    assert build_pattern(gen_input(test_data_a1)['rules'],
                        [1, 2]) == ['a', [[1,3], [3,1]]]
    assert build_pattern(gen_input(test_data_a1)['rules'],
                        [[1,3], [3,1]]) == [['a','b'],['b','a']]

# def test_parse_rules():
#     assert parse_rules(gen_input(test_data_a1)['rules'], 
#                        gen_input(test_data_a1)['rules'][1]) == 'a'
#     assert parse_rules(gen_input(test_data_a1)['rules'], 
#                        gen_input(test_data_a1)['rules'][3]) == 'b'
#     assert parse_rules(gen_input(test_data_a1)['rules'], 
#                        gen_input(test_data_a1)['rules'][0]) == '(a((ab)|(ba)))'
#     assert parse_rules(gen_input(test_data_a2)['rules'], 
#                        gen_input(test_data_a2)['rules'][0]) == '(a((((aa)|(bb))((ab)|(ba)))|(((ab)|(ba))((aa)|(bb))))b)'

def test_rule_matches():
    assert single_rule_match('a','a')
    assert not single_rule_match('b','a')
    assert single_rule_match('a','aab')
    assert single_rule_match('a','aba')
    assert not single_rule_match('(a((ab)|(ba)))','a')
    assert not single_rule_match('(a((ab)|(ba)))','b')
    assert single_rule_match('(a((ab)|(ba)))','aab')
    assert single_rule_match('(a((ab)|(ba)))','aba')


def test_answer():
    # assert answer(test_data_a1)['a'] == 2
    # assert answer(test_data_a2)['a'] == 2
    assert answer(data)['a'] != 0
    # assert answer(data)['b'] != 0

#-----------BIZNESS


### This hit the maximum recursion depth...PROBABLY BECAUSE OF THE MIS-PARSED MULTIPLE DIGIT NUMBERS
# # Recursive parsing of a regex pattern
# def parse_rules(rules, value):
#     if isinstance(value, str): # If you've reached the 'a' or 'b' just return it (0-condition)
#         return value
#     elif isinstance(value, Integral): # If you have an integer, then it's a rule address (key), so parse the rule
#         return parse_rules(rules, rules[value])
#     elif isinstance(value, list): # If you have a list, then it's either a list of addresses, or a list of lists which indicates "or"
#         if isinstance(value[0], list): # If the first element is a list, then it's a list of lists, so enclose the groups in parens and separate them with |
#             return ''.join(['(','|'.join([parse_rules(rules, value[i])
#                              for i in range(len(value))]),
#                             ')'])
#         else: # If the first element is not a list, then it's a list of addresses, so enclose the group in parens
#             return ''.join(['(',
#                             ''.join([parse_rules(rules, rules[value[i]]) for i in range(len(value))]),
#                             ')'])

def render_pattern(l):
    pattern_list = ['(',')']
    for e in l:
        if isinstance(e, str):
            pattern_list.insert(-1,e)
        elif isinstance(e, list):
            if isinstance(e[0], list):
                pattern_list.insert(-1,
                                    ''.join(['(',
                                             '|'.join([render_pattern(j) for j in e]),
                                             ')'])
                                    )
            else:
                pattern_list.insert(-1,''.join(e))
    return ''.join(pattern_list)

def nums_in_this_list(l):
    if not l:
        return -1
    else:
        while sum(isinstance(e,list) for e in l):
            try:
                l= list(itertools.chain.from_iterable(l))
            except TypeError:
                return True
        return sum(isinstance(e, int) for e in l)


# What if we iteratively build the string, instead of recursively? 
def build_pattern(rules, value):
    if isinstance(value, str):
        return value
    elif isinstance(value, Integral):
        return rules[value]
    if isinstance(value, list):
        if isinstance(value[0], list):
            return [build_pattern(rules, v) for v in value]
        # else:
        #     return [rules[v] for v in value]

def single_rule_match(rule, msg):
    return re.findall(f'({rule}){{1}}',msg)

def gen_input(input_data):
    raw_rules, raw_messages = input_data.split('\n\n')
    rules = {int(line.split(': ')[0]):line.split(': ')[1] for line in raw_rules.split('\n') if line}
    for k,v in rules.items():
        if '"' in v:
            rules[k] = v.replace('"','')
        elif '|' in v:
            rules[k] = [[int(c) for c in variant.split(' ')] for variant in v.split(' | ')]
        else:
            rules[k] = [int(c) for c in v if c in '0123456789']
    messages = [line for line in raw_messages.split('\n') if line]
    return {'rules':rules, 'msgs': messages}

def answer(input_data):
    inputs = gen_input(input_data)
    print(inputs['rules'])
    #pattern = parse_rules(inputs['rules'],inputs['rules'][0])
    # raw_pattern = inputs['rules'][0]
    # while nums_in_this_list(raw_pattern):
    #     raw_pattern = [build_pattern(inputs['rules'],e) for e in raw_pattern]
    # pattern = render_pattern(raw_pattern)
    answer_a = []
    # for msg in inputs['msgs']:
    #     answer_a.append(single_rule_match(pattern, msg))
    return {'a':sum(1 for e in answer_a if e), 'b':0}

if __name__ == "__main__":
    print(answer(data))

    # try:
    #     part = sys.argv[1]
    #     submit(answer(data)[part], part=part)
    # except IndexError:
    #     raise SystemExit("Usage: Include part as an command line argument\n Examples:\n'python 2020-dd.py a'\n'python 2020-dd.py b'")
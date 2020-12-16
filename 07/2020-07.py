from aocd import data, submit
import re
from collections import defaultdict

def get_test_data(part,fname=__file__[:-3]):

    with open(fname + "-test-data-" + part + ".txt","r") as f:
        test_data = f.read()

    return test_data

def get_test_answer(part,fname=__file__[:-3]):

    with open(fname + "-test-answer-" + part + ".txt", "r") as f:
        test_answer = f.read()

    return int(test_answer)

def test_a():
    assert answer_a(input_data=get_test_data(part='a')) == get_test_answer(part='a')

def test_b1():
    assert answer_b(input_data=get_test_data(part='a')) == get_test_answer(part='b1')

def test_b2():
    assert answer_b(input_data=get_test_data(part='b2')) == get_test_answer(part='b2')

# def test_submit():
#     assert answer_b(input_data=data) == 0

def recurse_containees(rules, bag_key, bag_list):
    # This builds a list of all the bags that can contain the BOI
    for bag in rules[bag_key]:
        bag_list.append(bag)
        for bag_key in bag.keys():
            if rules[bag_key]:
                recurse_containees(rules, bag_key, bag_list)
    return bag_list

def recurse_quantities(rules, bag_key, quantity=0):
    # This recursively traverses the graph of the rules by going down each
    # of the containEE bags until it finds a containEE with no rules
    counts = [c for c in rules[bag_key].values()]
    bags = [b for b in rules[bag_key].keys()]
    if not rules[bag_key]: #This containEE is NOT a containER, so holds no bags
        return 0
    else:
        # The trickiest part was finding the means to both SUM and MULTIPLY
        # while including the containER in the count (not just the bags it's holding)
        return sum([c + c * recurse_quantities(rules, b) for c,b in zip(counts,bags)]) 

def answer_a(input_data, BOI='shiny gold'):
    '''
    BOI = Bag of Interest (it's an F-16 joke)
    '''

    # https://regex101.com 

    # https://docs.python.org/3/library/collections.html#collections.defaultdict
    # A list is used as the default to provide for empty lists in the event
    # of no bags, since rules will be a list of dictionaries
    rules = defaultdict(list)

    # rules is a dictionary that answers the question
    # Given this bag (containee), which other bags (containers) can hold it, 
    # and how many (quantity)?
    for rule in input_data.split("\n"):
        container, containees = re.findall(r'^([\w\s]+) bags contain ([\,\w\s]+)',rule)[0]
        for quantity, containee in re.findall(r'(\d) ([\w\s]+) bag',containees):
            rules[containee].append({container:int(quantity)})

    BOI_list = recurse_containees(rules, bag_key=BOI, bag_list=[])
    
    return len({k for b in BOI_list for k in b.keys()})

def answer_b(input_data, BOI='shiny gold'):

    rules = defaultdict(dict)

    # rules is a dictionary that answers the question
    # Given this bag (containER), how many (quantity) other bags (containEEs) 
    # does it hold?
    for rule in input_data.split("\n"):
        container, containees = re.findall(r'^([\w\s]+) bags contain ([\,\w\s]+)',rule)[0]
        for quantity, containee in re.findall(r'(\d) ([\w\s]+) bag',containees):
            rules[container][containee] = int(quantity)

    return recurse_quantities(rules, bag_key=BOI)

# submit(answer_a(input_data=data, BOI='shiny gold'), part='a')
submit(answer_b(input_data=data, BOI='shiny gold'), part='b')

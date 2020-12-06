from aocd import get_data, submit
from itertools import combinations
from math import prod

p = "b"
d = 1
y = 2020

data01a = get_data(day=d, year=y)

with open('01a.txt','w') as f:
    f.write(data01a)

data01a_list = [int(i) for i in data01a.split(sep="\n")]

#print(data01a_list)

answer = 0

for c in combinations(data01a_list,3):
    if sum(c) == 2020:
        answer = prod(c)

submit(answer, part=p, day=d, year=y)
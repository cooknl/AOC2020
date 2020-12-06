from aocd import get_data, submit

fname = __file__[:-3].split(sep="-")

p = fname[2]
d = int(fname[1])
y = int(fname[0])

data = get_data(day=d, year=y).split(sep="\n")

width = len(data[0])

def count_trees(data, rt, dn):
    idx = 0
    num_trees = 0

    #https://stackoverflow.com/questions/1403674/pythonic-way-to-return-list-of-every-nth-item-in-a-larger-list
    #https://www.geeksforgeeks.org/range-vs-xrange-python/
    for row in (data[i] for i in range(dn, len(data), dn)):
        idx = (idx + rt) % width
        if row[idx] == "#":
            num_trees += 1
    return num_trees

prod_trees = 1

rules = [(1,1),
         (3,1),
         (5,1),
         (7,1),
         (1,2)]

for rule in rules:
    prod_trees *= count_trees(data, rule[0], rule[1])


submit(prod_trees, part=p, day=d, year=y)


from aocd import get_data, submit

fname = __file__[:-3].split(sep="-")

p = fname[2]
d = int(fname[1])
y = int(fname[0])

data = get_data(day=d, year=y).split(sep="\n")

with open(fname[0] + '-' + fname[1] + '.txt','w') as f:
    f.write(get_data(day=d, year=y))

width = len(data[0])

idx = 0
num_trees = 0

for row in data[1:]:
    idx = (idx + 3) % width
    if row[idx] == "#":
        num_trees += 1

submit(num_trees, part=p, day=d, year=y)


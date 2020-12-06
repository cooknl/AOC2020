from aocd import get_data, submit

fname = __file__[:-3].split(sep="-")

p = fname[2]
d = int(fname[1])
y = int(fname[0])

data = get_data(day=d, year=y).split(sep="\n")

with open(fname[0] + '-' + fname[1] + '.txt','w') as f:
    f.write(get_data(day=d, year=y))

def get_policy(line):
    b, l, p = line.split(" ")
    lo, hi = [int(i) for i in b.split("-")]
    l = l[0]
    return lo, hi, l, p

num_valid = 0

for row in data:
    low, high, letter, passwd = get_policy(row)
    if low <= passwd.count(letter) <= high:
        num_valid += 1

submit(num_valid, part=p, day=d, year=y)


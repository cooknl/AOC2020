import aocd_setup

info = aocd_setup.setup_info(__file__)

# https://docs.python.org/3.6/library/functions.html#int

data = info["data"].split("\n")

seat_ids = [
            int(
                s[:7].replace("B","1").replace("F","0") +  
                s[7:].replace("R","1").replace("L","0")
                ,2
          )
            for s in data
]

sorted_seat_ids = sorted(seat_ids)

# https://stackoverflow.com/questions/19184335/is-there-a-need-for-rangelena

diff_sorted_seat_ids = [
                        (s1,
                        s1 - s0 - 1)
                        for s0,s1 in zip(sorted_seat_ids[:-1],
                                         sorted_seat_ids[1:])
]

# https://www.geeksforgeeks.org/python-find-the-tuples-containing-the-given-element-from-a-list-of-tuples/
selected_seat = list(filter(lambda x: x[1]==1, diff_sorted_seat_ids))[0][0] - 1


aocd_setup.report(selected_seat, info["part"], info["day"], info["year"])
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

aocd_setup.report(max(seat_ids), info["part"], info["day"], info["year"])
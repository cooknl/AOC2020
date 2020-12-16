import aocd_setup

info = aocd_setup.setup_info(__file__)

groups = [g for g in info["data"].split("\n\n")]

group_replies = [r.split("\n") for r in groups]

group_reply_sets = [set().union(*r) for r in group_replies]

print(group_reply_sets)

# http://www.java2s.com/Tutorial/Python/0180__Collections/lenreturnsthenumberofelements.htm

group_reply_set_sums = [len(s) for s in group_reply_sets]

answer = sum(group_reply_set_sums)

# aocd_setup.report(answer=answer, 
#        part=info["part"], 
#        day=info["day"],
#        year=info["year"])
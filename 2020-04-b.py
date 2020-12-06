import aocd_setup
import re

info = aocd_setup.setup_info(__file__)

raw_passports = info["data"].split(sep="\n\n")

# https://www.geeksforgeeks.org/python-program-to-create-a-dictionary-from-a-string/
# https://stackoverflow.com/questions/4998629/split-string-with-multiple-delimiters-in-python
# https://www.geeksforgeeks.org/python-check-if-given-multiple-keys-exist-in-a-dictionary/

passport_field_lists = [raw_passport.replace('\n',' ').split(' ') for raw_passport in raw_passports]

passport = {}

count = 0

rqd_fields = {"byr", #(Birth Year)
              "iyr", #(Issue Year)
              "eyr", #(Expiration Year)
              "hgt", #(Height)
              "hcl", #(Hair Color)
              "ecl", #(Eye Color)
              "pid", #(Passport ID)
              #"cid", #(Country ID)
}

'''
byr (Birth Year) - four digits; at least 1920 and at most 2002.
iyr (Issue Year) - four digits; at least 2010 and at most 2020.
eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
hgt (Height) - a number followed by either cm or in:
If cm, the number must be at least 150 and at most 193.
If in, the number must be at least 59 and at most 76.
hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
pid (Passport ID) - a nine-digit number, including leading zeroes.
cid (Country ID) - ignored, missing or not.
'''


for passport_field_list in passport_field_lists:
    for field in passport_field_list:
        k,v = field.split(":")
        passport[k] = v
    if (
        (passport.keys() >= rqd_fields) and
        (1920 <= int(passport["byr"]) <= 2002) and
        (2010 <= int(passport["iyr"]) <= 2020) and
        (2020 <= int(passport["eyr"]) <= 2030) and
        (passport["ecl"] in ("amb", "blu", "brn", "gry", "grn", "hzl", "oth")) and 
        (
            (
                (passport["hgt"][-2:] == "cm") and 
                (150 <= int(passport["hgt"][:-2]) <= 193)
            ) or (
                (passport["hgt"][-2:] == "in") and 
                (59 <= int(passport["hgt"][:-2]) <= 76)
            )
        ) and 
        (re.match(r"^[0-9]{9}$",passport["pid"])) and
        (re.match(r"\#[0-9a-f]{6}",passport["hcl"]))
    ):
        count += 1
    passport = {}

aocd_setup.report(count, part=info["part"], day=info["day"], year=info["year"])
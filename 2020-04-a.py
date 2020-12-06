import aocd_setup

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

for passport_field_list in passport_field_lists:
    for field in passport_field_list:
        k,v = field.split(":")
        passport[k] = v
    if passport.keys() >= rqd_fields:
        count += 1
    passport = {}

aocd_setup.report(count, part=info["part"], day=info["day"], year=info["year"])
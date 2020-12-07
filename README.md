# AOC2020

[Advent of Code 2020](https://adventofcode.com/2020) Solutions and discussion

## Day 01 (Python)

- Learned about [advent-of-code-data](https://github.com/wimglenn/advent-of-code-data)
- Remembered with-open-as
- Remembered [itertools.combinations](https://docs.python.org/3/library/itertools.html#itertools.combinations)
- Remembered [math.prod](https://docs.python.org/3/library/math.html?highlight=math#math.prod) isn't built-in
- Writing inputs to a file for local work without hitting server

## Day 02 (Python)

- Started using filename for metadata
- Learned `__file__`
- Learned `l <= n < h` is a valid comparison expression

## Day 03 (Python)

- Used modulus operator `%` to wrap map

## Day 04 (Python)

- Created [aocd_setup.py] to extend automation of `aocd` to capture metadata and data, as well as for submission
- Initially had line splitting, but for some problems it's `\n\n` and for others it's `\n`, so kept it out of [aocd_setup.py]
- Learned that `>=` comparison allows for check of keys in a dictionary against a set of keys
- A lot of confusion on nested for loops about where the key:value split has to occur
- [regex101](https://www.regex101.com) to the rescue, once again
- Learned that `^` and `$` can be important so that the string must be **exactly** `{9}` characters, not a subset of greater than 9 characters

## Day 05 (Python)

- When they say "binary" you can believe them and just convert to unsigned int
- [int()](https://docs.python.org/3.6/library/functions.html#int) has built-in binary string to integer conversion
- `zip(a_list[:-1],a_list[1:])` creates a side-by-side tuple of neighboring list elements without messing with the original `a_list` somehow offset by one
- `lambda` FTW!

## Day 06 (Python)

- Set unions and intersections don't _quite_ work the same way
- Nested list comprehensions 😵

## Day 07 (Python)

- Created `AOCD_DIR` and `AOC_SESSION` environment variable using Powershell, per the [`advent-of-code-data` README](https://github.com/wimglenn/advent-of-code-data/blob/master/README.rst), as I'm on a Win10 machine
    - Per [the PowerShell docs](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_environment_variables?view=powershell-7.1) the PowerShell 
    script for this is ```PowerShell $Env:<variable-name> = "<new-value>" ```
    - So, I will now be using ```Python import os; os.environ["AOCD_DIR"]```
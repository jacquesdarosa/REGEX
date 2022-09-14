import re

def make_happy(txt):
    return re.sub("(?<=[:8x;])\(",')',txt)

given_string = "print:[('x(')"

print(make_happy(given_string))
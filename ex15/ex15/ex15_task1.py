import re

given_string = "5+1"
print(re.match("\\d+\\s?[\\+\\*/%-]\\s?\\d+", given_string))

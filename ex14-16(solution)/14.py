import re

given_string = "0023.07623070"
print(re.sub("^0*(\\d+\\.\\d*?[1-9])0*$", r"\1", given_string))


import re

test_string = input('enter your string here:')

 # using ljust()
 # adding trailing zero

result = test_string.strip('0')

print(result)

'''Markus solution : mport re

given_string = "0023.07623070"
print(re.sub("^0*(\\d+\\.\\d*?[1-9])0*$", r"\1", given_string))'''
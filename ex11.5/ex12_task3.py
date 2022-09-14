### Task 3

'''Create a variable called `text` to store the data: `Berlin is a city of culture.` . Replace the spaces with a hyphen.

- Your result should look like this:


Berlin-is-a-city-of-culture.'''

import re

text = 'Berlin is a city of culture.'
pattern = re.sub(r'\s', '-', text)
print(pattern)
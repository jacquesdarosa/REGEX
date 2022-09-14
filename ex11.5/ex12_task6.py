### Task 6

'''Create a variable called `text` to store the data: `The rain in Spain.`. Count how many times the subphrase `ai` appears in the string. Print the results on the screen.

- Your result should look like this:

2 '''

import re

text = 'The rain in Spain'

pattern = 'ai'
Count= len(re.findall(pattern, text))
print(Count)


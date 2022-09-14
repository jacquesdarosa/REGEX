### Task 4

'''Create a variable called `text` to store the data: `Berlin is a city of culture.` . Search if the phrase `in` appears inside the string. 
Print the output of the regex function.

- Your result should look like this:

```
<re.Match object; span=(4, 6), match='in'> '''

import re

text = 'Berlin is a city of culture'

pattern = re.search (r'in', text)
print(pattern)
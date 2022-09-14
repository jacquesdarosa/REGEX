### Task 5

'''Use the `text` variable from the previous task. Create a regular expression to look for any word that starts with an upper case "B". 
Print the position (start- and end-position) of the first match occurrence. 

- Your result should look like this:

```
(0, 6)'''

import re

text = 'Berlin is a city of culture.'

pattern = re.search(r'\bB\w+', text)
print(pattern.span())


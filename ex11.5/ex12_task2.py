### Task 2

'''Create a variable called `text` to store the data: `Berlin is surrounded by the State of Brandenburg and contiguous with Potsdam, Brandenburg's capital.` . 
Then search for the word `Frankfurt` in the string . 

- Your result should look like this:

```
None'''
import re

text = "Berlin is surrounded by the State of Brandenburg and contiguous with Potsdam, Brandenburg's capital."

pattern = re.search(r'Frankfurt', text)

print(pattern)

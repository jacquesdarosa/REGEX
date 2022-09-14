## Tasks

### Task 1

'''Create a variable called `text` to store the data: `Berlin is a world city of culture, politics, media and science.` . 
Then search for the first white space character in the string and print its location using the appropriate label. 

- Your result should look like this:

```
The first white-space character is located at position: 6'''

import re


text = 'Berlin is a world city of culture, politics, media and science.'

pattern = re.search(r'\s', text)

print('the first white-space is located at position:', pattern.start())



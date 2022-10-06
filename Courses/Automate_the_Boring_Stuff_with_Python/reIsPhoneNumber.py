import re

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d') # r is for raw string
mo = phoneNumRegex.search('My number is 415-555-4242.')
print(mo.group())
print(phoneNumRegex.findall('My number is 785-555-4242.')) # similar result to search()
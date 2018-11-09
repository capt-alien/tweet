import re

test = re.findall(r'\b[a-z]{0,15}\b','abcedab adsfasd-adacd')
print(test)

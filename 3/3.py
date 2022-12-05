from collections import Counter
import string

raw_data = open('data').read()

backpacks = raw_data.split('\n')

def findChar(a: str, b: str):
    return ''.join(set(a).intersection(b))

def getValue(char: str):
    val = string.ascii_lowercase.find(char)
    if val == -1:
        val = string.ascii_uppercase.find(char) +26
    return val +1

total_val = 0
for x in backpacks:
    c1 = x[0: int(len(x)/2)]
    c2 = x[int(len(x)/2):]
    found = findChar(c1, c2)
    total_val +=getValue(found)
    print(getValue(found))

print(total_val)
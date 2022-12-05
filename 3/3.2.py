import string

def findChar(a: str, b: str, c: str):
    return ''.join(set(a).intersection(b).intersection(c))

def getValue(char: str):
    val = string.ascii_lowercase.find(char)
    if val == -1:
        val = string.ascii_uppercase.find(char) +26
    return val +1

def solve(data):
    backpacks = data.split('\n')
    total_val = 0
    chunks = zip(*[iter(backpacks)]*3)
    for chunk in chunks:
        found = findChar(chunk[0], chunk[1], chunk[2])
        total_val +=getValue(found)

    print(total_val)

with open('data') as file:
    solve(file.read())
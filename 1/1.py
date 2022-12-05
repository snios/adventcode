
def solve(data):
    array = data.split("\n")
    
    count = 0
    for x in array:
        if x.isdigit():
            count += int(x)
        else:
            count = 0

    print(count)

with open('data') as file:
    solve(file.read())



def solve(data):
    array = data.split("\n")

    results = []
    count = 0
    for x in array:
            if x.isdigit():
                count += int(x)
            else:
                results.append(count)
                count = 0

    results.sort()
    print (sum(results[len(results)-3:]))


with open('data') as file:
    solve(file.read())

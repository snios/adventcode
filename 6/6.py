from collections import Counter

def solve(data):
    data_lenght = len(data)
    answer = 0
    for x in range(data_lenght):
        if len(Counter(data[x:int(x+4)]).items()) >3:
            print(data[x:int(x+4)])
            answer = x+4
            break
    print('answer: ', answer)

with open('data') as file:
    solve(file.read())
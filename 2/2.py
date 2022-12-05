raw_data = '''A Y
B X
C Z'''

normalized = raw_data.replace('A', '0').replace('X', '0').replace('B', '1').replace('Y', '1').replace('C', '2').replace('Z', '2').split('\n')

p2_score = 0
for x in normalized:
    players = x.split(' ')
    p1 = int(players[0])
    p2 = int(players[1])
    if(p1 +1) %3 == p2:
        print('p2 won')
        p2_score += 6+p2+1
    elif p1 == p2:
        print('draw')
        p2_score +=  3+p2+1
    else:
        print('p1 won')
        p2_score += p2+1

print(p2_score)
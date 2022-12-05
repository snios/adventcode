def solve(data):

    normalized = data.replace('A', '0').replace('X', '0').replace('B', '1').replace('Y', '1').replace('C', '2').replace('Z', '2').split('\n')

    p2_score = 0
    for x in normalized:
        players = x.split(' ')
        p1 = int(players[0])
        p2 = int(players[1])
        if p2 == 0:
            # need to loose
            p2 = (p1 -1)%3
        elif p2 == 1:
            # need to draw
            p2 = p1
        elif p2 == 2:
            # need to win
            p2 = (p1 +1)%3
        if(p1 +1) %3 == p2:
            # p2 won
            p2_score += 6+p2+1
        elif p1 == p2:
            # draw
            p2_score +=  3+p2+1
        else:
            # p1 won
            p2_score += p2+1

    print(p2_score)

with open('data') as file:
    solve(file.read())
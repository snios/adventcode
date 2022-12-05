def solve(data):
    workpairs = data.splitlines()
    count = 0
    for workpair in workpairs:
        ranges = workpair.split(',')
        range1 = range(int(ranges[0].split('-')[0]), int(ranges[0].split('-')[1]) +1)
        range2 = range(int(ranges[1].split('-')[0]), int(ranges[1].split('-')[1]) +1)
        set1 = set(range1)
        set2 = set(range2)
        intersected =  set1.intersection(set2)
        if len(intersected) > 0:
            count += 1
    print('answer', count)

with open('data') as file:
    solve(file.read())
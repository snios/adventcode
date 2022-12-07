def solve(data):
    divided_data = data.split('\n\n')
    move_data = divided_data[1].splitlines()
    lines = divided_data[0].splitlines()
    stack_count = (len(divided_data[0].splitlines()[0]) + 1) /4
    stacks = dict()
    for x in range(int(stack_count)):
        stacks[x+1] = list()
    for line in lines:
        line_pos = 0
        for x in range(int(stack_count)):
            item = line[line_pos:line_pos+3].strip()
            if len(item) == 3:
                stacks[x+1].append(item)
            line_pos += 4
    for move in move_data:
        split = move.split(' ')
        quantity = int(split[1])
        from_index = int(split[3])
        to_index = int(split[5])
        items_to_move = stacks[from_index][0:quantity]
        stacks[from_index] = stacks[from_index][quantity:]
        stacks[to_index][0:0] = items_to_move
    solution = ""
    for key in stacks:
        solution += stacks[key][0][1]
    print('answer: ', solution)
    
with open('data') as file:
    solve(file.read())
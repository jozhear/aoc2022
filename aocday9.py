# Second version.
# I truncated the code a bit to run more efficiently.
# Now the third function I wanted to create exists.
# I would still love to have the differences calculated in one place only, but that takes away the benefit of being able to run the third function
# regardless of what the outcomes of "difference_x" and "difference_y" are, since I can just swap them as I pass them in as arguments to the 
# tail_moving function.

# There's probably a way to truncate this even further, so I'll have to think about it.

all_positions=[]
answer_positions=[]

def tail_moving(difference1,difference2,tail1,tail2):
    if difference2 > 1 and difference1 == 0:
        tail1 += 1
    elif difference2 > 1 and difference1 == -1:
        tail1 +=1
        tail2 -=1
    elif difference2 > 1 and difference1 == 1:
        tail1 +=1
        tail2 +=1
    elif difference1 < -1 and difference2 == 0:
        tail1 -= 1
    elif difference1 < -1 and difference2 == -1:
        tail1 -=1
        tail2 -=1
    elif difference1 < -1 and difference2 == 1:
        tail1 -=1
        tail2 +=1
    return tail1,tail2

def movements(direction,x_head,y_head,x_tail,y_tail):
    compass = (direction.split(' '))[0]
    steps = int((direction.split(' '))[1])
    each_step = list(range(steps))
    if compass == 'U':
        for step in each_step:
            y_head += 1
            difference_x = x_head - x_tail
            difference_y = y_head - y_tail
            y_tail, x_tail = tail_moving(difference_x,difference_y,y_tail,x_tail)
            space = {}
            space['X'] = x_tail
            space['Y'] = y_tail
            all_positions.append(space)
        return x_head,y_head,x_tail,y_tail
    elif compass == 'D':
        for step in each_step:
            y_head -= 1
            difference_x = x_head - x_tail
            difference_y = y_head - y_tail
            y_tail, x_tail = tail_moving(difference_y,difference_x,y_tail,x_tail)
            space = {}
            space['X'] = x_tail
            space['Y'] = y_tail
            all_positions.append(space)
        return x_head,y_head,x_tail,y_tail
    elif compass =='R':
        for step in each_step:
            x_head += 1
            difference_x = x_head - x_tail
            difference_y = y_head - y_tail
            x_tail, y_tail = tail_moving(difference_y,difference_x,x_tail,y_tail)
            space = {}
            space['X'] = x_tail
            space['Y'] = y_tail
            all_positions.append(space)
        return x_head,y_head,x_tail,y_tail
    elif compass =='L':
        for step in each_step:
            x_head -= 1
            difference_x = x_head - x_tail
            difference_y = y_head - y_tail
            x_tail, y_tail = tail_moving(difference_x,difference_y,x_tail,y_tail)
            space = {}
            space['X'] = x_tail
            space['Y'] = y_tail
            all_positions.append(space)
        return x_head,y_head,x_tail,y_tail
        


def data():
    with open('day9.txt') as directions:
        directions = directions.readlines()
        x_head = 0
        y_head = 0
        x_tail = 0
        y_tail = 0
        for direction in directions:
            direction = direction.replace('\n','')
            x_head, y_head, x_tail, y_tail = movements(direction,x_head,y_head,x_tail,y_tail)
        for position in all_positions:
            if position not in answer_positions:
                answer_positions.append(position)
        print(len(answer_positions))
        
        
data()

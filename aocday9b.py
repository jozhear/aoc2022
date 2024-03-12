# This code is super long. I ran into an issue where I was trying to reuse the function 'segment_moving' on every piece of the tail, but that doesn't work.
# The segments don't move the same way. Segment 2 does, because Head can only move L, R, D, or U. Every other segment can move diagonally.
# Therefore after doing some experiments in Excel I realized that I can't evaluate segments past #2 based on the direction of the movement of the head.
# Sometimes, segments can move in another direction regardless of the direction of the head because they adjust to accommodate the diagonal movement
# of the piece in front of it.

# That guided my logic as I made assess_movement and ran it on a for loop of the segments that AREN'T segment # 2. These pieces would move in certain manners
# regardless of the direction of the head, so instead of feeding in the same parameters in different places as I did in the second version of my day 9 answer,
# I just fed in the same parameters in the same places. This made it work.

# I'm going to review some other people's code against mine to see how they did this and if it turned out as long as me. I got the right answer on my second
# try as I had a typo in the assess_movement and if I know anything it's that long, repetitive functions like assess_movement are prone to errors.

# There is probably a simpler way of doing this, so going to evaluate against some others and try and use that moving forward for the next question.

all_positions=[]
answer_positions=[]

def assess_movement(difference_x,difference_y,x,y):
    if difference_y > 1 and difference_x == 0:
        y += 1
    elif difference_y > 1 and difference_x <= -1:
        y +=1
        x -=1
    elif difference_y > 1 and difference_x >= 1:
        y +=1
        x +=1
    elif difference_x < -1 and difference_y == 0:
        x -= 1
    elif difference_x < -1 and difference_y <= -1:
        x -=1
        y -=1
    elif difference_x < -1 and difference_y >= 1:
        x -=1
        y +=1
    elif difference_y < -1 and difference_x == 0:
        y -=1
    elif difference_y < -1 and difference_x <=-1:
        y -=1
        x -=1
    elif difference_y < -1 and difference_x >=1:
        y -=1
        x +=1
    elif difference_x > 1 and difference_y == 0:
        x +=1
    elif difference_x > 1 and difference_y <= -1:
        x +=1
        y -=1
    elif difference_x > 1 and difference_y >=1:
        x +=1
        y +=1
    return x,y

def segment_moving(difference1,difference2,tail1,tail2):
    if difference2 > 1 and difference1 == 0:
        tail1 += 1
    elif difference2 > 1 and difference1 <= -1:
        tail1 +=1
        tail2 -=1
    elif difference2 > 1 and difference1 >= 1:
        tail1 +=1
        tail2 +=1
    elif difference1 < -1 and difference2 == 0:
        tail1 -= 1
    elif difference1 < -1 and difference2 <= -1:
        tail1 -=1
        tail2 -=1
    elif difference1 < -1 and difference2 >= 1:
        tail1 -=1
        tail2 +=1
    return tail1,tail2

def movements(direction,rope_segments):
    compass = (direction.split(' '))[0]
    steps = int((direction.split(' '))[1])
    each_step = list(range(steps))
    if compass == 'U':
        for step in each_step:
            rope_segments[0]['Y'] += 1
            segment = rope_segments[1]
            difference_x = rope_segments[0]['X'] - segment['X']
            difference_y = rope_segments[0]['Y'] - segment['Y']
            segment['Y'], segment['X'] = segment_moving(difference_x,difference_y,segment['Y'],segment['X'])
            i = 1
            for segment in rope_segments[2::]:
                difference_x = rope_segments[i]['X'] - segment['X']
                difference_y = rope_segments[i]['Y'] - segment['Y']
                segment['X'], segment['Y'] = assess_movement(difference_x,difference_y,segment['X'],segment['Y'])
                i+=1
                if segment['Segment'] == 'Tail':
                    coordinates = (segment['X'],segment['Y'])
                    all_positions.append(coordinates)
        return rope_segments
    elif compass == 'D':
        for step in each_step:
            rope_segments[0]['Y'] -= 1
            segment = rope_segments[1]
            difference_x = rope_segments[0]['X'] - segment['X']
            difference_y = rope_segments[0]['Y'] - segment['Y']
            segment['Y'], segment['X'] = segment_moving(difference_y,difference_x,segment['Y'],segment['X'])
            i = 1
            for segment in rope_segments[2::]:
                difference_x = rope_segments[i]['X'] - segment['X']
                difference_y = rope_segments[i]['Y'] - segment['Y']
                segment['X'], segment['Y'] = assess_movement(difference_x,difference_y,segment['X'],segment['Y'])
                i+=1
                if segment['Segment'] == 'Tail':
                    coordinates = (segment['X'],segment['Y'])
                    all_positions.append(coordinates)
        return rope_segments
    elif compass =='R':
        for step in each_step:
            rope_segments[0]['X'] += 1
            segment = rope_segments[1]
            difference_x = rope_segments[0]['X'] - segment['X']
            difference_y = rope_segments[0]['Y'] - segment['Y']
            segment['X'], segment['Y'] = segment_moving(difference_y,difference_x,segment['X'],segment['Y'])
            i = 1
            for segment in rope_segments[2::]:
                difference_x = rope_segments[i]['X'] - segment['X']
                difference_y = rope_segments[i]['Y'] - segment['Y']
                segment['X'], segment['Y'] = assess_movement(difference_x,difference_y,segment['X'],segment['Y'])
                i+=1
                if segment['Segment'] == 'Tail':
                    coordinates = (segment['X'],segment['Y'])
                    all_positions.append(coordinates)
        return rope_segments
    elif compass =='L':
        for step in each_step:
            rope_segments[0]['X'] -= 1
            segment = rope_segments[1]
            difference_x = rope_segments[0]['X'] - segment['X']
            difference_y = rope_segments[0]['Y'] - segment['Y']
            segment['X'], segment['Y'] = segment_moving(difference_x,difference_y,segment['X'],segment['Y'])
            i = 1
            for segment in rope_segments[2::]:
                difference_x = rope_segments[i]['X'] - segment['X']
                difference_y = rope_segments[i]['Y'] - segment['Y']
                segment['X'], segment['Y'] = assess_movement(difference_x,difference_y,segment['X'],segment['Y'])
                i+=1
                if segment['Segment'] == 'Tail':
                    coordinates = (segment['X'],segment['Y'])
                    all_positions.append(coordinates)
                    
        return rope_segments
    print(all_positions)


def data():
    with open('day9.txt') as directions:
        directions = directions.readlines()
        rope_segment = {}
        rope_segment['X'] = 0
        rope_segment['Y'] = 0
        rope_segment['Segment'] = 'Head'
        rope_segments = []
        rope_segments.append(rope_segment)
        for i in range(1,9):
            rope_segment = {}
            rope_segment['X'] = 0
            rope_segment['Y'] = 0
            rope_segment['Segment'] = i
            rope_segments.append(rope_segment)
        rope_segment = {}
        rope_segment['X'] = 0
        rope_segment['Y'] = 0
        rope_segment['Segment'] = 'Tail'
        rope_segments.append(rope_segment)
        for direction in directions:
            direction = direction.replace('\n','')
            updated_rope = movements(direction,rope_segments)
        for position in all_positions:
            if position not in answer_positions:
                answer_positions.append(position)
        print(answer_positions)
        print(len(answer_positions))
        
        
data()

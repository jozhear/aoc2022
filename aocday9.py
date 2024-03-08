# So I got the answer after about 3 hours or so of going over it.
# Initially I was having a hard time with the for loop in my movements function.
# My mindset here is to write GOOD code.
# I am looking at it, and I can see that my code really does the same thing each time in my compass directions.
# So I am going to make a quick self-challenge, and clean up my own code to use the tail_moving function I have defined there but didn't use.
# Originally i was going to upload only that version and not this long, untruncated one but I want to go get dinner and I think it'll be a good exercise.

# The funny thing too is if I would have done the third function right off the bat (i WAS thinking about it as I was sussing out the logic, but started thinking 'eh I'll just
# how far it takes me before I make a decision'. It became pretty clear as I defined the logic I could maek a third function) I would have probably solved it even faster?
# I ran into issues on those compass directions where I'd have a greater than backwards or an x_tail -=1 where it should be +=1, etc...

# The bottom line is I was able to figure out where the tail was going by thinking about the differences between the coordinates as the head would move apart from the tail.
# If the head is one square parallel, and two squares away on the same plane, it had to move diagonally.
# If it was moving in a straight line, the logic was quite straightforward.
# But I was having a hard time bootstrapping the code with the first breakdown of the 'compass' variable into directions.
# I really wanted to truncate my code, and I ended up not, but as stated above that's no problem. I'll clean it up and re-submit a _v2 sometime soon.
# overall, did not take me that long! Dictionaries have been my friend lately and I have a sneaky feeling knowing the coordinates of each movement will come in handy in
# 9b. 

# Once I got the list of dictionary objects, it was another for loop to append only unique items to the 'answer_positions' variable. Count it and got the answer first try!

all_positions=[]
answer_positions=[]

#def tail_moving(compass,step):
    #movement = step + 1

def movements(direction,x_head,y_head,x_tail,y_tail):
    compass = (direction.split(' '))[0]
    steps = int((direction.split(' '))[1])
    each_step = list(range(steps))
    if compass == 'U':
        for step in each_step:
            movement = step + 1
            y_head += 1
            difference1 = x_head - x_tail
            difference2 = y_head - y_tail
            if difference2 > 1 and x_head == x_tail:
                y_tail += 1
            elif difference2 > 1 and difference1 == -1:
                y_tail += 1
                x_tail -= 1
            elif difference2 > 1 and difference1 == 1:
                y_tail +=1
                x_tail +=1
            space = {}
            space['X'] = x_tail
            space['Y'] = y_tail
            all_positions.append(space)
        return x_head,y_head,x_tail,y_tail
    elif compass == 'D':
        for step in each_step:
            movement = step + 1
            y_head -= 1
            difference1 = x_head - x_tail
            difference2 = y_head - y_tail
            if difference2 < -1 and x_head == x_tail:
                y_tail -= 1
            elif difference2 < -1 and difference1 == -1:
                y_tail -=1
                x_tail -=1
            elif difference2 < -1 and difference1 == 1:
                y_tail -=1
                x_tail +=1
            space = {}
            space['X'] = x_tail
            space['Y'] = y_tail
            all_positions.append(space)
        return x_head,y_head,x_tail,y_tail
    elif compass =='R':
        for step in each_step:
            movement = step + 1
            x_head += 1
            difference1 = x_head - x_tail
            difference2 = y_head - y_tail
            if difference1 > 1 and y_head == y_tail:
                x_tail +=1
            elif difference1 > 1 and difference2 == -1:
                x_tail +=1
                y_tail -=1
            elif difference1 > 1 and difference2 == 1:
                x_tail +=1
                y_tail +=1
            space = {}
            space['X'] = x_tail
            space['Y'] = y_tail
            all_positions.append(space)
        return x_head,y_head,x_tail,y_tail
    elif compass =='L':
        for step in each_step:
            movement = step + 1
            x_head -= 1
            difference1 = x_head - x_tail
            difference2 = y_head - y_tail
            if difference1 < -1 and y_head == y_tail:
                x_tail -=1
            elif difference1 < -1 and difference2 == -1:
                x_tail -=1
                y_tail -=1
            elif difference1 < -1 and difference2 == 1:
                x_tail -=1
                y_tail +=1
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
            #print(x_head,y_head,x_tail,y_tail)
        for position in all_positions:
            if position not in answer_positions:
                answer_positions.append(position)
        print(len(answer_positions))
        
        
data()

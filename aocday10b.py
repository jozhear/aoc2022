# So I got the answer a little bit ago but wanted to clean my code up.
# As in some previous answers, I had a good deal of unwanted lines that were just repeating things that I could otherwise clean up with a third function.
# So I did, that's what the print_operation function is. Rather than just repeating everything, this gave me a super good opportunity to clean up as the same operation
# happened every single 'cycle' in the example.

# I'm pretty happy with how it turned out. Probably by most efficient code yet, which is great. I am understanding functions, how to pass in variables, etc very well.
# Managed to avoid any global variables this time too.

# Next time I really want to level up on classes, generators as well and start really leveraging some of the tougher Python things I have yet to fully understand.

def print_operation(cycle,x,answer,y):
    difference = cycle -x
    if difference <=1 and difference >= -1:
        answer[y] += '#'
    else:
        answer[y] += '.'
    cycle +=1
    if cycle > 39:
        y +=1
        cycle = cycle - 40
    return cycle,y

def cycle_perform(line,x,cycle,y,answer):
    if line[0] == 'a':
        line = line.split(' ')
        register = int(line[1])
        cycle,y = print_operation(cycle,x,answer,y)
        cycle,y = print_operation(cycle,x,answer,y)
        x += register
    else:
        cycle,y = print_operation(cycle,x,answer,y)
        
    return x,cycle,y

def data():
    with open('day10.txt') as f:
        answer = ['','','','','','']
        lines = f.readlines()
        x = 1
        cycle = 0
        y = 0
        for line in lines:
            line.replace('\n','')
            x,cycle,y = cycle_perform(line,x,cycle,y,answer)
        for row in answer:
            print(row)
data()

# This is the easiest one in a while. Took me about 40 minutes to do.
# The logic is simple, cycle has a value of 1. It goes up 1 for 'noop', and 2 for 'addx', but one at a time so it can add the value then check what 'cycle' is.
# if it's one of the values for cycle, it appends it to a list where it eventually adds to get the sum.
# I was having trouble because I had given cycle a value of 0 at the beginning when it really should be 1. Once I changed to 1, correct answer was given.

benchmarks = [20,60,100,140,180,220]
register_values = []
answer_strengths = []

def cycle_perform(line,x,cycle):
    if line[0] == 'a':
        line = line.split(' ')
        register = int(line[1])
        cycle +=1
        for iteration in benchmarks:
            if cycle == iteration:
                register_values.append(x)
        else:
            pass
        x += register
        cycle +=1
        for iteration in benchmarks:
            if cycle == iteration:
                register_values.append(x)
        else:
            pass
        return x,cycle
    else:
        cycle +=1
        for iteration in benchmarks:
            if cycle == iteration:
                register_values.append(x)
        else:
            pass
        x = x
        return x,cycle

def data():
    with open('day10.txt') as f:
        lines = f.readlines()
        x = 1
        cycle = 1
        for line in lines:
            line.replace('\n','')
            x,cycle = cycle_perform(line,x,cycle)
        y = 0
        for value in register_values:
            signal_strength = value * benchmarks[y]
            y +=1
            answer_strengths.append(signal_strength)
        answer = 0
        for strength in answer_strengths:
            answer = answer + strength
        print(answer)
data()

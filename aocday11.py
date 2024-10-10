# This was so much harder than previous, but I came into it with some momentum. I knew I wanted to do it correctly
# which is to say I wanted to make class objects of each monkey, then run the operations.

# This turned out to be super hard because I didn't fully understand how to nest functions in my class code. It took me
# FOREVER to figure out how I could create functions, and have them run based on the input to the class method (oldPlusNew, oldTimesNew, etc)
# Finally it occured to me that I could just map the functions outside of the class, then call them inside. This simplified things and got my momentum
# going when it came to monkeyDetermination and monkeyOperation. 

# I knew all I needed to do was make a determiniation on which monkey would have the object thrown to them, which I thought would be more complicated than it turned out being.
# Once I realized I could just return a tuple of ints, then feed those ints into the class call 'trueThrownList,falseThrownList,work[x].monkeyBusiness = work[x].monkeyTest(lines[y+1],work[x].monkeyStartingItems,work[x].monkeyBusiness)',
# I realized all I had to do was return the lists, modify the classes of monkey I grabbed with the ints from monkeyDetermination, then clear the list of the monkey throwing stuff.
# This was encouraging, as this all worked, and I was getting a list of 8 monkeys who carried 36 objects.

# However I realized I didn't even read the part where I was supposed to be calculating monkeyBusiness which is essentially an operation counting how many times each monkey
# looks at an item and eventually throws it. Luckily this turned out to be easy and a sign of my growing confidence with classes, functions, and returning function values.
# All I had to do was make a self.monkeyBusiness class, then feed that int of 0 into my monkeyTest function, adding every time the for loop went over the list of items.
# I returned the value and got a number that looked promising. Put it in, and correct! :D 

def startingItems(lines):
    itemList = lines.replace('\n','').replace(' ','').replace('Startingitems:','').split(',')
    itemList = list(map(int, itemList))
    return itemList

def oldPlusNew(number,old):
    new = number + old
    return new
    
    
def oldTimesNew(number,old):
    new = number * old
    return new
    
def oldSquared(old):
    new = old ** 2
    return new

def monkeyDetermination(trueMonkey,falseMonkey):
    trueLineSplit = trueMonkey.split(' ')
    falseLineSplit = falseMonkey.split(' ')
    trueMonkey = int(trueLineSplit[9])
    falseMonkey = int(falseLineSplit[9])
    return trueMonkey,falseMonkey
    

class monkey():
    def __init__(self,monkeyNumber,monkeyStartingItems,monkeyDetermination,monkeyBusiness):
        self.monkeyNumber = monkeyNumber
        self.monkeyStartingItems = monkeyStartingItems
        self.monkeyDetermination = monkeyDetermination
        self.monkeyBusiness = monkeyBusiness
        
    def monkeyOperation(self,lines,startingItems):
        lineSplit = lines.split(' ')
        operand = lineSplit[6]
        number = lineSplit[7]
        i = 0
        if number != 'old\n':
            number = int(number)
            if operand == "+":
                for old in startingItems:
                    old = oldPlusNew(number,old)
                    startingItems[i] = old
                    i +=1
            elif operand == "*":
                for old in startingItems:
                    old = oldTimesNew(number,old)
                    startingItems[i] = old
                    i +=1
        else:
            for old in startingItems:
                old = oldSquared(old)
                startingItems[i] = old
                i +=1
        return startingItems
    
    def monkeyTest(self,lines,startingItems,monkeyBusiness):
        lineSplit = lines.split(' ')
        divisor = lineSplit[5]
        divisor = int(divisor)
        trueMonkeyList = []
        falseMonkeyList = []
        for number in startingItems:
            monkeyBusiness += 1
            number = int(float((number) / 3))
            if number % divisor == 0:
                trueMonkeyList.append(number)
            else:
                falseMonkeyList.append(number)
        return trueMonkeyList,falseMonkeyList,monkeyBusiness
        
def data():
    with open('day11.txt') as f:
        lines = f.readlines()
        work = []
        x = 0
        y = 2
        z = 0
        multipliedBusiness = []
        for i in range(0, len(lines), 7):
            big_monkey = monkey(lines[i][7],startingItems(lines[i+1]),monkeyDetermination(lines[i+4],lines[i+5]),0)
            work.append(big_monkey)
        for x in range(0,20):
            for x in range(0, 8):
                a = work[x].monkeyDetermination[0]
                b = work[x].monkeyDetermination[1]
                trueMonkeyList = work[a].monkeyStartingItems
                falseMonkeyList = work[b].monkeyStartingItems
                work[x].monkeyStartingItems = work[x].monkeyOperation(lines[y],work[x].monkeyStartingItems)
                trueThrownList,falseThrownList,work[x].monkeyBusiness = work[x].monkeyTest(lines[y+1],work[x].monkeyStartingItems,work[x].monkeyBusiness)
                trueMonkeyList = trueMonkeyList + trueThrownList
                falseMonkeyList = falseMonkeyList + falseThrownList
                work[a].monkeyStartingItems = trueMonkeyList
                work[b].monkeyStartingItems = falseMonkeyList
                work[x].monkeyStartingItems = []
                #print(work[a].monkeyStartingItems,work[b].monkeyStartingItems)
                y += 7
            y = 2
        for x in range(0, 8):
            multipliedBusiness.append(work[x].monkeyBusiness)
        multipliedBusiness.sort(reverse=True)
        answer = multipliedBusiness[0] * multipliedBusiness[1]
        print(multipliedBusiness)
        print(answer)
        
data()

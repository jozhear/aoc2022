# Ridiculously hard. I had to look up the math because I had no idea how a number could become 'smaller' yet operate the same through
# each of the inspection operations.

# This link helped me out a lot; https://aoc.just2good.co.uk/2022/11.html#part-2

# First super intense math question, but that's all good to me. Here to learn! Now I know if I need to divide numbers a lot and keep numbers
# reasonable, this is a good place to start. In the end, I only needed to add a function to determine the number of all divisors multiplied together,
# then just add one line of code to the monkeyTest where it finds the remainder of the worry score over the divisorProduct. Code works fast too, even with 10k runs.

def getDivisorProduct(lines):
    divisor = int(lines.replace('\n','').replace(' ','').replace('Test:divisibleby',''))
    return divisor

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
    
    def monkeyTest(self,lines,startingItems,monkeyBusiness,divisorProduct):
        lineSplit = lines.split(' ')
        divisor = lineSplit[5]
        divisor = int(divisor)
        trueMonkeyList = []
        falseMonkeyList = []
        for number in startingItems:
            newNumber = number % divisorProduct
            monkeyBusiness += 1
            if newNumber % divisor == 0:
                trueMonkeyList.append(newNumber)
            else:
                falseMonkeyList.append(newNumber)
        return trueMonkeyList,falseMonkeyList,monkeyBusiness
        
def data():
    with open('day11.txt') as f:
        lines = f.readlines()
        work = []
        y = 2
        divisorList = []
        multipliedBusiness = []
        for i in range(0, len(lines), 7):
            big_monkey = monkey(lines[i][7],startingItems(lines[i+1]),monkeyDetermination(lines[i+4],lines[i+5]),0)
            work.append(big_monkey)
            divisorList.append(getDivisorProduct(lines[i+3]))
        divisorProduct = 1
        for x in divisorList:
            divisorProduct = divisorProduct * x
        for x in range(0,10000):
            for x in range(0, 8):
                a = work[x].monkeyDetermination[0]
                b = work[x].monkeyDetermination[1]
                trueMonkeyList = work[a].monkeyStartingItems
                falseMonkeyList = work[b].monkeyStartingItems
                work[x].monkeyStartingItems = work[x].monkeyOperation(lines[y],work[x].monkeyStartingItems)
                trueThrownList,falseThrownList,work[x].monkeyBusiness = work[x].monkeyTest(lines[y+1],work[x].monkeyStartingItems,work[x].monkeyBusiness,divisorProduct)
                trueMonkeyList = trueMonkeyList + trueThrownList
                falseMonkeyList = falseMonkeyList + falseThrownList
                work[a].monkeyStartingItems = trueMonkeyList
                work[b].monkeyStartingItems = falseMonkeyList
                work[x].monkeyStartingItems = []
                y += 7
            y = 2
        for x in range(0, 8):
            multipliedBusiness.append(work[x].monkeyBusiness)
        multipliedBusiness.sort(reverse=True)
        answer = multipliedBusiness[0] * multipliedBusiness[1]
        print(multipliedBusiness)
        print(answer)
        
data()

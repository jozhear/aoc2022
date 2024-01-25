# Had to review another person's code to really get the two functions across.
# I really wanted to have some code that uses two functions so I could drive this home for myself.
# The first function defines the logic, establishing elf1 and elf2 as the parameters to be passed in.
# The second function defines the split of the strings so that I can run the function across 
# each line in a for loop. I define the variables elf1 and elf2 as a tuple of integers after I've split them,
# then pass in those variables to the function checkForOverlap as arguments.
# Then it works!

def checkForOverlap(elf1,elf2):
    if elf1[0] >= elf2[0] and elf1[0] <= elf2[1]:
        return True
    elif elf2[0] >= elf1[0] and elf2[0] <= elf1[1]:
        return True
    elif elf1[1] >= elf2[0] and elf1[1] <= elf2[1]:
        return True
    elif elf2[1] >= elf1[0] and elf2[1] <= elf1[1]:
        return True
        
    
def splitUpElves():
    total=0
    with open('day4b.csv') as groups:
        for line in groups.readlines():
            elves = line.replace('-',' ').replace(',',' ').split( )
            elf1 = int(elves[0]),int(elves[1])
            elf2 = int(elves[2]),int(elves[3])
            if checkForOverlap(elf1,elf2):
                total +=1
        return total
splitUpElves()

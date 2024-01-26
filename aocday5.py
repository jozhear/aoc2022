# I made a lot of notes here initially but the bottom line is this.
# Once I was able to extract the data I needed from the spreadsheet the logic was pretty complex.
# Instead of making a grid like was my previous idea, I just made strings for each tower. I did it backwards in the first 
# for loop in boxes() because I wanted the "top" of each tower to be the LAST character.

# From there, the logic was essentially to run the lifts function on each movement in the spreadsheet.
# I had to extract the data I needed and modify the integers to match the python data (aka, 1 really being 0 for
# tower values.

# One caveat in my logic was that if the length of a string was less than x, the emptyBox variable would be empty.
# As a result my script wouldn't work. So I had to nest an if statement to say if that's the case, just flip
# the string, and if it's not, do the normal function and grab the few characters you need to define emptyBox.

# Updating the towers was a matter of assigning oldTower to tower y, newTower to tower z, then updating after I had done
# my concatenations / replacements.

# One good thing to know is that replace has a counter in it. I was running into issues where if an emptyBox occured
# twice in a tower, it would take too much from the oldTower. This was resolved by flipping oldTower, running the replace
# on the first counter (the top of the tower) then flipping it to be back to normal.

# Overall, significantly harder than previous problems BUT I did not have to look up anyone else's code to do it. :)

# I could probably update some of the variables to be dynamic but for now just going to put what I got to get this to work.

def lifts(towers,x,y,z):
    oldTower = towers[y]
    newTower = towers[z]
    emptyBox = ''
    a = len(oldTower)
    if a - x == -1:
        emptyBox = oldTower[::-1]
    else:
        emptyBox = oldTower[:len(oldTower)-x:-1]
    oldTower = oldTower[::-1]
    oldTower = oldTower.replace(emptyBox,'',1)
    oldTower = oldTower[::-1]
    newTower = newTower + emptyBox
    towers[y] = oldTower
    towers[z] = newTower
    print(towers)
    return towers
            
def boxes():
    with open('day5.csv') as boxes:
        towers=['','','','','','','','','']
        lines = boxes.readlines()
        x = 0
        for line in lines[7::-1]:
            for character in line[1::4]:
                towers[x] = towers[x] + character
                towers[x] = towers[x].strip()
                x+=1
            x = 0
        for line in lines[10::]:
            numbers = line.split(' ')
            numbers.remove('move')
            numbers.remove('from')
            numbers.remove('to')
            x = int(numbers[0]) + 1
            y = int(numbers[1]) - 1
            z = int(numbers[2]) - 1
            lifts(towers,x,y,z)
        return towers
    
boxes()

# One single function to do this all for now.
# I will probably make it better tomorrow. Was ripping my hair out getting the wrong answers even though I was confident I had
# built the code correctly, even if it isn't optimal or glamorous (though I did aim to truncate it more than my previous solutions).
# Ultimately, I wasn't casting the value for elves to an int and was getting wrong answers because of it. Could not for the
# life of me figure out why I was getting it wrong until I tested my elves variable and noticed the quotes between each value.
# Once I casted them to ints instead of leaving them as what they were (strings) my logic worked and I got the right answer.


def splitUpElves():
    total = 0
    with open('day4.csv') as groups:
        for line in groups.readlines():
          # This function changes the lines from the input into the strings they are and casts them to a list that's easy to work with.
            elves = line.replace('-',' ').replace(',',' ').split( )
          # Then it's just a matter of defining the logic. The first value will always be less than or equal to the second value. Then it's just a matter 
          # of determining if they match the criteria; first value smaller than or equal to third value, and second value greater than or equal to fourth value,
          # and great than or equal to third value. (IE, 1-99,2-98 = good).
            if int(elves[0]) <= int(elves[2]) and int(elves[1]) >= int(elves[3]) and int(elves[1]) >= int(elves[2]):
                print(elves[0],elves[1],elves[2],elves[3])
                total+=1
          # Same logic but on the inverse. Each condition adds 1 to my total variable which is the end result. If there's no match, I don't define any logic
          # and it just continues moving through the for loop.
            elif int(elves[2]) <= int(elves[0]) and int(elves[3]) >= int(elves[1]) and int(elves[3]) >= int(elves[0]):
                print(elves[0],elves[1],elves[2],elves[3])
                total+=1
            
        return total
                        
splitUpElves()

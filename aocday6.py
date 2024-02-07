# I had a great start to this one but ended up having to look up someone else's code to finish it.
# It didn't take me long to get my logic correct, but the caveat is that I was returning previous_chars from the find_marker function
# instead of the output that actually mattered; a boolean that basically was a switch for the data() function to tell it to keep looping or not.

# Once I realized that my goal was to determine the output of the find_marker function as a boolean versus focusing on feeding characters back out of it,
# it was a simple matter of doing an if statement and seeing whether the output of the find_marker function on the set of characters being fed in as the 
# previous_chars parameter was true or not.

# Then I got the answer :) 

def find_marker(previous_chars):
    for letter in previous_chars:
        if len(previous_chars) < 4:
            keep_looping = True
            return keep_looping
            break
        elif previous_chars.count(letter) == 1:
            pass
        elif previous_chars.count(letter) >= 2:
            keep_looping = True
            return keep_looping
            break
    else:
        keep_looping = False
        return keep_looping

def data():
    with open('day6.csv') as f:
        lines = f.readlines()
        data = lines[0]
        x=0
        previous_chars = ''
        for char in data:
            previous_chars = previous_chars + char
            if len(previous_chars) > 4:
                firstChar = previous_chars[0]
                previous_chars = previous_chars.replace(firstChar,'',1)
            x+=1
            if find_marker(previous_chars) == True:
                pass
            elif find_marker(previous_chars) == False:
                break
        return x
data()

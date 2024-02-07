# Literally took me about 30 seconds, easily the fastest answer I've ever contributed.
# I Guess i built it right the first time around because it was literally a matter of changing the length of previous chars
# in both of these functions to 14 instead of 4.
# If I had used a global variable (which I probably should since it's the same regardless of the function) it would have taken me 
# in theory even less time lol. 

def find_marker(previous_chars):
    for letter in previous_chars:
        if len(previous_chars) < 14:
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
            if len(previous_chars) > 14:
                firstChar = previous_chars[0]
                previous_chars = previous_chars.replace(firstChar,'',1)
            x+=1
            if find_marker(previous_chars) == True:
                pass
            elif find_marker(previous_chars) == False:
                break
        return x
data()

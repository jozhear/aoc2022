# The logic took me a little bit to figure out.
# I was a little burnt out after I finished question 7 and then cranked out 7b and 8.
# Ultimately it was not that hard, just had to compare the current value being passed through the for loop
# with what was around it on both sides.
# This was done using string manipulation and then a nested for loop.
# I had the code to build the vertical rows from 8b, which makes this question a little unique as the rest of the code 
# was not used at all.
# Initially I was going to run the same function on the vertical rows when I realized I could make things a little simpler by just finding the tree
# I want in the vertical function and doing the multiplication there.

# The code actually takes a good handful of seconds to run, so I think at some point I'd like to revisit this and optimize it a bit.
# Regardless I got the answer on the first try, was a pretty fun question actually.


all_trees=[]
list_of_scores=[]


def get_score_hori(line,y):
    x = 0
    for tree in line:
        left_multiplier = 0
        right_multiplier = 0
        right_string = line[x::1]
        left_string = line[x::-1]
        new_right_string = right_string.replace(right_string[0],'', 1)
        new_left_string = left_string.replace(left_string[0],'', 1)
        for comparisons in new_right_string:
            tree = int(tree)
            comparisons = int(comparisons)
            if tree > comparisons:
                right_multiplier += 1
            else:
                right_multiplier +=1
                break
        for comparisons in new_left_string:
            tree = int(tree)
            comparisons = int(comparisons)
            if tree > comparisons:
                left_multiplier +=1
            else:
                left_multiplier +=1
                break
        multiplier = right_multiplier * left_multiplier
        tree_with_coords = {}
        tree_with_coords['Coordinates'] = (x,y)
        tree_with_coords['Multiplier'] = multiplier
        all_trees.append(tree_with_coords)
        x+=1

def get_score_vert(line,x):
    y = 0
    for tree in line:
        up_multiplier = 0
        down_multiplier = 0
        down_string = line[y::1]
        up_string = line[y::-1]
        new_down_string = down_string.replace(down_string[0],'', 1)
        new_up_string = up_string.replace(up_string[0],'', 1)
        for comparisons in new_down_string:
            tree = int(tree)
            comparisons = int(comparisons)
            if tree > comparisons:
                down_multiplier +=1
            else:
                down_multiplier +=1
                break
        for comparisons in new_up_string:
            tree = int(tree)
            comparisons = int(comparisons)
            if tree > comparisons:
                up_multiplier +=1
            else:
                up_multiplier +=1
                break
        multiplier = down_multiplier * up_multiplier
        coordinates = (x,y)
        for tree in all_trees:
            if tree['Coordinates'] == coordinates:
                new_multiplier = multiplier * tree['Multiplier']
                tree['Multiplier'] = new_multiplier
                list_of_scores.append(new_multiplier)
        y+=1

        
def data():
    with open('day8.txt') as lines:
        lines = lines.readlines()
        y = 0
        up_to_down = ''
        for line in lines:
            line = line.replace('\n','')
            get_score_hori(line,y)
            y +=1
        y = 0
        for x in range (0,99):
            for line in lines:
                up_to_down = up_to_down + line[x]
            get_score_vert(up_to_down,x)
            up_to_down = ''
        sorted_scores = sorted(list_of_scores)
        final_answer = sorted_scores[::-1][0]
        print(final_answer)
            
data()

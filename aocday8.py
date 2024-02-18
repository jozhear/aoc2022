# significantly easier than the last one and in total only took me about 2.5 hours to do.
# I am definitely improving at python! :D 

# The strategy here was more obvious than the last one, I would just have to enumerate across each row forwards and backwards
# and run a basic check as I appended trees in that row to a new list, checking for the height of the current tree against
# trees in the row.

# The caveat was just enumerating in a backwards direction which I found online and could be done using the itertools
# command. 

# I also had a bit of a hard time concatenating the column trees, but I realized after it was because I never exported 
# day8.tst to the lines variable properly (lines.readlines())
# Once that was done I figured out that a nested for loop would work to 'create' these new
# rows from 0-99. 

# Then I just ran a slightly modified version of the original function on it, swapping values for X and Y
# so that I could get the proper values when I appended to my tree list.

# Then simple deduplication function and then get answer!

import itertools

all_trees=[]
answer_trees=[]

def find_tree_hori(line,y):
    checking_height = [-1]
    tree = (list(enumerate(line)))
    for x,height in tree:
        height = int(height)
        tallest_trees = (sorted(checking_height, reverse=True))
        if height > tallest_trees[0]:
            new_tree=(x,y)
            all_trees.append(new_tree)
        checking_height.append(height)
    checking_height = []
    line = line[::-1]
    checking_height = [-1]
    tree = list(zip(itertools.count(98,-1), line))
    for x,height in tree:
        height = int(height)
        tallest_trees = (sorted(checking_height, reverse=True))
        if height > tallest_trees[0]:
            new_tree=(x,y)
            all_trees.append(new_tree)
        checking_height.append(height)
    checking_height = []
    
def find_tree_vert(line,x):
    checking_height = [-1]
    tree = (list(enumerate(line)))
    for y,height in tree:
        height = int(height)
        tallest_trees = (sorted(checking_height, reverse=True))
        if height > tallest_trees[0]:
            new_tree=(x,y)
            all_trees.append(new_tree)
        checking_height.append(height)
    checking_height = []
    line = line[::-1]
    checking_height = [-1]
    tree = list(zip(itertools.count(98,-1), line))
    for y,height in tree:
        height = int(height)
        tallest_trees = (sorted(checking_height, reverse=True))
        if height > tallest_trees[0]:
            new_tree=(x,y)
            all_trees.append(new_tree)
        checking_height.append(height)
    checking_height = []
    
def data():
    with open('day8.txt') as lines:
        lines = lines.readlines()
        y = 0
        up_to_down = ''
        for line in lines:
            line = line.replace('\n','')
            find_tree_hori(line,y)
            y +=1
        y = 0
        for x in range (0,99):
            for line in lines:
                up_to_down = up_to_down + line[x]
            find_tree_vert(up_to_down,x)
            up_to_down = ''
        for tree in all_trees:
            if tree not in answer_trees:
                answer_trees.append(tree)
        print(len(answer_trees))

                

            
data()

# This was the hardest question so far by far. But part of the reason was I implemented a self-challenge where I would not look at others code while trying to do this and just try and do only my own code and get the ideas myself.
# I didn't limit myself to not googling because this was the first time I was working with dictionaries really. So there were a few things I needed to know.
# I don't feel guilty about that because the built in documentation in python isn't like Powershell's.

# It took me a long time to figure out how to do this but I eventually realized I needed to make a dictionary object.
# I needed objects that could have a name, the items within it, a size, and a level.
# First 'eureka' moment came when I looked at the question again and they referred to finding another directory as by name and level, so I figured it'd make sense to do the same thing.

# Lots of caveats though. I realized that the values were going through every folder before moving to the next one, and would always go to the first folder in the list of folders so
# I used that to my advantage when defining 'current_directory'. Even though there were multiple folders with the same name and level, you would ALWAYS go sooner to the most 
# recent one you created so indexing in reverse at the first value worked there. That was one of the huge challenges, I could figure out what to do for the rest but 
# was constantly overthinking 'cd..'

# The other was when I realized I had to put the current_directory definition in the if handlers, I wanted to only define it once but that messed things up when changing
# directories as I was looking for a value of level that was basically wrong. Changing the level before I looked for current_directory didn't matter and made it easier.

# Then came defining the size which came with a good set of challenges. I could add the values of files to the size easily enough, but when it came to adding the 
# size of the subfolders to the parent folders I had a really hard time. Eventually I figured out how to break down my huge list of directories into just dictionaries 
# and integers, and once I was able to only grab dictionaries and do work to them, it worked; I also had to go in reverse because I knew the sub folders were always added 
# last and I needed their values to be added first so that the parent folders would always get the most recent value of size.

# Then... it worked. Finally.

# I also learned while doing this from a colleague that there is an os walk function that probably would have saved hours, but it's okay, I learned so much doing it
# this way that it was completely worth it. I am hoping the next few questions will be easier :) 


list_of_directories = []

def create_directory(line,level,directory_string):
    values = line.split(' ')
    if values[1] == 'ls':
        level +=0
        return level, directory_string
    if values[0] == 'dir':
        directory_name = values[1]
        new_directory = {}
        new_directory['Directory'] = directory_name
        new_directory['Level'] = level
        new_directory['Items'] = []
        new_directory['Size'] = 0
        list_of_directories.append(new_directory)
        current_directory = [directory for directory in list_of_directories if directory['Directory'] == directory_string and directory['Level'] == (level -1)][::-1][0]
        current_directory['Items'].append(new_directory)
        return level, directory_string
    elif values[1] == 'cd' and values[2] != '..':
        directory_string = values[2]
        level +=1
        return level, directory_string
    elif values [1] == 'cd' and values[2] == '..':
        level -=1
        return level, directory_string
    else:
        current_directory = [directory for directory in list_of_directories if directory['Directory'] == directory_string and directory['Level'] == (level -1)][::-1][0]
        current_directory['Items'].append(int(values[0]))
        current_directory['Size'] = current_directory['Size'] + int(values[0])
        level +=0
        return level, directory_string
    
def calculate_size(directory):
    items = directory['Items']
    for item in items:
        if isinstance(item, dict):
            directory['Size'] = directory['Size'] +item['Size']
        else:
            pass
        
def get_sum(directory,answer):
    size = directory['Size']
    if size <= 100000:
        answer += size
        return answer
    else:
        return answer
    
    
def data():
    with open('day7.txt') as f:
        lines = f.readlines()
        level = 0
        answer = 0
        root = {}
        root['Directory'] = '/'
        root['Level'] = 0
        root['Items'] = []
        root['Size'] = 0
        list_of_directories.append(root)
        directory_string = '/'
        for line in lines:
            line = line.replace('\n','')   
            level, directory_string = create_directory(line,level,directory_string)
        for directory in list_of_directories[::-1]:
            calculate_size(directory)
        for directory in list_of_directories:
            answer = get_sum(directory,answer)
        print(answer)
data()

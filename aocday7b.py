# Did not take long, I just had to figure out the logic.
# Subtracting the directory size from root must equal less than 40,000,000.
# Once I was able to figure that out it was not hard to implement, just had to sort the answer and give me the lowest value possible.
# Answer was right on first try.

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
        
def get_smallest_directory(directory):
    size = list_of_directories[0]['Size'] - directory['Size']
    if size <= 40000000:
        return directory['Size']
    
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
        answers = []
        for directory in list_of_directories:
            if (get_smallest_directory(directory)) != None:
                answers.append(get_smallest_directory(directory))
        final_answer = sorted(answers)[0]
        print(final_answer)
data()

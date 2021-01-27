import os

# This is pretty neat! We can print the directories, it outputs a list of the names!
# and it includes file names in that directory as well.

# os.listdir('/') prints the directory names from the root directory. Even in windows!

def print_directories():
    dirNames = os.listdir('/')
    print(dirNames)

if __name__ == '__main__':
    print_directories()


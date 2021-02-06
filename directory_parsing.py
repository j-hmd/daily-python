import os


"""
Prints directories from the repository root.
"""
def get_directories(dirPath):
    dirs = []
    with os.scandir(path=dirPath) as it:
        for entry in it:
            if not entry.name.startswith('.') and entry.is_dir():
                dirs.append(entry)

    return dirs
    
if __name__ == '__main__':
    get_directories('.')


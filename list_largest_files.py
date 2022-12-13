# To list largest files in computer

import os
import pandas as pd
import numpy as np

print()
print()
print(f"BOT: Hello User! So how many large files do you want to see? (use 'all' to see all files)")
HEAD = input("YOU: ")

def main():
    
    dirName = os.getcwd()

    listOfFiles = list()

    try:
        for (absPath, dirnames, filenames) in os.walk(dirName): 

            dirpath = os.path.relpath(absPath)

            listOfFiles += [os.path.join(dirpath, file) for file in filenames]    
            file_list = []

    except FileNotFoundError:
        pass

    try:
        for file_name in listOfFiles:

            file_stats = os.stat(file_name)
            file_storage = file_stats.st_size / (1024 * 1024)    
            # relative_paths = [os.path.relpath(path, common_prefix) for path in paths]
            head, tail = os.path.split(file_name)

            file_list += [(tail, head, file_storage)] 
    except FileNotFoundError:
        pass

    SIZE_COLUMN_NAME = 'size (mb)'

    df = pd.DataFrame(file_list, columns=['Name', 'File Directory',  SIZE_COLUMN_NAME])
    df.reset_index(drop=True, inplace=True)

    # df[SIZE_COLUMN_NAME].apply(np.ceil)

    # df[SIZE_COLUMN_NAME] = df[SIZE_COLUMN_NAME].round(decimals=3)

    print()
    if str(HEAD) == "all":
        print(df.sort_values(by=SIZE_COLUMN_NAME, ascending=False).to_string(index=False))
    else:
        print(df.sort_values(by=SIZE_COLUMN_NAME, ascending=False).head(int(HEAD)).to_string(index=False))

    print()
    print()

main()

print(f'BOT: Ok,  I have accomplished your task, now Bye!')

print()
print()

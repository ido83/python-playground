import json
import os, sys
from os import listdir
from os.path import isfile, join

def get_list_of_files():
     print()

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    json_obj = {}
    json_obj['files'] = []
    mypath = "/Users/idonadler/Downloads"
    onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    for file in onlyfiles:
        json_obj['files'].append({
            'name': file,
            'path': os.path.abspath(file)
        })
    # Write the object to file.
    with open('example.json', 'w') as jsonFile:
        json.dump(json_obj, jsonFile)

import re

def has_numbers(inputString):#check if string have numbers
    return bool(re.search(r'\d', inputString))


def print_duplicates(string):#print duplicates
    for i in range(0, len(string),2):
        if i == len(string) - 1 or string[i] == string[i+1]:
            print(string[i],string[i+1])
    return string

def insert_X_duplicates(string):
    for i in range(0, len(string),2):
        if i == len(string) - 1 or string[i] == string[i+1]:
            string = string[:i+1] + 'X' + string[i+1:]
    return string

def remove_equal(string:str):
    if(string[-1]=="="):
        return string.replace("=","//XX///")
    return string
def replace_equal(string:str):
    if string.endswith("//XX///"):
        return string.replace("//XX///", "=")
    else:
        return string
def insert_X_Audio_duplicates(string):
    for i in range(0, len(string),7):
        if i == len(string) - 1 or string[i] == string[i+1]:
            string = string[:i+1] + "//X///" + string[i+1:]
    return string
def insert_X_Image_duplicates(string):
    for i in range(0, len(string),6):
        if i == len(string) - 1 or string[i] == string[i+1]:
            string = string[:i+1] + "//X/" + string[i+1:]
    return string
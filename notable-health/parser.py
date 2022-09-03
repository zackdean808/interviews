#!/bin/python3


import os
import sys
import argparse
import re 


def append_number_n(numbered_list):
    return 0 

def append_number_next(numbered_list):
    return 0 

def clean_up():
    os.remove("cleaned")

def prep_file_for_splitting():
    # open file for reading 
    with open(sys.argv[1], 'r') as file:
        fd = file.read()

    # since I don't know where the line breaks are, I need to conver them to spaces
    fd = fd.replace('\n', ' ')

    # write cleaned file for splitting 
    with open('cleaned', 'w') as file:
        file.write(fd) 
    
    print("File written")



if __name__ == "__main__":
    #main goes here 
    # 1. read in file 
    # 2. split text from start to '.' append to list 
    # 3. parse item in list
    # 4. make decision on time in list 


    # ignoring case seems wise. 
    re_number_n = re.compile('Number (one|two|three|four|five|six|seven|eight|nine)\.$', re.IGNORECASE)
    re_number_next = re.compile('Number next\.$', re.IGNORECASE)
    re_split_text = re.compile('/.+?\./')
    split_text = []
    final_list = [] 

    # send remove newline characters
    prep_file_for_splitting()

    # split file into lines on the period 
    





    # clean up 
    clean_up()




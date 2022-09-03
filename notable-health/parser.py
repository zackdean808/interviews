#!/bin/python3


import os
import sys
import argparse
import re
from typing import final 


def insert_at_number_n(numbered_list):
    print ("insert_at_number_n")
    print (numbered_list)

def append_number_next(numbered_list):
    print ("append_number_next")
    print (numbered_list)

def clean_up():
    os.remove("cleaned")
    os.remove("final")

def remove_bad_line_breaks():
    # open file for reading 
    with open(sys.argv[1], 'r') as file:
        fd = file.read()

    # since I don't know where the line breaks are, I need to conver them to spaces
    fd = fd.replace('\n', ' ')

    # write cleaned file for splitting 
    with open('cleaned', 'w') as file:
        file.write(fd) 

def insert_new_line_breaks():
    # open file for reading 
    with open(sys.argv[1], 'r') as file:
        fd = file.read()

    # Assume '.' means end of line 
    fd = fd.replace('.', '\n')

    # write cleaned file for splitting 
    with open('final', 'w') as file:
        file.write(fd) 
    

if __name__ == "__main__":
    #main goes here 
    # 1. read in file 
    # 2. split text from start to '.' append to list 
    # 3. parse item in list
    # 4. make decision on time in list 


    # ignoring case seems wise. 
    re_number_n = re.compile('Number\s(one|two|three|four|five|six|seven|eight|nine)', re.IGNORECASE)
    re_number_next = re.compile('Number next', re.IGNORECASE)
    re_split_text = re.compile('/.+?\./')
    split_text = []
    final_list = [] 

    # send remove newline characters
    remove_bad_line_breaks()

    # split file into lines on the period
    # TODO: there is abug in this where the line breaks aren't clean, but deal with later
    insert_new_line_breaks()


    with open('./final','r') as file: 
        lines = file.readlines()

        for l in lines:
            # print (l)
            if re_number_n.search(l):
                insert_at_number_n(l)
            if re_number_next.search(l):
                append_number_next(l)



    # clean up 
    clean_up()




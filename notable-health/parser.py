#!/bin/python3


import os
import sys
import argparse
import re 


def append_number_n(numbered_list):
    return 0 

def append_number_next(numbered_list):
    return 0 


if __name__ == "__main__":
    #main goes here 
    # 1. read in file 
    # 2. parse for text "number [1-9]" capture until '.' 
    #   2a. Insert in list at that point 
    # 3. parse for text "number next" capture until '.'
    #   3a. Append line to list  
    # I know I should put this else where but it's a quick note

    # ignoring case seems wise. 
    re_number_n = re.compile('Number (one|two|three|four|five|six|seven|eight|nine)\.$', re.IGNORECASE)
    re_number_next = re.compile('Number next\.$', re.IGNORECASE)


    with open(sys.argv[1], 'r') as file:
        lines = file.readlines()

        for l in lines:
            if re_number_n.match(l):
                print ("number n")
            if re_number_next.match(l):
                print ("number next")
            else:
                print ("no match")

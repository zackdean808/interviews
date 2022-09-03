#!/bin/python3


import os
import sys
import argparse
import re 






if __name__ == "__main__":
    #main goes here 
    # 1. read in file 
    # 2. parse for text "number [1-9]" capture until '.' 
    #   2a. Insert in list at that point 
    # 3. parse for text "number next" capture until '.'
    #   3a. Append line to list  
    # I know I should put this else where but it's a quick note

    with open(sys.argv[1], 'r') as file:
            print(file.read())
    

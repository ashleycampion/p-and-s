# Write a program that reads in a text file 
# and outputs the number of e's it contains. 
# The program should take the filename 
# from an argument on the command line.

# to read filename from command line one
# can use sys.argv from sys module, which
# is a list containing the command line arguments.
# sys.argv[1] refers to the first argument after
# the name of the python script to be run itself.

import sys

# use "with... as variable" syntax to ensure 
# file is closed after being read.
with open(sys.argv[1], 'r') as f:
    # read from file and count number of "e"s
    print(f.read().count("e"))
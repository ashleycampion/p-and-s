# Write a program that reads in a text file
# and outputs the number of e's it contains.
# The program should take the filename
# from an argument on the command line.

# To read filename from command line one
# can use sys.argv from sys module, which
# is a list containing the command line arguments.
# sys.argv[1] refers to the first argument after
# the name of the python script to be run itself,
# which would represent the file we want to read in.

import sys
fileToRead = sys.argv[1]

# use "with... as variable" syntax to ensure
# file is closed after being read.
with open(fileToRead, 'r') as f:
    # read from file and count number of "e"s
    print(f.read().count("e"))

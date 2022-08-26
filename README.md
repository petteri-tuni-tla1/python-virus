# Python Virus

Example of how to write a prototype of a virus with Python.
Based on this: https://thepythoncorner.com/posts/2021-08-30-how-to-create-virus-python

The virus causes any program it is infected by to print out an annoying unwanted message. Moreover the files infected are capable of spreading the virus by infecting any intact files with the same functionality.

## Requirements

When the virus is launched, it will
1. Print out the message to the screen
2. Search for all the python programs in certain directory of the system
3. Infect the intact files by cloning itself into the files found

## Versions

### 1.0

Skeleton for the program with stub functions. 
Hello World only.

### 2.0

Finds file in given directory (./test for development).
Reads the source code from the current file - not used at this point.
Infects files in given directory by adding comment.

### 3.0

Infects found files with the actual virus code.
Preventing multiple infections not yet implemented.

Directory for sample python code without virus for testing added.

**NOTE: line feed setting may affect how well behaves (\r\n)**


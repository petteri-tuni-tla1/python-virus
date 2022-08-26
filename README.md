# Python Virus

# Disclaimer

**FOR EDUCATION PUPOSES ONLY**

Demonstrates the idea of a virus.

# Introduction

Example of how to write a prototype of a virus with Python.
Based on this: https://thepythoncorner.com/posts/2021-08-30-how-to-create-virus-python

The virus causes any program it is infected by to print out an annoying unwanted message. Moreover the files infected are capable of spreading the virus by infecting any intact files with the same functionality.

# How to use

## For testing

Clone the repository (check the URL) and go to directory

```
git clone https://github.com/petteri-tuni-tla1/python-virus.git
cd python-virus
```

Create "test" directory and copy sample code

```
mkdir test'
cp samples/ip.txt test/ip.py'
cp samples/lottery.txt test/lottery.py'
```

Try out the test scripts. Should work without side effect from virus.
`python3 test/ip.py`

Run the virus code.
`python3 numbers.py`

Try out the test scripts. Infection should be visible.
`$ python3 test/ip.py`

## More realistic

Better more realistic example is to create a empty directory for testing and copying both the infected and uninfected files there. Then modifying the code to search files in local directory instead of "test" directory.

# Requirements

When the virus is launched, it will
1. Print out the message to the screen
2. Search for all the python programs in certain directory of the system
3. Infect the intact files by cloning itself into the files found

# Versions

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

### 3.1

Detects if a file is already infected.
Regex used for line feed detection for better environment compatibility.


# Backlog

* recursive and more versatile file search
* disguise virus code

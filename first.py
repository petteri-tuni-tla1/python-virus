# Virus prototype in Python

def get_virus_code():
    pass

def find_files_to_infect():
    return ("")

def summon_chaos():
    pass

def infect():
    pass

print ("Hello Virus!")

try:
     # retrieve the virus code from the current infected script
     virus_code = get_virus_code() 
 
     # look for other files to infect
     for file in find_files_to_infect():
         infect(file, virus_code)
 
     # call the payload
     summon_chaos()

except:
    pass

finally:
    # delete used names from memory
    for i in list(globals().keys()):
        if(i[0] != '_'):
            exec('del {}'.format(i))

    del i

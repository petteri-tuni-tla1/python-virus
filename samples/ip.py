# --------------------------------------------------------------
# ip.py 

import random, sys

random.seed()

nr = 1
if (len(sys.argv) > 1):
    nr=int(sys.argv[1])

for _ in range(nr):
    ip_addr = ''
    for _ in range(3):
        ip_addr = ip_addr + str(random.randint(2,254)) + "."
    ip_addr = ip_addr + str(random.randint(2,254))
    print ("Random IP address: ", ip_addr)


from bccal import broadcastadd
from nkcal import networkadd
from rangecalculate import iprange

def main():
    uservar=192
    uservar1=168
    uservar2=1
    uservar3=int(input("Enter number of PC to be connected in a network:"))
    broadcastadd.broadcastadd(uservar,uservar1,uservar2,uservar3)
    networkadd.networkadd(uservar,uservar1,uservar2,uservar3)
    iprange.iprange(uservar,uservar1,uservar2,uservar3)
main()


# Manthan Ashok Rajurkar
# Amrutvahini College of Engineering
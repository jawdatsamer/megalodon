#! /usr/bin/python3

import os
import subprocess

# This part collects the current network settings and then places them in a file and displays the contents of the file on the screen
def shownetworkconf():
    os.system("cd ~")
    os.system("ifconfig > ~/megalodon_files/network/res.txt")
    os.system("ip route | grep default >> ~/megalodon_files/network/res.txt")
    os.system("cat ~/megalodon_files/network/res.txt | less")

# This part takes the name of the network interface from the user and then opens the window for the network interface settings,
# and when the settings are finished, restart the network interface to run the settings correctly
def editnetworkconf():
    print ("Please answer the question to complete the process correctly !!")
    interface = str(input("enter the interface name here :"))
    os.system("sudo cp -i /etc/sysconfig/network-scripts/ifcfg-{} /etc/sysconfig/network-scripts/.ifcfg-{}.backup".format(interface,interface))
    print ("Backup file for /etc/sysconfig/network-scripts/ifcfg-{} was created in /etc/sysconfig/network-scripts/.ifcfg-{}.backup".format(interface,interface))
    os.system("sudo nmtui edit {}".format(interface))
    os.system("sudo ifdown {}".format(interface))
    os.system("sudo ifup {}".format(interface))

# This part displays the hostname of the server
def showhostconf():
    print (subprocess.getoutput("hostname -f"))

# This section opens the settings interface for changing hostname, and then asking the user if he want to reboot the server
def edithostconf():
    os.system("sudo cp -i /etc/hostname /etc/.hostname.backup")
    print ("Backup file for /etc/hostname was created in /etc/.hostname.backup")
    os.system("sudo nmtui hostname")
    rebootanswer = str(input("""progress completed !! the system should reboot to take efect do you want reboot now
do you want to reboot now (y) or (n) ?"""))
    if rebootanswer == "y" :
            os.system("sudo reboot")
            exit()
    elif rebootanswer == "n" :
            exit()
    else:
            exit()

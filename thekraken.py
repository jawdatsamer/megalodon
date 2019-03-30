##########################################################################################################################
#                                                                                                                        #
# These some information about these tool :-                                                                             #
# Tool name : The kraken                                                                                                 #
# Author : Jawdat Samer                                                                                                  #
# Email : jawdat.samer@protonmail.com                                                                                    #
# License with GNU GPLv3 or any later version of these license                                                           #
# Version : 1.0                                                                                                          #
# Tested in : CentOS 7, RHEL 7                                                                                #
# Developed using : Fedora 29 , Visual Studio Code and VMware Workstation                                                #
#                                                                                                                        #
# !!WARNNING!! : These tool not compatable with Ubuntu server and Debian , don't be sad we will support them in the      #
# future ^_^                                                                                                             #
#                                                                                                                        # 
##########################################################################################################################

#! /usr/bin/python3
import os
import subprocess
from src import networkconf
from src import usersandgroupconf
from src import servicesmanagement
from src import managepackages
from src import backuptool

#Report function start here
#This part of the code is used to display a simplified report about the system status of the person who executes the program
def report():
    servername = subprocess.getoutput("hostname -f")
    user = subprocess.getoutput('whoami')
    userlog = subprocess.getoutput("who")
    uptime = subprocess.getoutput("uptime -p")
    memorystate = subprocess.getoutput("free -h")
    diskstate = subprocess.getoutput("df -h") 
    print ("""

Welcome back to {} server again Mr.{} these is a small report about the system for you :

        __________________________________Report start here__________________________________

the users loged to the system :
{}
        _____________________________________________________________________________________

the system up time since :
{}

        _____________________________________________________________________________________

The state of memory is :
{}

        _____________________________________________________________________________________

The state of Disks space is :
{}

        __________________________________Report Stop here___________________________________
""".format(servername ,user, userlog, uptime,memorystate,diskstate))

#report function end here

def networkoptions():
    print ("""
        __________________________________Network configuration and the hostname_____________

What do want to do, please choose from the list :

1) Show the network configuration
2) Edit the network configuration
3) show the hostname
4) edit the hostname
0) Back to the main menu
""")

    choseoption = str(input("Enter the number next to your choice to continue >> "))
    if choseoption == "1":
        networkconf.shownetworkconf()    
    elif choseoption == "2":
        networkconf.editnetworkconf()
    elif choseoption == "3":
        networkconf.showhostconf()
    elif choseoption == "4":
        networkconf.edithostconf()
    elif choseoption == "0":
        os.system("clear")
        options()

def usersandgroupoptions():
        print ("""
        __________________________________Configure Users and groups_________________________

what do want to do, please choose from the list :

1) show users
2) add new user
3) delete user
4) modify user
5) show groups
6) add new group
7) delete group
8) modify group
0) Back to the main menu
        """)
        choseoption = str(input("Enter the number next to your choice to continue >> "))
        if choseoption == "1":
           usersandgroupconf.showusers() 
        elif choseoption == "2":
           usersandgroupconf.addusers() 
        elif choseoption == "3":
            usersandgroupconf.delusers()
        elif choseoption == "5":
            usersandgroupconf.showgroups()
        elif choseoption == "6":
            usersandgroupconf.addgroups()
        elif choseoption == "0":
            os.system("clear")
            options()

def servicesoptions():
    print ("""
        __________________________________Services Management________________________________

what do want to do, please choose from the list :

1) Show all services status
2) Show all running services
3) Show service status
4) Services resources monitor
5) Start a service
6) Stop a service
7) Restart a service
0) Back to the main menu

""")
    choseoption = str(input("Enter the number next to your choice to continue >> "))
    if choseoption == "1" :
        servicesmanagement.checkall()
    elif choseoption == "2" :
        servicesmanagement.checkrun()
    elif choseoption == "3" :
        servicesmanagement.checkone()
    elif choseoption == "4" :
        servicesmanagement.servicemonitor()
    elif choseoption == "5" :
        servicesmanagement.servicestart()
    elif choseoption == "6" :
        servicesmanagement.servicestop()
    elif choseoption == "7" :
        servicesmanagement.servicerestart()
    elif choseoption == "0" :
        os.system("clear")
        options()

def managepackagesoption():
    print("""
        __________________________________Packages Management________________________________

what do want to do, please choose from the list :

Show packages :
    1) List all packages installed, available and update
    2) List all packages installed
    3) List all packages available
    4) List all packages updates
    5) List all extra packages
    6) List recently added packages
    7) List all obsoleting packages
    8) List all packages dependencies and what packages provide them
Update, Upgrade and Downgrade :
    9) Check for available package upgrades
    10) Upgrade all the packages on your system
    11) Upgrade, but only 'newest' package match which fixes a problem that affects your system
    12) Upgrade a package
    13) Downgrade a package
Install and remove packages:
    14) install a package
    15) remove a package
    16) reinstall a package
RPM package files :
    17) install package
    18) upgrade package
    19) reinstall package
    20) uninstall package
0) Back to the main menu
""")
    choseoption = str(input("Enter the number next to your choice to continue >> "))
    if choseoption == "1":
        managepackages.listpackage(choseoption)
    elif choseoption == "2":
        managepackages.listpackage(choseoption)
    elif choseoption == "3":
        managepackages.listpackage(choseoption)
    elif choseoption == "4":
        managepackages.listpackage(choseoption)
    elif choseoption == "5":
        managepackages.listpackage(choseoption)
    elif choseoption == "6":
        managepackages.listpackage(choseoption)
    elif choseoption == "7":
        managepackages.listpackage(choseoption)
    elif choseoption == "8":
        managepackages.listpackage(choseoption)
    elif choseoption == "9":
        managepackages.updateupgrade(choseoption)
    elif choseoption == "10":
        managepackages.updateupgrade(choseoption)
    elif choseoption == "11":
        managepackages.updateupgrade(choseoption)
    elif choseoption == "12":
        managepackages.updateupgrade(choseoption)
    elif choseoption == "13":
        managepackages.updateupgrade(choseoption)
    elif choseoption == "14":
        managepackages.installremove(choseoption)
    elif choseoption == "15":
        managepackages.installremove(choseoption)
    elif choseoption == "16":
        managepackages.installremove(choseoption)
    elif choseoption == "17":
        managepackages.rpmpackages(choseoption)
    elif choseoption == "18":
        managepackages.rpmpackages(choseoption)
    elif choseoption == "19":
        managepackages.rpmpackages(choseoption)
    elif choseoption == "20":
        managepackages.rpmpackages(choseoption)
    elif choseoption == "0" :
        os.system("clear")
        options()
#options function start here
#This part of the code is used to display the options provided by the program to customize the system in the form of options chosen by the user, and according to the choice is directed to the user to function appropriate to implement its option
def options():
    print ("""
        __________________________________Main Menu__________________________________________

What do you want to do today , please choose from the list : 

1) Network configuration and the hostname
2) Configure Users and groups
3) Services Management
4) Packages Management
5) Backup tool
6) show a small report about the system
0) Exit
""")
    choseoption = str(input("Enter the number next to your choice to continue >> "))
    if choseoption == "1" :
        os.system("clear")
        networkoptions()
    elif choseoption == "2":
        os.system("clear")
        usersandgroupoptions()
    elif choseoption == "3":
        os.system("clear")
        servicesoptions()
    elif choseoption == "4":
        os.system("clear")
        managepackagesoption()
    elif choseoption == "5":
        print ("Not programmed yet !!")
    elif choseoption == "6":
        os.system("clear")
        report()
        command = input("Enter c to go to the main menu >> ")
        if command == "c":
            os.system("clear")
            options()
    elif choseoption == "0":
        print ("Goodbye, come back soon ^_^ \n")
        exit()    
#options function end here

#user part start here
#This part of the code is used to execute the appropriate functions for the user when starting the program

os.system("clear")
print("""
                                        ██████████                    
                                      ██░░░░░░░░░░██                  
                                    ▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓                
                                  ▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓              
                                  ██░░▒▒██▒▒▒▒▒▒██▒▒▒▒██              
                                  ██░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██              
                        ██████    ██░░▒▒▒▒▒▒██▒▒▒▒▒▒▒▒██    ██████    
                      ██████▒▒▓▓    ▓▓▒▒▒▒██▓▓██▒▒▒▒██    ▓▓▒▒████▓▓  
                    ██      ██░░██    ██▒▒▒▒██░░▒▒██    ██░░██      ██
                    ██      ██▒▒▒▒████▒▒▒▒▒▒▒▒▒▒▒▒▒▒████▒▒▒▒██      ██
                      ██      ██▒▒▒▒▒▒▒▒██▒▒▒▒▒▒██▒▒▒▒▒▒▒▒██      ██  
                                ██▒▒████▒▒▒▒▒▒▒▒▒▒████▒▒██            
                        ██████    ██░░▒▒██▒▒██▒▒██▒▒▒▒██    ██████    
                      ██████▒▒████▒▒▒▒██▒▒▒▒██▒▒▒▒██▒▒▒▒████▒▒██████  
                    ██      ██▒▒▒▒▒▒██▒▒▒▒██  ██▒▒▒▒██▒▒▒▒▒▒██      ██
                    ██        ██████▒▒████      ████▒▒██████        ██
                      ██          ████              ████          ██  
                                ████                  ████            
                                ██                      ██            
                                ██    ██          ██    ██            
                                  ▓▓▓▓              ▓▓▓▓              
            [#] The Kraken v1.0

                    
                  " It's time to think more and write less with The Kraken "


""")
command = input("Enter c to continue or q to quit >> ")
if command == "c":
    os.system("clear")
    options()
elif command == "q":
    print ("Goodbye, come back soon ^_^ \n")
    exit()
else:
    print ("wrong choice the will go close !!\n")
    exit()

#user part end here

##########################################################################################################################
#                                                                                                                        #
# These some information about these tool :-                                                                             #
# Tool name : Megalodon                                                                                                  #
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
import random

#Report function start here
#This part of the code is used to display a simplified report about the system status of the person who executes the program
def report():
    servername = subprocess.getoutput("hostname -f")
    user = subprocess.getoutput('whoami')
    userlog = subprocess.getoutput("who")
    upsince = subprocess.getoutput("uptime -s")
    uptime = subprocess.getoutput("uptime -p")
    memorystate = subprocess.getoutput("free -h")
    diskstate = subprocess.getoutput("df -h") 
    print ("""

Welcome back to {} server again Mr.{} these is a small report about the system for you :

        __________________________________Report start here__________________________________

The users loged to the system :
{}
        _____________________________________________________________________________________

The system up time statistics :
this system has been working since : {}
this system has been up since : {}
        _____________________________________________________________________________________

The state of memory is :
{}

        _____________________________________________________________________________________

The state of Disks space is :
{}

        __________________________________Report Stop here___________________________________
""".format(servername ,user, userlog, upsince,uptime,memorystate,diskstate))

#report function end here

def networkoptions():
    print ("""
        __________________________________Network configuration and the hostname_____________

What do you want to do, please choose from the list :
Network options :
    1) Show the network configuration
    2) Edit the network configuration
Hostname options :
    3) show the hostname
    4) edit the hostname

0) Back to the main menu
00) Exit
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
    elif choseoption == "00":
        print ("Goodbye, come back soon ^_^ \n")
        exit() 
def usersandgroupoptions():
        print ("""
        __________________________________Configure Users and groups_________________________

what do you want to do, please choose from the list :
Users configuration : 
    1) show users
    2) show user information
    3) add new user (Quick)
    4) add new user (Custom)
    5) delete user
    6) modify user
Groups configuration :
    7) show groups
    8) add new group
    9) delete group
    10) modify group 

0) Back to the main menu
00) Exit
        """)
        choseoption = str(input("Enter the number next to your choice to continue >> "))
        if choseoption == "1":
           usersandgroupconf.showusers()
        elif choseoption == "2":
            usersandgroupconf.showuserinfo()
        elif choseoption == "3":
            usersandgroupconf.addusersquick()
        elif choseoption == "4":
           usersandgroupconf.adduserscustom() 
        elif choseoption == "5":
            usersandgroupconf.delusers()
        elif choseoption == "6":
            usersandgroupconf.moduser()
        elif choseoption == "7":
            usersandgroupconf.showgroups()
        elif choseoption == "8":
            usersandgroupconf.addgroups()
        elif choseoption == "9":
            usersandgroupconf.removegroups()
        elif choseoption == "10":
            usersandgroupconf.modifygroup()
        elif choseoption == "0":
            os.system("clear")
            options()
        elif choseoption == "00":
            print ("Goodbye, come back soon ^_^ \n")
            exit() 

def servicesoptions():
    print ("""
        __________________________________Services Management________________________________

what do you want to do, please choose from the list :

Show services and monitor :
    1) Show all services status
    2) Show all running services
    3) Show service status
    4) monitor services by their resource usage
Service Control :
    5) Start a service
    6) Stop a service
    7) Restart a service

0) Back to the main menu
00) Exit
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
    elif choseoption == "00":
        print ("Goodbye, come back soon ^_^ \n")
        exit() 
def managepackagesoption():
    print("""
        __________________________________Packages Management________________________________

what do you want to do, please choose from the list :

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
00) Exit
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
    elif choseoption == "00":
        print ("Goodbye, come back soon ^_^ \n")
        exit() 
def backupoptions():
    print("""
        __________________________________Backup Tool________________________________________

what do you want to do, please choose from the list :

Backup options :
    1) Backup user home directory
    2) Backup home directory for all users (Not working yet!)
    3) Backup linux system configuration files
    4) Backup logs
    5) Backup all the system
Restore options :
    6) Restore user home directory from backup
    7) Restore all user home directory from backup (Not working yet!)
    8) Restore linux system configuration files from backup
    9) Restore logs from backup
    10) Restore all the system from backup
0) Back to the main menu
00) Exit
""")
    choseoption = str(input("Enter the number next to your choice to continue >> "))
    if choseoption == "1":
        backuptool.backupuser()
#    elif choseoption == "2":
#        backuptool.backup_all_users()
    elif choseoption == "3":
        backuptool.backupconffiles()
    elif choseoption == "4":
        backuptool.backuplogs()
    elif choseoption == "5":
        backuptool.fullbackup()
    elif choseoption == "6":
        backuptool.restoreuserfiles()
    elif choseoption == "0":
        os.system("clear")
        options()
    elif choseoption == "00":
        print ("Goodbye, come back soon ^_^ \n")
        exit()    
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
5) Backup Options
6) show a small report about the system
0) Exit

WARNING : These tool not compatible with Ubuntu server and Debian and if you try to use them within these systems, it will be at your own risk , don't be sad we will support them in the future

""")
    choseoption = str(input("Enter the number next to your choice to continue >> "))
    if choseoption == "1" or choseoption == "2" or choseoption == "3" or choseoption == "4" or choseoption == "5" or choseoption == "6":
        tracker = int(choseoption)
        while tracker != 0:
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
                os.system("clear")
                backupoptions()
            elif choseoption == "6":
                os.system("clear")
                report()
                command = input("Enter c to go to the main menu >> ")
                if command == "c" or command == "":
                    os.system("clear")
                    options()
            elif choseoption == "0":
                break
    elif choseoption == "":
        print ("Wrong choose ! we are going to close -_-")
    else:
        print ("Wrong choose ! we are going to close -_-")
    if choseoption == "0":
        print ("Goodbye, come back soon ^_^ \n")
#options function end here

#user part start here
#This part of the code is usedc to execute the appropriate functions for the user when starting the program

os.system("clear")

for x in range(1):
    screen = random.randint(1,2)
    if screen == 1 :
        print("""           
                 ███▄ ▄███▓▓█████   ▄████  ▄▄▄       ██▓     ▒█████  ▓█████▄  ▒█████   ███▄    █ 
                ▓██▒▀█▀ ██▒▓█   ▀  ██▒ ▀█▒▒████▄    ▓██▒    ▒██▒  ██▒▒██▀ ██▌▒██▒  ██▒ ██ ▀█   █ 
                ▓██    ▓██░▒███   ▒██░▄▄▄░▒██  ▀█▄  ▒██░    ▒██░  ██▒░██   █▌▒██░  ██▒▓██  ▀█ ██▒
                ▒██    ▒██ ▒▓█  ▄ ░▓█  ██▓░██▄▄▄▄██ ▒██░    ▒██   ██░░▓█▄   ▌▒██   ██░▓██▒  ▐▌██▒
                ▒██▒   ░██▒░▒████▒░▒▓███▀▒ ▓█   ▓██▒░██████▒░ ████▓▒░░▒████▓ ░ ████▓▒░▒██░   ▓██░
                ░ ▒░   ░  ░░░ ▒░ ░ ░▒   ▒  ▒▒   ▓▒█░░ ▒░▓  ░░ ▒░▒░▒░  ▒▒▓  ▒ ░ ▒░▒░▒░ ░ ▒░   ▒ ▒ 
                ░  ░      ░ ░ ░  ░  ░   ░   ▒   ▒▒ ░░ ░ ▒  ░  ░ ▒ ▒░  ░ ▒  ▒   ░ ▒ ▒░ ░ ░░   ░ ▒░
                ░      ░      ░   ░ ░   ░   ░   ▒     ░ ░   ░ ░ ░ ▒   ░ ░  ░ ░ ░ ░ ▒     ░   ░ ░ 
                    ░      ░  ░      ░       ░  ░    ░  ░    ░ ░     ░        ░ ░           ░ 
                                                                      ░                           
            [#] Megalodon v1.0

                 "Don't do it like a regular System Admin , with Megalodon do it like a King"
""")
    elif screen == 2 :
        print("""           
                                                      ░░░░                                                        
                                                    ░░    ░░                                                      
                                                    ░░  ░░░░                                                      
                                                      ░░░░                                                        
                                                                                                  
                                          ░░                                                                      
                                      ░░░░░░░░    ░░  ░░░░  ░░░░░░██████████████  ░░░░    ░░                      
                                      ░░  ░░      ░░    ░░  ██████▒▒▓▓▒▒▓▓▒▒▓▓██  ░░    ░░                        
                                        ░░░░      ░░    ░░▓▓▒▒▒▒▓▓▒▒▒▒▓▓████▓▓  ░░░░      ░░                      
                                            ██████████████▒▒▒▒▒▒▒▒▒▒▒▒██                                          
                                    ████████▓▓▒▒▒▒▓▓▒▒▓▓▒▒▒▒▒▒▒▒▒▒▒▒██                                            
                                ████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒████                                          
                            ████▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓████▒▒                                    
                          ██▓▓▒▒▒▒▒▒▒▒▒▒▓▓██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓████                                
                        ██▓▓▒▒▒▒▒▒▒▒▒▒▓▓▒▒▓▓██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓████                            
                      ██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██▒▒▒▒██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▒▒████                        
                    ██▒▒▒▒▒▒▒▒████▒▒▒▒▒▒▓▓██▒▒██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓██                      
                  ██▒▒▒▒▒▒▒▒██░░▒▒▒▒▒▒██▒▒██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓██                    
                  ██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██  ████████████████
                ░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██░░██▒▒▒▒▒▒██▒▒▒▒▒▒▒▒██▒▒░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓██▓▓▓▓▓▓▓▓▓▓▓▓▒▒██
                ██▒▒▒▒▒▒▒▒▒▒██████░░██▒▒░░░░░░██▒▒▒▒▒▒▒▒▒▒██░░▒▒████████████████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒████  
                  ██████████░░░░░░██░░▒▒░░░░▒▒░░██▒▒▒▒▒▒▒▒██████                    ████████▒▒▒▒▒▒▒▒▒▒▓▓████      
                        ██████████▒▒▒▒░░▒▒░░████  ██▒▒▒▒▒▒██                                ██▒▒▒▒▒▒▒▒██          
                          ██░░░░▒▒░░░░██████        ██▒▒▒▒▒▒██                              ██▒▒▒▒▒▒██            
                            ████▓▓████                ▓▓██▒▒██                              ██▒▒▒▒██              
                                                          ████                              ██▒▒▒▒██              
                                                                                              ██▒▒██              
                                                                                              ██▒▒██              
                                                                                                ████              
            [#] Megalodon v1.2 come to you by Jawdat Samer
                       
                       "Don't do it like a regular System Admin , with Megalodon do it like a King"              
""")

command = input("Enter c to continue or q to quit >> ")
if command == "c" or command == "":
    os.system("clear")
    options()
elif command == "q":
    print ("Goodbye, come back soon ^_^ \n")
    exit()
else:
    print ("wrong choice the will go close !!\n")
    exit()

#user part end here

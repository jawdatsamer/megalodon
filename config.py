#! /usr/bin/python3

import os

#This part is used to install the important tools needed by the program to work correctly
if 'NAME="CentOS Linux"' in open("/etc/os-release").read() or 'NAME=CentOS Linux' in open("/etc/os-release").read():
    os.system("sudo yum update")
    os.system("sudo yum install NetworkManager-tui")    
    os.system("sudo yum install -y https://centos7.iuscommunity.org/ius-release.rpm")
    os.system("sudo yum update")
    os.system("sudo yum install -y python36u python36u-libs python36u-devel python36u-pip")

elif 'NAME="Ubuntu"' in open("/etc/os-release").read() or 'NAME=Ubuntu' in open("/etc/os-release").read():
    os.system("sudo apt-get update")
    os.system("sudo apt-get install python3")
    os.system("sudo apt-get install NetworkManager")
elif 'NAME="Red Hat Enterprise Linux Server"' in open("/etc/os-release").read() or 'NAME=Red Hat Enterprise Linux Server' in open("/etc/os-release").read():
    os.system("sudo yum update")
    os.system("sudo yum install NetworkManager-tui")    
    os.system("sudo yum install centos-release-scl")
    os.system("sudo yum install rh-python36")
else:
    print ("Sorry, we could not detect your operating system, please enter the operating system name manually !!")
    os_name = str(input("""whats is your OS name choose from the list :
1) Red Hat Enterprise Linux Server
2) Ubuntu Server
3) CentOS

Please enter the number here >>"""))
    if os_name == "1":
        os.system("sudo yum install NetworkManager-tui")
    elif os_name == "2":
        os.system("sudo yum install NetworkManager")
    elif os_name == "3" :
        os.system("sudo yum install NetworkManager-tui")

#This part is used to create folders that the program uses to place its files during the execution of certain tasks
os.system("cd")
os.system("mkdir ~/megalodon_files")
os.system("mkdir ~/megalodon_files/network")

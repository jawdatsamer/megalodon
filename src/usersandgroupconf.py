#! /usr/bin/python3

import os
import subprocess

# This part is used to open a file /etc/passwd To view the users inside it
def showusers():
    os.system("""awk -F: '{ print "username: " $1 " | user id: " $3 " | group id: " $4 " | path: " $6}' /etc/passwd | less""")


def addusers():
    newuser = str(input("Enter new user name :"))
    newgroup = str(input("Enter the group you want to join user to it [{}]:".format(newuser)))
    newpassword = str(input("Enter the new password to {} account".format(newuser)))
    askabouthomedir = str(input("Do you want to add home directory for these user ? (y) or (n) :"))
    if askabouthomedir == "y":
        homedir = str(input("Enter the path for new user home directory [/home/{}]".format(newuser)))
        if newgroup == "":
            os.system("sudo useradd -d /home/{} -U -p {} {} ".format(newuser,newpassword,newuser))
        else:
            os.system("sudo useradd -d {} -g {} -p {} {} ".format(homedir,newgroup,newpassword,newuser))
    elif askabouthomedir == "n" :
        os.system("sudo useradd -M -U -p {} {} ".format(newpassword,newuser))


def delusers():
    deluser = str(input("Enter the name of user you want to delete :"))
    os.system("sudo deluser {}".format(deluser))

def showgroups():
    os.system("""awk -F: '{ print "groupname: " $1 " | group id: " $3 " | members: " $4}' /etc/group | less""")

def addgroups():
    newgroup = str(input("Enter the new group name :"))
    os.system("groupadd {}".format(newgroup))
#! /usr/bin/python3

import os
import subprocess

# This part is used to open a file /etc/passwd To view the users inside it
def showusers():
    os.system("""awk -F: '{ print "username: " $1 " | user id: " $3 " | group id: " $4 " | GECOS: " $5 " | path: " $6 " | Shell: " $7}' /etc/passwd | less""")

def showuserinfo():
    username = str(input("Please enter the user name :"))
    print("\n")
    os.system("""awk -F: '{ print "username:" $1 " | user id: " $3 " | group id: " $4 " | GECOS: " $5 " | path: " $6 " | Shell: " $7}' /etc/passwd |less > ~/megalodon_files/usersandgroups/res.txt""")
    os.system("cat ~/megalodon_files/usersandgroups/res.txt | grep :{} > ~/megalodon_files/usersandgroups/res1.txt".format(username))
    print("-------------------------------------------------------------")
    os.system("cat ~/megalodon_files/usersandgroups/res1.txt")
    print("-------------------------------------------------------------")
    os.system("sudo chage {} -l".format(username))

def addusersquick():
    username = str(input("Enter name for the new user :"))
    os.system("sudo adduser {}".format(username))

def adduserscustom():
    newuser = str(input("Enter new user name :"))
    newgroup = str(input("Enter the group you want to join user to it [{}]:".format(newuser)))
    if newgroup == "":
        group = "-U"
    else :
        group = "-N -g {}".format(newgroup)

    newpassword = str(input("Enter the new password to {} account:".format(newuser)))

    askabouthomedir = str(input("Do you want to add home directory for these user ? (y) or (n) :"))
    if askabouthomedir == "y":
        askabouthomedir = str(input("Do want to use home directory /home/{} for these user ? (y) or (n) :".format(newuser)))
        if askabouthomedir == "n":
            homedir = str(input("Enter the path for new user home directory :"))
        elif askabouthomedir == "y":
            homedir = "/home/{}".format(newuser)
    elif askabouthomedir == "n":
        homedir = "-M"

    shell = str(input("""Chose the shell for these user from the list or enter shell path :
1)bash
2)sh
3)python
4)no login
>>"""))
    if shell == "1":
        shell = "/bin/bash"
    elif shell == "2":
        shell = "/bin/sh"
    elif shell == "3":
        shell = "/bin/python"
    elif shell == "4":
        shell = "/sbin/nologin"

    comment = str(input("Enter comment(GECOS) for these new user account :"))
    if comment == "":
        os.system("sudo useradd {} -d {} {} -p {} -s {}".format(newuser,homedir,group,newpassword,shell))
    else:
        os.system("sudo useradd {} -d {} {} -p {} -s {} -c {}".format(newuser,homedir,group,newpassword,shell,comment))   

def delusers():
    deluser = str(input("Enter the name of user you want to delete :"))
    askabouthomedir = str(input("Do you want delete home directory for user {} , (y) or (n) ?".format(deluser)))
    if askabouthomedir == "y":
        os.system("sudo userdel {} -r".format(deluser))
    elif askabouthomedir == "n":
        os.system("sudo userdel {}".format(deluser))

def moduser():
    os.system("clear")
    print("""
        __________________________________Modify user________________________________________

Select the desired edit from the list :
    1) Change the login name
    2) Change the home directory for the user account
    3) Set account expiration date
    4) Set the number of days after a password expires until the account is permanently disabled
    5) Change user primary group
    6) Add users to new groups and remove them from the old
    7) Add users to new groups without remove them from the old
    8) Lock user account
    9) Unlock user account
    10) move the home directory for the user account
""")
    chooseoption = str(input("Enter the number next to your choice to continue >> "))
    if chooseoption == "1" :
        username = str(input("Enter the current user name :"))
        newusername = str(input("Enter the new user name :"))
        os.system("sudo usermod {} -l {}".format(username,newusername))

    elif chooseoption == "2":
        username = str(input("Enter the user name :"))
        homepath = str(input("Enter the new home directory path :"))
        os.system("sudo usermod {} -d {}".format(username,homepath))

    elif chooseoption == "3":
        username = str(input("Enter the user name :"))
        expdate = str(input("Enter the account expiration date as follows [yyyy,mm,dd] or leave it blank if the account does not expire:"))
        os.system("sudo usermod {} -e {}".format(username,expdate))

    elif chooseoption == "4" :
        username = str(input("Enter the user name :"))
        inactivedate = str(input("Enter The number of days after a password expires until the account is permanently disabled\n *rememper A value of 0 disables the account as soon as the password has expired, and a value of -1 disables the feature."))
        os.system("sudo usermod {} -f {}".format(username,inactivedate))

    elif chooseoption == "5" :
        username = str(input("Enter the user name :"))
        primgroup = str(input("Enter the new primary group name or number for these user :"))
        os.system("sudo usermod {} -g {}".format(username,primgroup))

    elif chooseoption == "6":
        usersname = str(input("Enter the user name , or enter list of users with these format [user1,user2,user3...] :"))
        groupsname = str(input("Enter the group name , or enter list of groups with these format [group1,group2,group3...] :"))
        os.system("sudo usermod {} -G {}".format(usersname,groupsname))
        
    elif chooseoption == "7":
        usersname = str(input("Enter the user name , or enter list of users with these format [user1,user2,user3...] :"))
        groupsname = str(input("Enter the group name , or enter list of groups with these format [group1,group2,group3...] :"))
        os.system("sudo usermod {} -G {} -a".format(usersname,groupsname))

    elif chooseoption == "8":
        username = str(input("Enter the user name :"))
        os.system("sudo usermod {} -L".format(username))

    elif chooseoption == "9":
        username = str(input("Enter the user name :"))
        os.system("sudo usermod {} -U".format(username))

    elif chooseoption == "10":
        username = str(input("Enter the user name :"))
        newhomepath = str(input("Enter the new home dir path for the user :"))
        os.system("sudo usermod {} -d {} -m".format(username,newhomepath))
def showgroups():
    os.system("""awk -F: '{ print "groupname: " $1 " | group id: " $3 " | members: " $4}' /etc/group | less""")

def addgroups():
    newgroup = str(input("Enter the new group name :"))
    os.system("sudo groupadd {}".format(newgroup))

def removegroups():
    groupname = str(input("Enter the group name :"))
    os.system("sudo groupdel -f {}".format(groupname))

def modifygroup():
    groupname = str(input("Enter group name :"))
    

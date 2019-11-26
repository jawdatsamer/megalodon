#! /usr/bin/python3

import os
import subprocess

def backupuser():
    username = str(input("Please enter the user name :"))
    homedir = "~{}".format(username)
    date = subprocess.getoutput("date -I")
    backupfolder = str(input("Type the path of the folder that you want to save the backup inside him [~/megalodon_files/backup_files] :"))
    if backupfolder == "":
        backupfolder = "~/megalodon_files/backup_files/users_backup/"
    os.system("sudo tar -cvf {}/{}_backup_{}.tar {}".format(backupfolder,username,date,homedir))

# def backup_all_users():
#     username = str(os.system("""awk -F: '{ print $1}' /etc/passwd |less > ~/megalodon_files/usersandgroups/res.txt"""))
#     homedir = [str(os.system("""awk -F: '{ $6 }'"""))]
#     date = subprocess.getoutput("date -I")
#     namelist = []
#     backupfolder = str(input("Type the path of the folder that you want to save the backup inside him [~/megalodon_files/backup_files] :"))
#     if backupfolder == "":
#         backupfolder = "~/megalodon_files/backup_files/all_users_backup/"
#     get_name = open("~/megalodon_files/usersandgroups/res.txt","r")
#     for line in get_name.readlines():
#         namelist.append(line)
#         line_num += 1

def backupconffiles():
    backupname = str(input("Please Enter the name for new backup :"))
    conf_files = "/etc/*"
    date = subprocess.getoutput("date -I")
    backupfolder = str(input("Type the path of the folder that you want to save the backup inside him [~/megalodon_files/backup_files/conf_backup/] :"))
    if backupfolder == "":
        backupfolder = "~/megalodon_files/backup_files/conf_backup/"
    os.system("sudo tar -cvf {}/{}_backup_{}.tar {}".format(backupfolder,backupname,date,conf_files))

def backuplogs():
    backupname = str(input("Please Enter name for the new backup :"))
    logs_files = "/var/log/*"
    date = subprocess.getoutput("date -I")
    backupfolder = str(input("Type the path of the folder that you want to save the backup inside him [~/megalodon_files/backup_files/logs_backup/] :"))
    if backupfolder == "":
        backupfolder = "~/megalodon_files/backup_files/logs_backup/"
    os.system("sudo tar -cvf {}/{}_backup_{}.tar {}".format(backupfolder,backupname,date,logs_files))

def fullbackup():
    backupname = str(input("Please Enter name for the new backup :"))
    filespath = "/*"
    date = subprocess.getoutput("date -I")
    backupfolder = str(input("Type the path of the folder that you want to save the backup inside him [~/megalodon_files/backup_files/full_system/backup/] :"))
    if backupfolder == "":
        backupfolder = "~/megalodon_files/backup_files/full_system_backup/"
    os.system("sudo tar -cvf {}/{}_backup_{}.tar {}".format(backupfolder,backupname,date,filespath))

def restoreuserfiles():
    backupfolder = str(input("Please enter the path for your backup file :"))
    username = str(input("Enter user name :"))
    userfilespath = "/home/{}/".format(username)
    os.system("sudo tar -xf {} {}".format(backupfolder,userfilespath))

def restoreconffiles():
    backupfolder = str(input("Please enter the path for your backup file :"))
    conffiles = "/etc/"
    os.system("sudo tar -xf {} {}".format(backupfolder,conffiles))

def restorelogs():
    backupfolder = str(input("Please enter the path for your backup file :"))
    logsfiles = "/var/log/"
    os.system("sudo tar -xf {} {}".format(backupfolder,logsfiles))

# Danger part !!
def restorefullbackup():
    print ("Warning These is a danger process, be carefull !!")
    backupfolder = str(input("Please enter the path for your backup file :"))
    rootpath = "/"
    os.system("sudo tar -xf {} {}".format(backupfolder,rootpath))

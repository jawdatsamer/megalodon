#! /usr/bin/python3

import os
import subprocess

def backupuser():
    username = str(input("Please enter the user name :"))
    homedir = "~{}".format(username)
    date = subprocess.getoutput("date -I")
    backupfolder = str(input("Type the path of the folder that you want to save the backup inside him [~/megalodon_files/backup_files] :"))
    if backupfolder == "":
        backupfolder = "~/megalodon_files/backup_files/"
    os.system("sudo tar -cvf {}/{}_backup_{}.tar {}".format(backupfolder,username,date,homedir))

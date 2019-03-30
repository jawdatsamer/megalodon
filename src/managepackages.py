
#! /usr/bin/python3

import os
import subprocess

def listpackage(ch):
    ch = str(ch)
    if ch == "1":
        os.system("sudo yum list all | less")
    elif ch == "2":
        os.system("sudo yum list installed | less")
    elif ch == "3":
        os.system("sudo yum list available | less")
    elif ch == "4":
        os.system("sudo yum list updates | less")
    elif ch == "5":
        os.system("sudo yum list extras | less")
    elif ch == "6":
        os.system("sudo yum list recent | less")
    elif ch == "7":
        os.system("sudo yum list obsoletes | less")
    elif ch == "8":
        os.system("sudo yum deplist | less")

def updateupgrade(ch):
    ch = str(ch)
    if ch == "9":
        os.system("sudo yum check-update")
    elif ch == "10":
        os.system("sudo yum check-update && sudo yum upgrade")
    elif ch == "11":
        os.system("sudo yum check-update && sudo yum upgrade-minimal")
    elif ch == "12":
        packagename = str(input("Please enter the package name :"))
        os.system("sudo yum upgrade {}".format(packagename))
    elif ch == "13":
        packagename = str(input("Please enter the package name :"))
        os.system("sudo yum downgrade {}".format(packagename))

def installremove(ch):
    ch = str(ch)
    if ch == "14":
        packagename = str(input("Please enter the package name :"))
        os.system("sudo yum install {}".format(packagename))
    elif ch == "15":
        packagename = str(input("Please enter the package name :"))
        os.system("sudo yum remove {}".format(packagename))
    elif ch == "16":
        packagename = str(input("Please enter the package name :"))
        os.system("sudo yum reinstall {}".format(packagename))

def rpmpackages(ch):
    ch = str(ch)
    if ch == "17":
        rpmpath = str("Please enter the path of rpm package :")
        os.system("sudo rpm -i {}".format(rpmpath))
    elif ch == "18":
        rpmpath = str("Please enter the path of rpm package :")
        os.system("sudo rpm --upgrade {}".format(rpmpath))
    elif ch == "19":
        rpmpath = str("Please enter the path of rpm package :")
        os.system("sudo rpm --reinstall {}".format(rpmpath))
    elif ch == "20":
        rpmpath = str("Please enter the path of rpm package :")
        os.system("sudo rpm --erase {}".format(rpmpath))
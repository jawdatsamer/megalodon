
#! /usr/bin/python3

import os
import subprocess

# This part is used to display all services in the server and the status of it
def checkall():
    os.system("sudo systemctl list-units --type service")

# This part is used to display all services that are running
def checkrun():
    os.system("sudo systemctl list-units --type service | grep running | less")

# This part takes the name of the service from the user, and then checks if it works
def checkone():
    servicename = str(input("Please enter the name of the service :"))
    os.system("sudo service {} status".format(servicename))

# This part is used to monitor the operation of services that consume system resources heavily
def servicemonitor():
    os.system("sudo systemd-cgtop")

# This part asks the user to enter the service name and then start it
def servicestart():
    servicename = str(input("Please enter the name of the service to start it :"))
    os.system("sudo service {} start".format(servicename))

# This part asks the user to enter the service name and then stop it
def servicestop():
    servicename = str(input("Please enter the name of the service to stop it :"))
    os.system("sudo service {} stop".format(servicename))

# This part asks the user to enter the service name and then restart it
def servicerestart():
    servicename = str(input("Please enter the name of the service to restart it :"))
    os.system("sudo service {} restart".format(servicename))

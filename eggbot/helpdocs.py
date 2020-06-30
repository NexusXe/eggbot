import os, discord, sys


def getAuth(wanted):
    file = open('auth').readlines()
    for line in file:
        if line.startswith(wanted):
            print(line)
            return str([line][0])


TOKEN = getAuth('TOKEN')

print(TOKEN)

import os

#module that causes the program to quit
moduleName = "quit"

commandWords = ["quit","control"]

def execute(command):
    os._exit(0)

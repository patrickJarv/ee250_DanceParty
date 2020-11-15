#You can import any modules required here
import os
#This is name of the module - it can be anything you want
moduleName = "quit"

#These are the words you must say for this module to be executed
commandWords = ["quit","control"]

#This is the main function which will be execute when the above command words are said
def execute(command):
    os._exit(0)

#You can import any required modules here
import sys
sys.path.insert(1, '/home/ee250/project-pjarvis')
import spotifyPlayer
#This can be anything you want
moduleName = "Spotify Player"

#All of the words must be heard in order for this module to be executed
commandWords = ["spotify", "artist", "song"]

def execute(command):
    #Write anything you want to be executed when the commandWords are heard
    #The 'command' paramete"r is the command you speak
    terms = command.split()
    if(terms[0] != "spotify"):
        return "ERROR"

    idx = 0
    band = 0
    song = 0
    for i in range(len(terms)):
    	if(terms[i] == "artist"):
    		band = i;
    	if(terms[i] == "song"):
    		song = i;


    if(band+1 == song) or (band > song):
        return "ERROR"

    bandStr = "";
    for i in range(band+1, song):
    	bandStr = bandStr + terms[i]
    	if (i != (song-1)):
    		bandStr = bandStr + " "


    if(song+1 == len(terms)):
        return "ERROR"
    songStr = ""
    for i in range (song + 1, len(terms)):
    	songStr = songStr + terms[i]
    	if (i != (len(terms)-1)):
    		songStr = songStr + " "
    help = spotifyPlayer.spotifyPlayer()
    return help.begin(bandStr, songStr)
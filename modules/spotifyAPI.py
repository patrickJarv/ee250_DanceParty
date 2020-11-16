import sys
sys.path.insert(1, '/home/ee250/project-pjarvis')
import spotifyPlayer

moduleName = "Spotify Player"
commandWords = ["spotify", "artist", "song"]

def execute(command):
    #get the response in the Note
    terms = command.split()
    #if the first one isn't Spotify then the command is wrong
    if(terms[0] != "spotify"):
        return "ERROR"

    #parse the command so that we have the song and artist name
    idx = 0
    band = 0
    song = 0
    for i in range(len(terms)):
    	if(terms[i] == "artist"):
    		band = i;
    	if(terms[i] == "song"):
    		song = i;

    #also bad format of command
    if(band+1 == song) or (band > song):
        return "ERROR"

    bandStr = "";
    for i in range(band+1, song):
    	bandStr = bandStr + terms[i]
    	if (i != (song-1)):
    		bandStr = bandStr + " "

    #another bad format of command
    if(song+1 == len(terms)):
        return "ERROR"
    songStr = ""
    for i in range (song + 1, len(terms)):
    	songStr = songStr + terms[i]
    	if (i != (len(terms)-1)):
    		songStr = songStr + " "
            
     #once we have the names, we pass it to the object that handles the API
    help = spotifyPlayer.spotifyPlayer()
    return help.begin(bandStr, songStr)

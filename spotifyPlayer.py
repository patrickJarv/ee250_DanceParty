import spotipy
import json
import time
import os
import requests
import spotipy.util as util
 


class spotifyPlayer:
	token = None
	clientRP = None
	def __init__(self):
		pass

	def begin(self, bandStr=None, songStr=None):
		
		###### INSERT SPOTIFY USERNAME HERE #####
		
		username = ""
		
		#########################################
		
		#if the request has nothing inside
		if(bandStr is None or songStr is None):
			print("no band or song name given")
			return
		#in order to make a request, we must have a token authorization, if we don't we get the Google pop-up where we must copy the URL into the command line.
		#only have to do this token authorization once, as the token gets stored in the cache after the first use.
		scope = 'user-read-private user-read-playback-state user-modify-playback-state'
		self.token = util.prompt_for_user_token(username, scope)
		#token authorization will occur when we say the Note Spotify artist test song start so after that we return that Setup was complete
		if bandStr == "test" and songStr == "start":
			return "Setup"
		songStrExtra = songStr + " - single version"
		#create request object and find the Web Browser that has the Spotify Web Player open
		spotify = spotipy.Spotify(auth=self.token)
		devices = spotify.devices()
		deviceID = devices['devices'][0]['id']
		
		#search for the artist given
		results = spotify.search(q='artist:' + bandStr, type='artist')
		artistId = results['artists']['items'][0]['id']
		results = spotify.artist_albums(artistId)
		albums = results['items']
		call = False
		
		#look through all albums to find the song requested
		for item in albums:
		    albumID = item['id']
		    albumArt = item['images'][0]['url']

		    # Extract track data
		    trackResults = spotify.album_tracks(albumID)
		    trackResults = trackResults['items']
		    for item in trackResults:
			
			#if the song we are looking at has the same name as the one requested
		    	if(item['name'].lower()== songStr or item['name'].lower()== songStrExtra):
				#we only want the first one in popularity so the call variable is used to prevent other songs from being selected
		    		if(not call):
					#grab the data
					    uri = item['uri']
					    trackSelectionList = []
					    trackSelectionList.append(uri)
					    data =spotify.audio_features(item['id'])
					    name = item['name']
					    call = True
					#try to play the song, one of the limitations with the API is that some songs can't be played
					    try:
					    	spotify.start_playback(deviceID, None, trackSelectionList)
					    except:
					    	continue
					    response = spotify.current_playback()
					#don't give the data to the RPi until the song starts playing
					    while True:
					    	if(response['is_playing']):
					    		break
					    	response = spotify.current_playback()
					#then return the song's JSON object
					    return(bandStr + '#%#' + name + '#$#' + json.dumps(data, sort_keys=True, indent=2))

		#if we couldn't find the song in the first for loop then we look broader, taking in karoake versions, live editions, or other 
		    for item in trackResults:
		    	reduced = item['name'][0:len(songStr)].lower()
		    	if(reduced == songStr):
				#I think rehearsal versions of the song aren't dance party material so we skip it
		    		if "rehearsal" in item['name'].lower():
		    			continue
				#otherwise, we repeat the same process as the above for loop
		    		if(not call):
					    uri = item['uri']
					    trackSelectionList = []
					    trackSelectionList.append(uri)
					    data =spotify.audio_features(item['id'])
					    name = item['name']
					    call = True	
					    try:
					    	spotify.start_playback(deviceID, None, trackSelectionList)
					    except:
					    	continue
					    response = spotify.current_playback()
					    while True:
					    	#print(response['is_playing'])
					    	if(response['is_playing']):
					    		break
					    	response = spotify.current_playback()
					    return(bandStr + '#%#' + name + '#$#' + json.dumps(data, sort_keys=True, indent=2))

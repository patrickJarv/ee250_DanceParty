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
		if(bandStr is None or songStr is None):
			print("no band or song name given")
			return
		username = "pjarvite"
		scope = 'user-read-private user-read-playback-state user-modify-playback-state'
		self.token = util.prompt_for_user_token(username, scope)
		songStrExtra = songStr + " - single version"
		spotify = spotipy.Spotify(auth=self.token)
		devices = spotify.devices()
		deviceID = devices['devices'][0]['id']
		results = spotify.search(q='artist:' + bandStr, type='artist')
		# print(json.dumps(results, sort_keys=True, indent=2))
		artistId = results['artists']['items'][0]['id']
		results = spotify.artist_albums(artistId)
		albums = results['items']
		call = False
		for item in albums:
		    # print("ALBUM: " + item['name'])
		    albumID = item['id']
		    albumArt = item['images'][0]['url']

		    # Extract track data
		    trackResults = spotify.album_tracks(albumID)
		    trackResults = trackResults['items']
		    for item in trackResults:
		    	# print(json.dumps(item['name'].lower(), sort_keys=True, indent=2))
		    	# reduced = item['name'][0:len(songStr)].lower()
		    	if(item['name'].lower()== songStr or item['name'].lower()== songStrExtra):
		    		if(not call):
					    uri = item['uri']
					    trackSelectionList = []
					    trackSelectionList.append(uri)
					    data =spotify.audio_features(item['id'])
					    name = item['name']
					    call = True
					    #print(data)
					    #return json.dumps(data, sort_keys=True, indent=2)
					    #spotify.pause_playback()
					    #print(json.dumps(spotify.current_playback(), sort_keys=True, indent=2))
					    try:
					    	spotify.start_playback(deviceID, None, trackSelectionList)
					    except:
					    	continue
					    #print('\n\n\n')
					    response = spotify.current_playback()
					    #print(json.dumps(response, sort_keys=True, indent=2))
					    while True:
					    	#print(response['is_playing'])
					    	if(response['is_playing']):
					    		break
					    	response = spotify.current_playback()
					    return(bandStr + '#%#' + name + '#$#' + json.dumps(data, sort_keys=True, indent=2))


		    for item in trackResults:
		    	# print(json.dumps(item['name'].lower(), sort_keys=True, indent=2))
		    	reduced = item['name'][0:len(songStr)].lower()
		    	if(reduced == songStr):
		    		if "rehearsal" in item['name'].lower():
		    			continue
		    		if(not call):
					    uri = item['uri']
					    trackSelectionList = []
					    trackSelectionList.append(uri)
					    data =spotify.audio_features(item['id'])
					    name = item['name']
					    call = True	
					    #return json.dumps(data, sort_keys=True, indent=2)
					    #spotify.pause_playback()
					    #print(json.dumps(spotify.current_playback(), sort_keys=True, indent=2))
					    try:
					    	spotify.start_playback(deviceID, None, trackSelectionList)
					    except:
					    	continue
					    #print('\n\n\n')
					    response = spotify.current_playback()
					    #print(json.dumps(response, sort_keys=True, indent=2))
					    while True:
					    	#print(response['is_playing'])
					    	if(response['is_playing']):
					    		break
					    	response = spotify.current_playback()
					    return(bandStr + '#%#' + name + '#$#' + json.dumps(data, sort_keys=True, indent=2))
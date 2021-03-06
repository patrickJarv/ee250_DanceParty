In the COVID-19 world, we are all isolated, so why not convert your Raspberry Pi into a mini dance creator with a scrolling display of your songs while also having an LED that flickers to the beat of the music? So, this project allows you to play these sick beats through your iPhone's Siri. Enjoy!

## Welcome to the Party!
EE250 IOT Project - Spotify API and SiriControl\
By Patrick Jarvis

### Requirements:
You will need:
- An iOS device
- A Spotify Premium account
- A device/laptop that can run Python scripts, SSH to the Raspberry Pi, and open Spotify Web Player
- A Raspberry PI with an LED in **D4** port and the Grove-LCD RGB Backlight in **I2C-3** port
- All of these Python modules
   - sys, mqtt, json, random, time, multiprocessing, spotipy, os, requests , pkgutil, email, imaplib

### Installation and Demonstrations
Note: After doing all nine labs for EE250, I only had to install spotipy
To install Spotipy: run `pip install spotipy --upgrade`\
To link your iOS's Notes to the project's email in order to run the Siri Control click [here](https://drive.google.com/file/d/1wRCpC8f-u29_QZx1BR_u3eci0t-CyRIV/view?usp=sharing).\
To see how to initialize the siri_connector.py, use [this link](https://drive.google.com/file/d/16qXkwm7uudCAdTCI-L9hDtE_yDg3GhUK/view?usp=sharing).\
To see a demonstration of how to run and test the project use [this link](https://drive.google.com/file/d/1NCj5qbpdBkFYDYdTS05wmRlo0hEg2a_6/view?usp=sharing).\
Additional features of the project (for rubric purposes, this is part of my demonstration) are [here](https://drive.google.com/file/d/16or9nAcAfTbg3WXOBbrZLWkcEawUp_qw/view?usp=sharing)

### How to Run (Initialization)
- Clone the repository in both the device/laptop and RPi.
- Link your iOS's Notes Default Account with the project's email (Look at the first link for more help).
  - Project Email Username: ee250projecttemp@gmail.com
  - Project Email Password: EE250temp
- Open up spotifyPlayer.py on your device/laptop and insert your Spotify username at Line 20. Save.
- Run the siri_connector.py on your device/laptop
- Open your device/laptop and open [Spotify](spotify.com) and click "Open Web Player". **Recommended to not do this in a Virtual Machine**
- Say to Siri on your iOS: "Note Spotify test Artist start"
- This will create a Google popup that shows a blank tab but a unique URL. Copy that URL and paste it into the terminal and hit Enter.
- Lastly, run the rpi_client.py on the Raspberry Pi
- You are all set! Now you can use Siri on your iOS and say the below commands to play your songs!
  - To play a song: Say to Siri "Note Spotify Artist *artist_name* Song *song_name*"
    - Example: "Note Spotify Artist Imagon Dragons Song Demons"
  - To quit running: Say "Note quit control"
  
### Writeup of Protocols and Nodes Utilized
 - Documentation found [here](https://docs.google.com/document/d/1AVjEMhZv4gkq3RwCr8Rqr1_Q0uC9sA6JXzk58-4u1Vo/edit?usp=sharing)

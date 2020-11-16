In the COVID-19 world, we are all isolated, so why not convert your Raspberry Pi into a mini dance creator with a scrolling display of your songs while also having an LED that flickers to the beat of the music? This project allows you 

## Welcome to the Party!
EE250 IOT Project - Spotify API and SiriControl\
By Patrick Jarvis

### Requirements:
You will need:
- An iOS with Gmail application
- A device/laptop that can run Python scripts, SSH to the Raspberry Pi, and open Spotify on https://google.com
- A Raspberry PI with an LED in **D4** port and the Grove-LCD RGB Backlight in **I2C-3** port
- All of these Python modules
   - sys, mqtt, json, random, time, multiprocessing. spotipy, os, requests , pkgutil, email, imaplib

### Installation and Demonstrations
Note: After doing all nine labs for EE250, I only had to install spotipy
To install Spotipy: run `pip install spotipy --upgrade`\
To link your iOS's Notes to the project's email in order to run the Siri Control click [here](https://pages.github.com/).\
To see a demonstration of how to run and test the project use [this link](https://google.com/).

### How to Run
- Clone the repository in both the device/laptop and RPi.
- Link your iOS's Notes with the project's email (Look at the first link for more help).
  - Project Email Username: ee250projecttemp@gmail.com
  - Project Email Password: EE250temp
- Run the rpi_client.py on your RPi
- Run the siri_connector.py on your device/laptop
- Open up Google on your device/laptop and open [Spotify](spotify.com) and click "Open Web Player"
- You are all set! Now you can use Siri on your iOS and say the below commands to play your songs!
  - To play a song: Say to Siri "Note Spotify Artist *artist_name* Song *song_name*
    - Example: "Note Spotify Artist Imagon Dragons Song Demons"
  - To quit running: Say "Note quit control"
  

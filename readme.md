
# Spotify track/album control

Simple track and album control for Spotify Connect.

## Bases on 
https://github.com/paulorodriguesxv/python-spotify-remote-control

## Install

pip install -r requirements.txt


## Create a Spotify APP:
    - https://developer.spotify.com/dashboard/login
    - Create a new App
    - Edit the config.yaml and set client id and secret
    - Edit settings and put http://localhost:3000/callback in Redirect URIs field

## Authorize app 
python3 spotify_auth.py and access http://localhost:3000 with your browser to authorize the app

## Run Example

python3 app.py spotify:track:5ECpVZ4c6AndofTaPdtZtV
python3 app.py spotify:album:5ECpVZ4c6AndofTaPdtZtV


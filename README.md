# SPOTIFY BILLBOARD 100 PLAYLIST PROGRAM

A simple program that scrapes the Billboard Hot 100 list from the exact historical day specified and uploads the list into the user's Spotify account as a playlist. Built with PyCharm.

## Description

This program uses BeautifulSoup to scrape the Billboard list on a specific date and then connects to the Spotify Web API via the Spotipy Library in order to upload the list as a playlist in your Spotify account. 

## Getting Started

* Download the zip and unpack.
* Open the project in your Python IDE.
* Install the Spotipy package and generate a `SPOTIPY_CLIENT_ID`, `SPOTIPY_CLIENT_SECRET`, `SPOTIPY_REDIRECT_URI`, and `SPOTIPY_USER_ID` to receive an authorization token to interact with Spotify's API. Instructions here:
* https://spotipy.readthedocs.io/en/2.19.0/#ids-uris-and-urls
* Once you have generated an authorization token and have a `SPOTIPY_CLIENT_ID`, `SPOTIPY_CLIENT_SECRET`, `SPOTIPY_REDIRECT_URI`, and `SPOTIPY_USER_ID`, save these elements as environment variables: 
  <img src="https://github.com/ygyzys83/Spotify-Billboard-Playlist/blob/main/images/variables%201.jpg" width="250" />
* Once environment variables are saved, confirm that the corresponding variable names in `main.py` (lines 11-14) match the environment variable names:
  ```
  SPOTIPY_CLIENT_ID = os.environ.get("SPOTIPY_CLIENT_ID")
  SPOTIPY_CLIENT_SECRET = os.environ.get("SPOTIPY_CLIENT_SECRET")
  SPOTIPY_REDIRECT_URI = os.environ.get("SPOTIPY_REDIRECT_URI")
  SPOTIFY_USER_ID = os.environ.get("SPOTIFY_USER_ID")
  ```
* Run `main.py` and follow the onscreen instructions.

## Authors

* Godman Tan
  * gtprogramming1@gmail.com

"""
Spotify Listening Project
----------------------------

something fun to get back into coding regularly

Started: August 24, 2026
Status: Just getting started!

Goals:
- connect to Spotify
- print out artists + albums

Completed:
- created virtual env for proj
- installed spotipy
- created spotify app + got ID and secret
- created .env file to store ID and secret
- found out some spotipy documentation is outdated??
- note to self, check spotify api docs for latest info
"""

import spotipy, os
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv

# load variables from .env file
load_dotenv()

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(os.getenv("SPOTIPY_CLIENT_ID"),
                                               client_secret=os.getenv("SPOTIPY_CLIENT_SECRET"),
                                               redirect_uri=os.getenv("SPOTIPY_REDIRECT_URI"),
                                               scope="user-library-read"))

"""print(os.getenv("SPOTIPY_CLIENT_ID"))
print(os.getenv("SPOTIPY_CLIENT_SECRET"))
print(os.getenv("SPOTIPY_REDIRECT_URI"))"""


# the ID for benee :)
benee_uri = "spotify:artist:0Cp8WN4V8Tu4QJQwCN5Md4"

# spotify apis docs state the limit can't be more than 10, not 20
results = sp.artist_albums(benee_uri, album_type="album", limit=10)
albums = results['items'] 

# intro to pagination, yay! copied from docs
while results['next']:
    results = sp.next(results)
    albums.extend(results['items'])

for album in albums:
    print(album['name'])
    
print(sp.current_user())
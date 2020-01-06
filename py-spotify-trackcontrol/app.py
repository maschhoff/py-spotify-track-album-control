#
# Based on https://github.com/paulorodriguesxv/python-spotify-remote-control
# Based on https://github.com/bjarneo/Pytify
#
import sys

from pytify.core import get_album_tracks
from pytify.auth import authenticate
from pytify.core import read_config
from pytify.core import play


_auth = authenticate(read_config())

# with arguments_data_manager = DataManager()
if len(sys.argv) > 1:
    print("SporitfyConnect")
    spotifyuri = sys.argv[1]
    tracklist=[]
    if "album" in spotifyuri:
        print('Album')
        split=spotifyuri.split(':')
        results = get_album_tracks(split[2], _auth)
        tracks=results['items']
        for track in tracks:
            tracklist.append(track['uri'])
        #print(tracklist)
    elif "track" in spotifyuri:
        print('Track')
        tracklist.append(spotifyuri)
    else:
        print('Not supported jet!')
    print("Start playing!")
    play(tracklist, _auth)
    exit()
else:
    print("ERROR: SpotifyURL Parameter missing!")
    exit()

    

#
# Based on https://github.com/paulorodriguesxv/python-spotify-remote-control
# Based on https://github.com/bjarneo/Pytify
#
import sys

from pytify.core import get_album_tracks
from pytify.auth import authenticate
from pytify.core import read_config
from pytify.core import play




def init():
    if len(sys.argv) > 1:
        spotifyuri = sys.argv[1]
        play_uri(spotifyuri)
    else:
        print("ERROR: SpotifyURL Parameter missing!")
        exit()

def play_uri(spotifyuri):

    
    print("SporitfyConnect")
    _auth = authenticate(read_config())
    tracklist=[]
    if "album" in spotifyuri:
        print('Album')
        split=spotifyuri.split(':')
        results = get_album_tracks(split[2], _auth)
        tracks=results['items']
        for track in tracks:
            tracklist.append(track['uri'])
    elif "track" in spotifyuri:
        print('Track')
        tracklist.append(spotifyuri)
    else:
        print('Not supported jet!')
    print("Start playing!")
    play(tracklist, _auth)
    exit()

if __name__ == '__main__':
    init()
    

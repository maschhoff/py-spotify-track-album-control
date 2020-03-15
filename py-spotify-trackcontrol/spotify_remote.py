#
#Basedon https://github.com/paulorodriguesxv/python-spotify-remote-control
#Basedon https://github.com/bjarneo/Pytify
#
import sys

from pytify.core import get_album_tracks
from pytify.auth import authenticate
from pytify.core import read_config
from pytify.core import play
from pytify.core import playdev
from pytify.core import list_devices




def init():
	if len(sys.argv)>2:
		spotifyuri=sys.argv[1]
		spotifydevice=sys.argv[2]
		play_uri(spotifyuri,spotifydevice)
	else:
		print("ERROR: Spotify Parameter missing! url or device_name")
		exit()

def stop(device_name):
	_auth=authenticate(read_config())
	dev_id=""
	spdevices=list_devices(_auth)
	#print(spdevices)
	for dev in spdevices['devices']:
		if device_name == dev['name']:
			dev_id=dev['id']
	
	#Set device_name as player
	print("Set Player: "+device_name)
	playdev(dev_id,False,_auth)
	
def resume(device_name):
	_auth=authenticate(read_config())
	dev_id=""
	spdevices=list_devices(_auth)
	#print(spdevices)
	for dev in spdevices['devices']:
		if device_name == dev['name']:
			dev_id=dev['id']
	
	#Set device_name as player
	print("Set Player: "+device_name)
	playdev(dev_id,False,_auth)

def play_uri(spotifyuri,device_name):

	print("SporitfyConnect")
	_auth=authenticate(read_config())
	
	#get device id from device name
	dev_id=""
	spdevices=list_devices(_auth)
	#print(spdevices)
	for dev in spdevices['devices']:
		if device_name == dev['name']:
			dev_id=dev['id']
	
	#Set device_name as player
	print("Set Player: "+device_name)
	playdev(dev_id,True,_auth)
	
	#Track or Album
	print("Track: "+spotifyuri)
	tracklist=[]
	if "album" in spotifyuri:
		print('is Album')
		split=spotifyuri.split(':')
		results=get_album_tracks(split[2],_auth)
		tracks=results['items']
		for track in tracks:
			tracklist.append(track['uri'])
	elif "track" in spotifyuri:
		print('is Track')
		tracklist.append(spotifyuri)
	else:
		print('Notsupportedjet!')
	
	#Play
	print("Start playing!")
	play(tracklist,_auth)
	#exit()

if __name__=='__main__':
	init()


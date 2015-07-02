#!/usr/bin/python

import feedparser
import urllib.request
import urllib.parse
import json
import time

url = 'https://api.telegram.org/'
botkey = 'bot122232540:AAHDFXIuQOzCaO0XGlBAGNdlcy5rLDYQ0O8'
offset = 0

helptext = '''I can help you spot the International Space Station passing overhead.

/help - this text.
/now - where is the station right now?
/spot (latitude) (longitude) - when will the station pass over me?

(Or just reply with a Telegram location)'''

def getUpdates(offset=0,timeout=0):
	parameters = {
	'offset':offset,
	'timeout':timeout
	}
	tosend = urllib.parse.urlencode(parameters)
	with urllib.request.urlopen(url + botkey + '/getUpdates?' + tosend) as f:
		data = json.loads(f.read().decode('utf-8'))
	return(data['result'])

def processUpdate(update):
	from_id = update['message']['chat']['id']
	message_id = update['message']['message_id']
	
	if 'location' in update['message']:
		iss = spaceStationPass(update['message']['location']['latitude'], update['message']['location']['longitude'])
		sendMessage(from_id, iss, message_id)
	
	elif 'text' in update['message']:
		text = update['message']['text']
		cmd = text.split(' ',1)[0]
		if cmd == '/help':
			sendMessage(from_id, helptext, message_id)

		elif cmd == '/spot':
			try:
				arguments = text.split(' ',1)[1]
				iss = spaceStationPass(arguments.split(' ')[0], arguments.split(' ')[1])
				sendMessage(from_id, iss, message_id)
			except IndexError:
				pass
		
		elif cmd == '/now':
			iss = spaceStationNow()
			sendLocation(from_id, iss['latitude'], iss['longitude'], message_id)
			
	
def sendMessage(to, text, reply=False):
	parameters = {
	'chat_id':to,
	'text':text
	}
	
	if reply:
		parameters['reply_to_message_id'] = reply
	
	tosend = urllib.parse.urlencode(parameters).encode('utf-8')
	urllib.request.urlopen(url + botkey + '/sendMessage?', tosend)
	
def sendLocation(to, latitude, longitude, reply=False):
	parameters = {
	'chat_id':to,
	'latitude':latitude,
	'longitude':longitude
	}
	
	if reply:
		parameters['reply_to_message_id'] = reply
	
	tosend = urllib.parse.urlencode(parameters).encode('utf-8')
	urllib.request.urlopen(url + botkey + '/sendLocation?', tosend)
	
def spaceStationPass(latitude, longitude):
	with urllib.request.urlopen('http://api.open-notify.org/iss-pass.json?lat=' + str(latitude) + '&lon=' + str(longitude)) as f:
		issdata = json.loads(f.read().decode('utf-8'))
	nextpass = "The next time the ISS will pass overhead will be at"
	nextpass += time.strftime('%d %B at %H:%M UTC', time.gmtime(issdata['response'][0]['risetime']))
	nextpass += " for " + str(issdata['response'][0]['duration']) + " seconds."
	return nextpass

def spaceStationNow():
	with urllib.request.urlopen('http://api.open-notify.org/iss-now.json') as f:
		issdata = json.loads(f.read().decode('utf-8'))
	return issdata['iss_position']

while True:
	updates = getUpdates(offset, 10)
	if updates:
		offset = updates[-1]['update_id'] + 1
		
		for update in updates:
			processUpdate(update)



		

#!/usr/bin/python

import feedparser
import urllib.request
import urllib.parse
import json

url = 'https://api.telegram.org/'
botkey = 'bot122232540:AAHDFXIuQOzCaO0XGlBAGNdlcy5rLDYQ0O8'
offset = 0

helptext = '''I'm a bot who can help you spot the International Space Station passing overhead.

/help - this text.'''

def getUpdates(offset=0,timeout=0):
	with urllib.request.urlopen(url + botkey + '/getUpdates?offset=' + str(offset) + '&timeout=' + str(timeout)) as f:
		data = json.loads(f.read().decode('utf-8'))
	return(data['result'])

def processUpdate(update):
	from_id = update['message']['from']['id']
	text = update['message']['text']
	message_id = update['message']['message_id']
	if text == "/help":
		sendMessage(from_id, helptext, message_id)
	
def sendMessage(to, text, reply=False):
	parameters = {
	'chat_id':to,
	'text':text
	}
	
	if reply:
		parameters['reply_to_message_id'] = reply
	
	tosend = urllib.parse.urlencode(parameters).encode('utf-8')
	urllib.request.urlopen(url + botkey + '/sendMessage?', tosend)
	
while True:
	updates = getUpdates(offset, 10)
	if updates:
		offset = updates[-1]['update_id'] + 1
		
		for update in updates:
			processUpdate(update)



		

#!/usr/bin/python

import feedparser
import urllib.request
import json

url = 'https://api.telegram.org/'
botkey = 'bot122232540:AAHDFXIuQOzCaO0XGlBAGNdlcy5rLDYQ0O8'
offset = 0

def getUpdates(offset=0,timeout=0):
	with urllib.request.urlopen(url + botkey + '/getUpdates?offset=' + str(offset) + '&timeout=' + str(timeout)) as f:
		data = json.loads(f.read().decode('utf-8'))
	return(data['result'])

def processUpdate(update):
	print(update['message']['text'])

while True:
	updates = getUpdates(offset, 10)
	if updates:
		offset = updates[-1]['update_id'] + 1
		
		for update in updates:
			processUpdate(update)



		

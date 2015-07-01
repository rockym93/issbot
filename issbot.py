#!/usr/bin/python

import feedparser
import urllib.request
import json

offset = '0'
url = 'https://api.telegram.org/'
botkey = 'bot122232540:AAHDFXIuQOzCaO0XGlBAGNdlcy5rLDYQ0O8'

while True:
	with urllib.request.urlopen(url + botkey + '/getUpdates?offset=' + offset) as f:
		data = json.loads(f.read().decode('utf-8'))
	
	for update in data['result']:
		offset = str(update['update_id'])
		print(offset)
		print(update['message']['text'])
		

		

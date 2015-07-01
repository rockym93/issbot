#!/usr/bin/python

import feedparser
import urllib.request
import json

url = 'https://api.telegram.org/'
botkey = 'bot122232540:AAHDFXIuQOzCaO0XGlBAGNdlcy5rLDYQ0O8'
offset = 0
timeout = 10

while True:
	with urllib.request.urlopen(url + botkey + '/getUpdates?offset=' + str(offset) + '&timeout=' + str(timeout)) as f:
		data = json.loads(f.read().decode('utf-8'))
	if data['result']:
		for update in data['result']:
			print(update['message']['text'])
		offset = data['result'][-1]['update_id'] + 1
	else:
		print("Nothing new to report.")
		

		

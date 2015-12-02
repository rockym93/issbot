#!/usr/bin/env python

import lazybot as bot

import urllib
import json
import sys
import time

data = json.load(sys.stdin)

with open('key.txt') as f:
	bot.key = f.read().rstrip()

def pass(latitude, longitude):
	'''generic function for grabbing pass data given latitude and longitude'''
	with urllib.request.urlopen('http://api.open-notify.org/iss-pass.json?lat=' + str(latitude) + '&lon=' + str(longitude)) as f:
		issdata = json.loads(f.read().decode('utf-8'))
	nextpass = "The next time the ISS will pass overhead will be "
	nextpass += time.strftime('%d %B at %H:%M UTC', time.gmtime(issdata['response'][0]['risetime']))
	nextpass += " for " + str(issdata['response'][0]['duration']) + " seconds."
	return nextpass


### Command Definitions ###

def help(message):
	helptext = '''I can help you spot the International Space Station passing overhead.

Send me a location to get pass predictions, or /now to see where the station is right now.'''
	tosend = {
	'chat_id': message['chat']['id'],
	'reply_to_message': message['message_id'],
	'text': helptext
	}
	bot.api('sendMessage', tosend)

def now(message):
	with urllib.request.urlopen('http://api.open-notify.org/iss-now.json') as f:
		issdata = json.loads(f.read().decode('utf-8'))
	latitude = issdata['iss_position']['latitude']
	longitude = issdata['iss_position']['longitude']
	tosend = {
	'chat_id': message['chat']['id'],
	'reply_to_message': message['message_id'],
	'latitude': latitude,
	'longitude': longitude,
	}
	bot.api('sendLocation', tosend)

bot.commands['/now'] = now

def location(message):
	latitude = message['location']['latitude']
	longitude = message['location']['longitude']
	
	tosend = {
	'chat_id': message['chat']['id'],
	'reply_to_message': message['message_id'],
	'text': "The ISS will next pass over your location at " + pass(latitude, longitude)
	}
	bot.api('sendMessage', tosend)

bot.handlers['location'] = location

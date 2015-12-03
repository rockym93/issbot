#!/usr/bin/env python3

import lazybot as bot

import requests

import time

def isspass(latitude, longitude):
	'''generic function for grabbing pass data given latitude and longitude'''
	issdata = requests.get('http://api.open-notify.org/iss-pass.json?lat=' + str(latitude) + '&lon=' + str(longitude)).json()
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
	issdata = requests.get('http://api.open-notify.org/iss-now.json').json()
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
	'text': isspass(latitude, longitude)
	}
	bot.api('sendMessage', tosend)

bot.handlers['location'] = location

### END COMMAND DEFINITIONS ###

bot.processupdate()

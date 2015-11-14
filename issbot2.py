#!/usr/bin/env python

import lazybot as bot

import urllib
import json
import sys

data = json.load(sys.stdin)

with key.txt as f:
	bot.key = f.read()

def pass(latitude, longitude):
'''generic function for grabbing pass data given latitude and longitude'''
# Insert that here.


### Command Definitions ###

def now(message):
	# Insert now-fetching function here
	tosend = {
	'chat_id': message['chat']['id'],
	'reply_to_message': message['message_id'],
	'latitude': latitude,
	'longitude': longitude,
	}
	bot.api('sendLocation', tosend)

bot.commands['/now'] = now

def here(message):
	# Extract latitude and longitude from input
	
	tosend = {
	'chat_id': message['chat']['id'],
	'reply_to_message': message['message_id'],
	'text': "The ISS will next pass over your location at " + pass(lat, long)
	}
	bot.api('sendMessage', tosend)

bot.commands['/here'] = here

def location(message):
	lat = message['location']['latitude']
	long = message['location']['longitude']
	
	tosend = {
	'chat_id': message['chat']['id'],
	'reply_to_message': message['message_id'],
	'text': "The ISS will next pass over your location at " + pass(lat, long)
	}
	bot.api('sendMessage', tosend)

bot.handlers['location'] = location

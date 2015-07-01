#!/usr/bin/python

import feedparser
import urllib.request
import json

with urllib.request.urlopen('https://api.telegram.org/bot122232540:AAHDFXIuQOzCaO0XGlBAGNdlcy5rLDYQ0O8/getUpdates') as f:
	data = json.loads(f.read().decode('utf-8'))

print(data)

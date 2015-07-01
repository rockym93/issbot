#!/usr/bin/python

import feedparser
import urllib.request

with urllib.request.urlopen('https://api.telegram.org/bot122232540:AAHDFXIuQOzCaO0XGlBAGNdlcy5rLDYQ0O8/getUpdates') as f:
	print(f.read())

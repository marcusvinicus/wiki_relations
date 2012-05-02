#!/usr/bin/env python

"""
This package shows that it is possible to connect wikipedians 
based on the pages that they edit in commom. The ideia is to connect
then based on interest areas.
"""

WIKI_URL = "http://en.wikipedia.org/w/api.php?"
API_CMD = "action=query&list=usercontribs&format=json&uclimit=500&ucuser=%s"

from sys import stdout
from urllib import urlopen
import json

class User:
	
	def __init__(self, login):
		self.login = login
		url = ''.join([WIKI_URL, API_CMD]) % self.login
		stdout.write ("Downloading %s's complete list of edited pages" % self.login)
		self.pages = self.get_all_pages(url)
		print (self)

	def __str__(self):
		result = (self.login + " has edited " + str(len(self.pages)) + " pages.")
		pages = []
		#for page_id, page_title in self.pages.iteritems():
		#	pages.append('\n ' + page_title + " (" +  page_id + ")")
		result = result + ''.join(pages)
		return result.encode('utf-8','replace')

	def get_all_pages(self, url, url_continue=''):
		stdout.write('.')
		stdout.flush()
		pages = {}
		data = json.load(urlopen(url+url_continue))
		usercontribs = data['query']['usercontribs']
		for contrib in usercontribs:
			page_id = contrib['pageid']
			page_title = contrib['title']
			pages[page_id] = page_title

		if 'query-continue' in data:
			ucstart = data['query-continue']['usercontribs']['ucstart']
			more_pages = self.get_all_pages(url, '&ucstart=%s' % ucstart)
			return dict(pages.items() + more_pages.items())
		else:
			print
			return pages


class Page:
	def __init__(self):
		pass

	def __str__(self):
		pass


def main():
	jimbo = User("Jimbo_Wales")
	filelakeshoe = User("Filelakeshoe")

if __name__ == "__main__":
	
	result = main()
	exit(result)
#!/usr/bin/env python

"""
This package shows that it is possible to connect wikipedians 
based on the pages that they edit in commom. The ideia is to connect
then based on interest areas.
"""

WIKI_URL = "http://en.wikipedia.org/w/api.php?"
API_CMD = "action=query&list=usercontribs&format=xml&uclimit=500&ucuser=%s"

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
		dom = minidom.parse(urlopen(url+url_continue))
		query = dom.getElementsByTagName('query').item(0)
		usercontribs = query.getElementsByTagName('usercontribs').item(0)
		for item in usercontribs.getElementsByTagName('item'):
			page_id = item.getAttribute('pageid')
			page_title = item.getAttribute('title')
			pages[page_id] = page_title
		query_continue = dom.getElementsByTagName('query-continue').item(0)
		if query_continue:
			usercontribs = query_continue.getElementsByTagName('usercontribs').item(0)
			ucstart = usercontribs.getAttribute('ucstart')
			more_pages = self.get_all_pages(url,'&ucstart=%s' % ucstart)
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
	from urllib import urlopen
	from xml.dom import minidom
	from sys import stdout
	result = main()
	exit(result)
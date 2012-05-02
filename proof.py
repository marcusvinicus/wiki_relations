#!/usr/bin/env python

"""
This package shows that it is possible to connect wikipedians 
based on the pages that they edit in commom. The ideia is to connect
then based on interest areas.
"""

WIKI_URL = "http://en.wikipedia.org/w/api.php?"
API_CMD = "action=query&list=usercontribs&format=xml&uclimit=100&ucuser=%s"

class User:
	def __init__(self, login):
		self.login = login
		self.pages = self.get_pages()

	def __str__(self):
		print self.login + ",", len(self.pages), "pages edited"
		print "-"*60
		for page_id, page_title in self.pages.iteritems():
			print page_title, "(" + page_id + ")"
		print "-"*60
		return ''

	def get_pages(self):
		pages = {}
		url = ''.join([WIKI_URL, API_CMD]) % self.login

		dom = minidom.parse(urlopen(url))
		query = dom.getElementsByTagName('query').item(0)
		usercontribs = query.getElementsByTagName('usercontribs').item(0)
		for item in usercontribs.getElementsByTagName('item'):
			page_id = item.getAttribute('pageid')
			page_title = item.getAttribute('title')
			pages[page_id] = page_title
		return pages


class Page:
	def __init__(self):
		pass

	def __str__(self):
		pass


def main():
	user = User("Jimbo_Wales")
	print user

	


if __name__ == "__main__":
	from urllib import urlopen
	from xml.dom import minidom
	result = main()
	exit(result)
"""Crawler 1.0 in python. 
It uses urllib2,urlparse and BeautifulSoup.

This program can be executed by the following command:
>>python crawlaway.py http://www.google.com

Hope it helps :) """


import sys
import re
import urllib2
import urlparse
from BeautifulSoup import BeautifulSoup
tocrawl = set([sys.argv[1]])                        #Acts like a stack; with add() and pop() functions;
crawled = set([])                                   #Same as tocrawl


i = 0
while i < 5:                                        #For now only five entries. You can increase it to whichever number you like
    i = i + 1
    try:
        crawling = tocrawl.pop()
        print crawling
    except:
        raise StopIteration
    url = urlparse.urlparse(crawling)
    try:
        data = urllib2.urlopen(crawling).read()
    except:
        continue
    soup = BeautifulSoup(data)
    print soup.title                                #To display the title of a given page
    links = soup.findAll('a', href=True)
    crawled.add(crawling)                           #As the page has been crawled and should not be crawled again
    for link in links:
        href = link.get('href')
        """ Here depending on what <a href=".." we have to contruct 
            different end urls which it has to hit. For example:
            <a href="http://twitter.com"> will just hit the url.
            Whereas if it is,
            <a href="#contact"> it will be: "http://twitter.com#contact"""
        if href.startswith('/'):
            href = 'http://' + url[1] + href
        elif href.startswith('#'):
            href = 'http://' + url[1] + '/' + url[2] + href
        elif not href.startswith('http'):
            href = 'http://' + url[1] + '/' + href
        if href not in crawled:
            tocrawl.add(href)                       #Finally adding the constructed link to the stack

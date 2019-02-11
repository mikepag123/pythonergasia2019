import urllib2
import re

#syndesh se ena URL
webs = raw_input('Dwste link: ')
website = urllib2.urlopen(webs)

#diabase html code
html = website.read()

#use re.findall to get all the links

links = re.findall('"((http|ftp)s?://.*?)"', html)

print len(links)

# included many vairations of the '<br>' tag
breaks = re.findall('<br>|<br/>|<br />|\n', html)
print len(breaks)

# The intent of this script to better understand interacting with websites both behind the scenes and via a browser.
""" 
Search google for a random image based upon a random word.  Print each step to the console and display the image.
"""

# IMPORTS
import sys
import re
import argparse
import os 
import os.path
import image
import urllib
import urlparse
import webbrowser
import mechanize
from bs4 import BeautifulSoup  # currently using the html5lib parser due to trouble installing lxml

br = mechanize.Browser()
br.set_handle_robots(False)
br.addheaders = [('User-agent','chrome')]



#--try this selenium stuff later--
# parseArg = argparse.ArgumentParser(description = 'Grab a random image based upon a random word')
# parseArg.add_argument("-se", "--selenium", help="Should the script use selenium to access the browser?", action="store_true")
# args = parseArg.parse_args()
# want to perform the actions in the browser itself if the script is told to use selenium
# otherwise (default) I will go ahead and grab all content without the browser's help



def getRandomWord():
	"""Pull a random word from wordgenerator.setgetgo.com/get.php"""

	tester = BeautifulSoup(br.open("http://randomword.setgetgo.com/get.php").read())
	searchText = tester.body.get_text()
	searchText = searchText.replace(" ","+").strip()  # remove new lines and replace spaces with +
	return searchText


def findImage(searchText): 
	"""Pull the first image from a google image search"""
	# https://www.google.com/search?site=imghp&tbm=isch&source=hp&biw=956&bih=1074&q=<searchText>&oq=<searchText>
	# <div class="rg_di" data-ri="0">
	#	<a>
	#		<img class="rg_i">

	query = "http://www.google.com/search?site=imghp&tbm=isch&q="+searchText
	page = BeautifulSoup(br.open(query).read())
	searchDiv = page.find_all('div',attrs={'id':'search'})
	searchDiv = BeautifulSoup(str(searchDiv[0]))
	links = searchDiv.find_all('a')
	img_source = links[0].find('img')['src']
	return img_source


def saveFile(rawFile):
	"""Save a given file to the current working directory"""
	


def pwd(rel = "."):
	"""print the current working directory or its parent directory"""
	if (rel == ".") or (rel == "current"):
		return os.getcwd()
	elif (rel == "..") or (rel == "previous"):
		targetdir = os.getcwd() # get the current working directory
		targetdir = targetdir.split("/")
		targetdir = targetdir[0:-1] #remove the last leg of the directory
		parentdir = targetdir[0]
		for x in targetdir[1:]:  #reassemble the pieces
			parentdir += "/" + x
		return parentdir
	else:
		raise ValueError("Valid Args: '.','..','current','previous'")

print getRandomWord()
print findImage('hulk')
print findImage(getRandomWord())

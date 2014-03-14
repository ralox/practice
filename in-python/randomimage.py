# The intent of this script to better understand interacting with the browser both behind the scenes and directly.
""" 
Search google for a random image based upon a random word.  Print each step to the console and display the image.
"""

# IMPORTS
import sys
import argparse
import os 
import os.path
import urllib
import urlparse
import webbrowser
import mechanize
from bs4 import BeautifulSoup  # currently using the html5lib parser due to trouble installing lxml

browser = mechanize.Browser()
browser.set_handle_robots(False)
browser.addheaders = [('User-agent','chrome')]


# parseArg = argparse.ArgumentParser(description = 'Grab a random image based upon a random word')
# parseArg.add_argument("-se", "--selenium", help="Should the script use selenium to access the browser?", action="store_true")
# args = parseArg.parse_args()
#--try this selenium stuff later--
# want to perform the actions in the browser itself if the script is told to use selenium
# otherwise (default) I will go ahead and grab all content without the browser's help


def getRandomWord():
	"""
	Pull a random word from wordgenerator.net
	"""
	# www.wordgenerator.net/random-word-generator.php
	# plain text (not the <p>) within <strong id="rname">
	
	soup = BeautifulSoup(browser.open("www.wordgenerator.net/random-word-generator.php"))
	searchText = soup.strong
	searchText = searchText.replace(" ","+")  # google replaces spaces in a search term with +


def grabImage(searchText): 
	"""
	Pull the first image from a google image search
	"""
	# https://www.google.com/search?site=imghp&tbm=isch&source=hp&biw=956&bih=1074&q=<searchText>&oq=<searchText>
	
	# <div class="rg_di" data-ri="0">
	#	<a>
	#		<img class="rg_i">

	query = "https://www.google.com/search?site=imghp&tbm=isch&source=hp&biw=956&bih=1074&q="+searchText+"&oq="+searchText


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




soup = BeautifulSoup(browser.open("www.wordgenerator.net/random-word-generator.php").read())
searchText = soup.strong
print searchText

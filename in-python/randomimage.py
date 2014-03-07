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
import webbrowser


parseArg = argparse.ArgumentParser(description = 'Grab a random image based upon a random word')
parseArg.add_argument("-se", "--selenium", help="Should the script use selenium to access the browser?", action="store_true", type=bool)
args = parseArg.parse_args()

# want to perform the actions in the browser itself if the script is told to use selenium
# otherwise (default) I will go ahead and grab all content without the browser's help

def readSite(url):
	"""Get the contents of the given url"""
	if ( args.selenium = false):
		return urllib.urlopen(url)
	else:
		webbrowser.open(url) #don't know yet if I need to open a new browser or use an existing one...
	


def parseRandomWord(siteContent):
	"""Pull the random word from the contents of the readSite run"""


def grabImage(siteContent) 
	"""Pull the image from the contents of the readSite run"""







def pwd(rel = "."):
	"""print the current working directory or its parent directory"""
	if (rel == ".") or (rel == "current"):
		return os.getcwd()
	elif (rel == "..") or (rel == "previous"):
		targetdir = os.getcwd() #get the current working directory
		targetdir = targetdir.split("/")
		targetdir = targetdir[0:-1] #remove the last leg of the directory
		parentdir = targetdir[0]
		for x in targetdir[1:]:  #reassemble the pieces
			parentdir += "/" + x
		return parentdir
	else:
		raise ValueError("Valid Args: '.','..','current','previous'")




webpage1 = readSite("http://barnett.cc")
print webpage1.headers

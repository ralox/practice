#Practice file for exploring Python's features.  Primary focus is Modules and Object-Oriented principles
"""This is a module about modules.  Whatup.
"""

# IMPORTS
import time
import os  #allows a crap ton of file, directory, and process activities!
	# chdir, chmod, chown, dup, stat, rename, link, symlink, unlink, remove, listdir, mkdir, open, read, 
	# urandom, wait, ...etc.
import os.path
import urllib

# Use the following format to import specific methods:
# from time import asctime

def getTime():
	"""useless method that just prints the return from asctime""" 
	return time.asctime()


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


def ls(directory):
	"""return the contents of the given directory."""
	return os.listdir(directory)


def wget(url):
	"""return the contents of a webpage"""
	return urllib.urlopen(url)


print getTime()
print pwd()
print pwd("previous")
print ls(pwd(".."))
webpage = wget("http://barnett.cc")
print webpage.headers

# this is my hello world script which is intended to help me learn the basics of Python
# each piece returns a value that allows me to evaluate the snippet's successful functionality


# import
#--------------------------------------------------
import sys
baseval = int(sys.argv[1])


# simple math
#--------------------------------------------------
x = 2 * 4 * 8 / 32
print "2*(4)*8/32=",x
def dosomemath(y):
	a=y/2
	b=y*2
	c=y**2*2
	return a * y * b / c
resval = dosomemath(baseval)
print "Replacing 4 with",baseval,"results in",resval


# perform a count
#--------------------------------------------------
def count_digits(digits):
	digits=str(digits)
	return len(digits)
print "The result is",count_digits(resval),"digits long."


# compare values
#--------------------------------------------------
def areEqual(var1, var2):
	try:
		return var1.upper() == var2.upper()
	except AttributeError:
		return var1 == var2
print "Jedi is the same as jedi? ",areEqual("jedi", "Jedi")	


# list play
#--------------------------------------------------
mylist = ["Ava","Jon","Jeff","Tyler","Amanda"]
intlist = range(resval,baseval+1)
ziplist = zip(mylist, range(len(mylist)))
print "My 3 best closest pals are",mylist[:3]
print "The range of the values given earlier is:",intlist
print "The reverse of that list is:",intlist[::-1]
print "Ziping the lists creates:", ziplist


# looping
#--------------------------------------------------
def sum(xlist):
	retval = xlist[0]
	for x in xlist[1:]:
		retval += x
	return retval	
def product(myList):
	newNum = myList[0]
	for x in myList[1:]:
		newNum = newNum * x
	return newNum
def factorial(myNum):
	return product(range(1,myNum+1))
def reverse(myList):
	# Don't actually do this crap btw.  This can be accomplished
	# more efficiently using list splicing
	length = len(myList)  
	newList = [0]*length  # just to create a list with the exact same number of slots 
	for x in range(length):
		newList[x] = myList[length-(x+1)]
	return newList
print "add the numbers to get:",sum(intlist)
print "add the names to get:",sum(mylist)
print "factorial of 4 is:",factorial(4)
print "put your thang down, flip it and reverse it:",reverse(mylist)
print "minimums are:",min(mylist),"and",min(intlist)
print "maximums are:",max(mylist),"and",max(intlist)


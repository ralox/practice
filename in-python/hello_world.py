# this is my hello world script which is intended to help me learn the basics of Python
# each piece returns a value that allows me to evaluate the snippet's successful functionality


# import
import sys
baseval = int(sys.argv[1])


# simple math
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
def count_digits(digits):
	digits=str(digits)
	return len(digits)
print "The result is",count_digits(resval),"digits long."


# compare values
def areEqual(var1, var2):
	try:
		return var1.upper() == var2.upper()
	except AttributeError:
		return var1 == var2
print "Jedi is the same as jedi? ",areEqual("jedi", "Jedi")	


# list play
mylist = ["Ava","Jon","Jeff","Tyler","Amanda"]
intlist = range(resval,baseval+1)
print "My 3 best closest pals are",mylist[:3]
print "The range of the values given earlier is:",intlist
print "The reverse of that list is:",intlist[::-1]

# looping
def sum(xlist):
	retval = xlist[0]
	for x in xlist[1:]:
		retval += x
	return retval	
print sum(intlist)
print sum(mylist)




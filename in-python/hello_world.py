# this is my hello world script which is intended to help me learn the basics of Python
# each piece returns a value that allows me to evaluate the snippet's successful functionality


# import
#--------------------------------------------------
import sys
baseval = int(sys.argv[1]) #this single argument is set when calling the script. It is required.


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


# compare values
#--------------------------------------------------


# Lists
#--------------------------------------------------
mylist = ["Ava","Jon","Jeff","Tyler","Amanda"]
intlist = range(resval,baseval+1)
ziplist = zip(mylist, range(len(mylist)))
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
	# Don't actually do it this way. 
	# instead:  listname[::-1] 
	length = len(myList)  
	newList = [0]*length  # create same number of slots 
	for x in range(length):
		newList[x] = myList[length-(x+1)]
	return newList

print "add the numbers to get:",sum(intlist)
print "My 3 best closest pals are",mylist[:3]
print "The range of the values given earlier is:",intlist
print "The reverse of that list is:",intlist[::-1]
print "Ziping the lists creates:", ziplist
print "add the names to get:",sum(mylist)
print "factorial of 4 is:",factorial(4)
print "put your thang down, flip it and reverse it:",reverse(mylist)
print "minimums are:",min(mylist),"and",min(intlist)
print "maximums are:",max(mylist),"and",max(intlist)
print "sort pals alphabetically: ", mylist.sort() # rearranges the list alphabetically or numerically
print "copy my pals list and sorty it: ", sorted(mylist) # creates a sorted COPY of the list


# Function Definition
#--------------------------------------------------
def defaultValues(x=1,z=5):
	#by default, x is 1 and z is 5
	temp = (x** 2) * z - z 
	return temp
def multiUse(x):
	x = x * x
	return x
print map(multiUse, range(6)) #map = run a function over each list element, passing the elements as arguments
print defaultValues()
print defaultValues(x=3,z=10)


# String
#--------------------------------------------------
wordy = "corn, beef, hash, pablo"
checkbee = "bee" in wordy #should be true
checkant = "ant" in wordy #should be false
splitter = wordy.split(',') #creates a list using the comma as a delimeter
joiner = ",".join(mylist) #brings the strings together into one big fucking string with commas in it
striper = wordy.strip("onrclabp, ") #remove the characters from the beginning and the end of the string
substituter = "I'm going to add %s and %s to this sentence" % ("one word", "then another") #should do what it says 
def count_digits(digits):
	digits=str(digits)
	return len(digits)
def areEqual(var1, var2):
	try:
		return var1.upper() == var2.upper()
	except AttributeError:
		return var1 == var2

print "Jedi is the same as jedi? ",areEqual("jedi", "Jedi")	
print "The result is",count_digits(resval),"digits long."
print "Example string: ", wordy
print "does this string contain 'bee'...expect True: ", checkbee
print "does the same string contain 'ant'...expect False: ", checkant
print "split the aforementioned string into a list: ", splitter
print "take my list of pals and jam it into a single string: ", joiner
print "take the characters [cornapbl, ] of each end of the string: ", striper
print substituter


# File Manipulation
#--------------------------------------------------
exampleFile = open('example.txt', 'r') #open the file in read mode
copyFile = open('copy.txt', 'w') #create a new file in write mode
copyFile.write(exampleFile.read()) #make a copy of the example file
exampleFile.close() 
copyFile.close()
copyFile = open('copy.txt', 'r')
print copyFile.read()
copyFile.close()
copyFile = open('copy.txt', 'w')
copyFile.write("The Star Wars text has been overwritten.")
copyFile.close()
copyFile = open('copy.txt', 'a') #open the file in append mode
copyFile.write("Append this line.")
copyFile.close()
copyFile = open('copy.txt', 'r')
print copyFile.read()
copyFile.close()


# Dictionaries
#--------------------------------------------------
dictionary1 = {"jon":"Sneoux","jeff":"Skez","dave":"Ralox","family":"Solar"}
for key, value in dictionary1.items(): print key, value  #print everything via a for loop
#print dictionary1.keys() #would print all of the keys
#print dictionary1.values() #would print all of the values
print dictionary1["jeff"] + " was the first of the " + dictionary1["family"] + " family"
print dictionary1.get("tyler", "That name was not found") #will print the default answer because 'tyler' is not in the dictionary
print dictionary1.get("dave", "That name was not found") #will print Ralox because 'dave' is in the dictionary
#dictionary1.setdefault("That name was not found") #would do the same as the line above
#ALL global and local variables are stored in dictionaries
print globals() #within a smaller context, use locals()





#this is my normal hello world script

print "hey there, world, what up?"

x = 2 * 4 * 8 / 32
print "I really like the number",x

def dosomemath(y=4):
	a=y/2
	b=y*2
	c=y**2*2
	return a * y * b / c

print "The machine likes the number",dosomemath()

def count_digits(digits):
	digits=str(digits)
	return len(digits)

print count_digits(1234567890)

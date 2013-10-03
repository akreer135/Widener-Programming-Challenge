from sys import argv
script, arg1, arg2 = argv
arg1 = int(arg1)
arg2 = int(arg2)
print "Input: %d, %d" %(arg1, arg2)
output = 0
def add(x):
	global output
	output+=x
if arg1<arg2:
	map(add, range(arg1, arg2+1))
else:
	map(add, range(arg2, arg1+1))
print "Output:", output

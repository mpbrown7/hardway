#create a variable with four %r's
formatter = "%r %r %r %r"

#print the variable formatter after 1,2,3,4 are passed to it.
print formatter % (1, 2, 3, 4)
#print the variable after four strings are passed to it
print formatter % ("one", "two", "three", "four")
#print the variable after four strings are passed to it, though special strings
print formatter % (True, False, False, True)
#print the variable with itself passed to it, so it literaly prints the %r %r %r %r
print formatter % (formatter, formatter, formatter, formatter)
#print the four strings on one line due to the comma between them
#the third string is printed with "" around it due to the '
print formatter % (
	"I had this thing.",
	"That you could type up right.",
	"But it didn't sing.",
	"So I said goodnight."
)

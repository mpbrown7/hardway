#This variable prints a decimal version of 10 in a string
x = "There are %d types of people." % 10
#This assigns the word binary to the variable named binary
binary = "binary"
#This assigns the word don't to the variable do_not
#three
do_not = "don't"

print "the variable binary is: %r" % binary
print "the variable do_not is: %r" % do_not

#This assigns a statement containing the two previous variables, binary and do_not, that are printed out using the %s or string print formatter
#one
y = "Those who know %s and thos who %s." % (binary, do_not)

#prints x 
print x
#prints y
print y

#prints the variable x formatted with %r which prints it as is, or raw
print "I said: %r." % x
#prints the variable y formatted with %s which is standard string format
print "I also said: '%s'." % y

#Assings a Boolean to hilarious and passes it to the variable joke_evaluation where it is picked up by th %r
hilarious = False
#two
joke_evaluation = "Isn't that joke so funny?! %r"

#the below line is similar to print "Isn't that joke so funny?! %r" % True
print "Isn't that joke so funny?! %r" % True
print joke_evaluation % hilarious

#assigns a string to w and a string to e
#six
w = "This is the left side of ..."
#seven
e = "a string with a right side."

#concatenates the two strings together and prints them
print w + e

print "here is the reverse:"
print e + w

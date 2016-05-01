#Open the sys package and use the argv feature from that package
from sys import argv

#This grabs two variables form the command line after typing python
#The first is the name of the script you are running and the second
#is the name of the file you are going to read the contents of.
script, filename = argv

#filename = raw_input(">")
#Open takes a parameter and returns a value you an set to your own variable.
#This opened a file.
txt = open(filename)

#Prints out a phrase then the filename
print "Here's your file %r:" % filename
#The function "read" is called on txt.
#What we got back from the "open" command above is a file that we can run 
#a command against using the ".", the name of the command, and parameters.
#Just like open and raw_input.  the difference is that when you say 
#txt.read() you are saying, "Hey txt! Do your read command with no
#parameters.

print txt.read()

#Print a line
print "Type the filename again:"
#Take input from the command line using ">" as the prompt
file_again = raw_input(">")

##Executed open again to open a file
txt_again = open(file_again)

#Print out the output from having txt_again execute read against the open 
#file and display its contents
print txt_again.read()


#open(...)
#    open(name[, mode[, buffering]]) -> file object
#
#    Open a file using the file() type, returns a file object.  This is the
#    preferred way to open a file.  See file.__doc__ for further information.

#What way is the other better?
#raw_input: More flexible
#argv: More consistent (tab out the name of the file)
#txt.close()
#txt_again.close()


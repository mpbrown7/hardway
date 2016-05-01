#Use the argv feature from the sys package
from sys import argv

#Two variables are assigned to command line arguments specificed when running the script
#script, filename = argv
filename = raw_input("file?")

#Print out some lines with a warning
print "We're going to read %r." % filename
#print "If you don't want that, hit CTRL-C (^C)."
#print "if you do want that, hit RETURN."

#Receive the reply 
#raw_input("?")

#Open a file with the name passed on the command line and assign it to "target"
print "Opening the file..."
#target = open(filename, 'r+')
target = open(filename)

#Truncate the "target" file
#print "Truncating the file.  Goodbye!"
#target.truncate()

print "Now I'm going to ask you for three lines."

#Assign three lines of input to three variables, line1, line2, and line3
#line1 = raw_input("line 1: ")
#line2 = raw_input("line 2: ")
#line3 = raw_input("line 3: ")

#print "I'm going to write these to the file."

#Write data to the "target" file
#target.write(line1)
#target.write("\n")
#target.write(line2)
##target.write("\n")
#target.write(line3)
#target.write("\n")
#message = "%s\n%s\n%s\n" % (line1, line2, line3)

#target.write(message)
print target.read()

#Close the "target" file which saves the original file named "filename"
print "And finally, we close it."
target.close()

#close -- Closes the file.  Like File->Save.. in your editor
#read -- Reads the contents of the file, you can assign the result to a variable
#readline -- Reads just one line of a text file
#truncate -- Empties the file, watch out if you care about the file.
#write(stuff) -- Writes stuff to a file.

#r+, w+, and a+ for reading and/or writing

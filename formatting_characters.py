
#http://learnpythonthehardway.org/book/ex5.html
name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
weight = 180 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print "Let's talk about %r." % name
print "He's %d inches tall." % height
print "He's %d pounds heavy." % weight
print "Actually that's not too heavy."
print "He's got %s eys and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (age, height, weight, age + height + weight)

#2.54 centimeters in 1 inch
#0.453592 kilograms in 1 pound

print "Let's go metric!"

conversion_centimeter = 2.54
metric_height = height * conversion_centimeter
print "He's %g centimeters tall." % metric_height

conversion_kilos = 0.453592
metric_weight = weight * conversion_kilos
print "He's %d kilos heavy." % metric_weight

#http://docs.python.org/release/2.5.2/lib/typesseq-strings.html
#d	Signed integer decimal.	
#i	Signed integer decimal.	
#o	Unsigned octal.	(1)
#u	Unsigned decimal.	
#x	Unsigned hexadecimal (lowercase).	(2)
#X	Unsigned hexadecimal (uppercase).	(2)
#e	Floating point exponential format (lowercase).	(3)
#E	Floating point exponential format (uppercase).	(3)
#f	Floating point decimal format.	(3)
#F	Floating point decimal format.	(3)
#g	Floating point format. Uses exponential format if exponent is greater than -4 or less than precision, decimal format otherwise.	(4)
#G	Floating point format. Uses exponential format if exponent is greater than -4 or less than precision, decimal format otherwise.	(4)
#c	Single character (accepts integer or single character string).	
#r	String (converts any python object using repr()).	(5)
#s	String (converts any python object using str()).	(6)
#%	No argument is converted, results in a "%" character in the result.

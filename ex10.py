tabby_cat = '''\tI'm tabbed in.'''
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

test = """
\a\a\a was that a bell? \b\n
form feed \t
\v
"""
print test

#while True:
#	for i in ["/","-","|","\\","|"]:
#		print "%s\t" % i,

#%r is for debugging and %s is for displaying

#escape_sequences = '''
#\\ Backslash()
#\' Single-quote (')
#\" Double-quote (")
#\a ASCII bell (BEL)
#\b ASCII backspace (BS)
#\f ASCII formfeed (FF)
#\n ASCII linefeed (LF)
#\N {name} Charactrer named name in the Unicode database (Unicode only)
#\r ASCII Carriage Return (CR)
#\t ASCII Horizontal Tab (TAB)
#\u xxxx Character with 16-bit hex value xxxx (Unicode only)
#\U xxxxxxxx Character with 32-bit hex value xxxxxxxx (Unicode only)
#\v ASCII vertical tab (VT)
#\ooo Character with octal value ooo
#\xhh Character with hex value hh
#'''

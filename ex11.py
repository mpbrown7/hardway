print "How old are you?",
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weigh?",
weight = raw_input()

print "So, you're %r old, %r tall and %r heavy." % (age, height, weight)

print "how many miles is it to there?",
distance = raw_input()
print "how many exits do you pass on the way?",
exits = raw_input()
print "how many beers to drink?",
beers = raw_input()

print "%s miles and %s exits should earn you %s beers!" % (distance, exits, beers)


#input() tries to interpret the input given by the user
#raw_input() just takes the input

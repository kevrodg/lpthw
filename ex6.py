# assigns x the string in the quotes and puts the number 10 where the %d is.
x = "There are %d types of people." % 10
# assigns the string in quotes to binary
binary = "binary"
# makes the variable do_not into don't
do_not = "don't"
# assigns x the string in the quotes. Uses the variables binary and do_not.
y = "Those who know %s and those who %s." % (binary, do_not)

# prints the variable x
print x
# prints the variable y
print y

# prints what is in the quotes and inserts the value of variable x where %r is.
print "I said: %r." % x
# prints what is in the quotes and inserts the value of variable y where %s is.
print "I also said: '%s'." % y

# sets the variable to false
hilarious = False
# assigns the text in the quotes to the variable joke_evaluation
joke_evaluation = "Isn't that joke so funny?! %r"

# prints the text of the variable joke_evaluation and prints the value of hilarious
print joke_evaluation % hilarious

# assigns the text in the quotes to variable w
w = "This is the left side of..."
# assigns the text in the quotes to variable e
e = "a string with a right side."

# prints the strings from variables w and e
print w + e
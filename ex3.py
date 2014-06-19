# This prints the text inside the quotes
print "I will now count my chickens:"

# This prints the word Hens, then calculates 30 divided by 6 and adds 25.
print "Hens", 25 + 30 / 6
# This prints the word Roosters, then subtracts the remainder of 25 times 3 divided by 4 from 100.
# This % is the modulo. Here it is 25 * 3 which is 75. Then we do 75 % 4. $ will go into 75 18 times and leave 3 remaining.
# 100 - those remainder 3 is 97.
print "Roosters", 100 - 25 * 3 % 4

# This prints the text inside the quotes.
print "Now I will count the eggs:"

# This is a funky order of operations one. First we do from left to right the big ticket items.
# I'll break it down:
# 3 + 2 + 1 - 5 + (4 % 2) - (1 / 4) + 6
# 4 % 2 = 0
# 1 / 4 = 0 (Since these are whole numbers, we can't put the fraction, so we get zero instead.)
# 3 + 2 + 1 - 5 + (0) - (0) + 6 = should be 7, yeah?
print 3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6

# This prints the text inside the quotes.
print "Is it true that 3 + 2 < 5 - 7?"

# This is a somewhat tricky order of operations.
# 3 + (2 < 5) - 7
# 3 + (0) - 7
# 3 - 7 = -2
print 3 + 2 < 5 - 7

# This prints the text inside the quotes and then shows what is 3 plus 2
print "What is 3 + 2?", 3 + 2
# Again, prints the text inside the quotes and then shows what is 5 minus 7
print "What is 5 - 7?", 5 - 7

# Prints the text inside the quotes
print "Oh, that's why it's False."

# Prints the text inside the quotes
print "How about some more."

# Prints the text inside the quotes and returns true or false based on if 5 is greater than -2. It is, so this should be true.
print "Is it greater?", 5 > -2
# Prints the text inside the quotes and returns true or false based on if 5 is greater than or equal to -2. It is, so this should be true.
print "Is it greater or equal?", 5 >= -2
# Prints the text inside the quotes and returns true or false based on if 5 is less than or equal to -2. It is not, so this should be false.
print "It it less or equal?", 5 <= -2
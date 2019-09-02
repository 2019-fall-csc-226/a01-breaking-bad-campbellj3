######################################################################
# Author: Jeremy Campbell
# Username: campbellj3
#
# Assignment: A01
#
# Purpose: A program that returns your Chinese Zodiac animal given a
# birth year between 1988 and 1999. Also prints your friend's animal,
# and your compatibility with that friend's animal.
######################################################################
# Acknowledgements:
#   Original Author: Dr. Scott Heggen
######################################################################

# Remember to read the detailed notes about each task in the A01 document.

######################################################################
# (Required) Task 1
# TODO Ask user for their birth year
user_input = input('What is your birth year?')

print('You said that your year was ' + user_input + '!')
print()             #blank line

if user_input == '1988':
    #This print statement will determine which animal that the user will receive based on the Chinese calendar.
    print('You were born in the year of the dragon! Too bad you cant breathe fire.')
    print()

elif user_input == '1989':
    print('You were born in the year of the snake! Do you still smell with your nose?')
    print()

elif user_input == '1990':
    print('You were born in the year of the horse! Hopefully you havent been eating hay though.')
    print()

elif user_input == '1991':
    print('You were born in the year of the goat! Have you tried using your horns to solve your problems?')
    print()

elif user_input == '1992':
    print('You were born in the year of the monkey! Are you excellent at climbing trees?')
    print()

elif user_input == '1993':
    print('You were born in the year of the Rooster! I would not advise screaming early in the morning to wake everyone around you.')
    print()

elif user_input == '1994':
    print('You were born in the year of the dog! Please try not to chase your tail in class.')
    print()

elif user_input == '1995':
    print('You were born in the year of the pig! Where are the cows and chickens?')
    print()

elif user_input == '1996':
    print('You were born in the year of the rat! Try not to scare your other classmates with your quickness.')
    print()

elif user_input == '1997':
    print('You were born in the year of the ox! Could you help me pull my car?')
    print()

elif user_input == '1998':
    print('You were born in the year of the tiger! Be careful, your stripes may start showing.')
    print()

elif user_input == '1999':
    print('You were born in the year of the rabbit! Think quick or the tiger might get you!')
    print()

else:
    print('My apologies, please rerun the program with the year you were born in.')
    print()

# TODO Check the year using if conditionals, and print the correct animal for that year.
# See the a01_pets.py for examples


######################################################################
# (Required) Task 2
# TODO Ask the user for their friend's birth year
friend_input = input('Friend of the original user, what is your birth year?')

print('You said that your year was ' + user_input + '!')
print()             #blank line

if user_input == '1988':
    #This print statement will determine which animal that the user will receive based on the Chinese calendar.
    print('You were born in the year of the dragon! Too bad you cant breathe fire.')
    print()

elif user_input == '1989':
    print('You were born in the year of the snake! Do you still smell with your nose?')
    print()

elif user_input == '1990':
    print('You were born in the year of the horse! Hopefully you havent been eating hay though.')
    print()

elif user_input == '1991':
    print('You were born in the year of the goat! Have you tried using your horns to solve your problems?')
    print()

elif user_input == '1992':
    print('You were born in the year of the monkey! Are you excellent at climbing trees?')
    print()

elif user_input == '1993':
    print('You were born in the year of the Rooster! I would not advise screaming early in the morning to wake everyone around you.')
    print()

elif user_input == '1994':
    print('You were born in the year of the dog! Please try not to chase your tail in class.')
    print()

elif user_input == '1995':
    print('You were born in the year of the pig! Where are the cows and chickens?')
    print()

elif user_input == '1996':
    print('You were born in the year of the rat! Try not to scare your other classmates with your quickness.')
    print()

elif user_input == '1997':
    print('You were born in the year of the ox! Could you help me pull my car?')
    print()

elif user_input == '1998':
    print('You were born in the year of the tiger! Be careful, your stripes may start showing.')
    print()

elif user_input == '1999':
    print('You were born in the year of the rabbit! Think quick or the tiger might get you!')
    print()

else:
    print('My apologies, please rerun the program with the year you were born in.')
    print()

#Sources used for the chinese calendar: https://en.wikipedia.org/wiki/Chinese_zodiac
# TODO Similar to above, check your friend's year using if conditionals, and print the correct animal for that year


######################################################################
# (Optional) Task 3
# TODO Check for compatibility between your birth year and your friend's birth year
# NOTE: You can always assume the first input is your birth year (i.e., 1982 for me).
# This way, you are not writing a ton of code to consider every possibility.
# In other words, only do one row of the sample compatibility table.


# TODO print if you are a strong match, no match, or in between

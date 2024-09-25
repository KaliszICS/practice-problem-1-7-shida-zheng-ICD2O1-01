# Lesson plan
  

'''
	Lesson 1.7 - Booleans
	Author: Mr. Kalisz
	Date Created: September 17, 2021
	Date Last Modified: February 15, 2022
'''


#boolean
#Has one of two values - True/False (Notice the capitalization)

#Booleans will allow us to control our code later on but for now they allow us to tell if a condition is true or false and output such.

#Creating a boolean

condition = True #creates a boolean with the value True

condition = False #changes the variable to a boolean with the value False

#Other ways to create booleans

#comparisons

# >, <, == (equivalence), >=, <=, != (not equivalent)

#bool1 = 5 < 4 #Compares 5 < 4 to make a boolean value of False, then assigns it to bool1
#bool1 = False

#bool1 = 5 < 5
#bool1 = False

#bool1 = 19 < 19
#bool1 = False

#bool1 = 4 == 4.0
#bool1 = True

bool1 = -1 <= 1
#bool1 = True

#print(bool1)

bool2 = 5 != 4
#bool2 = True

bool2 = 40 < 10 * 8

#bool2 = "hello" < 500
#You cannot compare words to numbers

print(bool2)



#Can also compare characters and Strings!

bool2 = "a" < "b" #The earlier in the alphabet, the less the character's value when comparing.
#True since a is earlier in the alphabet than b

bool2 = "a" < "B"
#False

#ALL UPPERCASE LETTERS ARE LESS THAN ALL LOWERCASE LETTERS

#print(bool2)

bool2 = "aab" < "aba" #Also true since "aab" is earlier alphabetically than "aba"
#True

bool2 = "a" < "aba"
print(bool2)

bool2 = "hello" < "hellos"

bool2 = "hello" == "hello"

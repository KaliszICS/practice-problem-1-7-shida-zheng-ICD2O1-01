'''
    Lesson: Booleans
    Author: Mr. Kalisz
    Date Creatd: Sept 25, 2024
    Date Last Modified: Sept 25, 2024
'''

#Booleans - True or False

trueOrFalse = True
print(trueOrFalse)
trueOrFalse = False
print(trueOrFalse)

#Comparators - <, >, ==(equivalence), !=(not equivalent), <=, >=

#Creates a boolean based on the comparison result
bool1 = 5 < 10#True
print(bool1)

#Greater than MUST be greater to be true
bool1 = 10 > 10#False
print(bool1)

#Not equals needs to be different
bool1 = 5 != 5.0 #False

#True when the first value is less than OR equal to the second
bool1 = 4 <= 4 #True

#bool1 = 40 < "word" #Runtime error since its based on a value
#can't compare ints to Strings

#Data Types

bool1 = "word" < "hello" 
print(bool1)
#Compared Alphabetically - KIND OF

bool1 = "fire" < "firetruck"
print(bool1)
#Shorter words than contain all the same letters in the same order come first and are less than

bool1 = "Zoo" < "alphabet" #
print(bool1)
#when casing is not all the same, there a second rule (ASCII)
#Characters are ACTUALLY compared, using their ASCII value
#https://www.asciitable.com/

#Convert to boolean - bool()

# int -> boolean
#False when the integer is 0, True otherwise

print(bool(5))
print(bool(0))
print(bool(-9))

# float -> boolean
#folllows the same logic as integer

print(bool(5.0))
print(bool(0.0))
print(bool(-9.0))

# str -> boolean
#True when anything is in the String
#False when it is an empty String

print(bool("Hello")) # True
print(bool("True")) # True
print(bool("False")) # True
print(bool("")) #False
print(bool(" ")) #True

#DO NOT DO THIS - DO NOT COMPARE BOOLEANS

bool1 = True
print(bool1 == True)
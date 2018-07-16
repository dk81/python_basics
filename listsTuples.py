# -*- coding: utf-8 -*-
"""
Created on Fri Apr 27 08:51:58 2018

@author: dk
"""

# Lists In Python

'''
A list is an object which holds different data items. Since lists are mutable, 
the contents in a list can be changed.

Items in a list are called elements.

'''

# Examples Of Lists

square_numbers = [1, 4, 9, 16, 25, 36, 49, 64]

vowels = ["a", "e", "i", "o", "u"]

diff_types = [1, "apples", 27, True]

# Repitition Operator
# can do a list * n

print(vowels * 3)

print(diff_types * 2)

# Length Of A List With len():
    
'''
The len() function is for determining the number of elements in a list.
'''

square_numbers = [1, 4, 9, 16, 25, 36, 49, 64]
print(len(square_numbers))
    
# Indexing In A List

'''
Elements in a list can be accessed by its index. A list's index starts from 0 
which is associated with the first item of the list (from the left).
'''

vowels = ["a", "e", "i", "o", "u"]

print(vowels[0])
print(vowels[len(vowels) - 1])


# Changing Elements In A List (Mutability)

diff_types = [1, "apples", 27, True]

diff_types[0] = 5
diff_types[3] = False

print(diff_types)

# Concatenating Lists

a = [1, 2, 3]
b = [2, 4, 6]

print(a + b)


# A For Loop With A List

vowels = ["a", "e", "i", "o", "u"]

for i in vowels:
    print("Vowel: ", i)
    
    
# List Slicing
# Taking a selection from a list.

square_numbers = [1, 4, 9, 16, 25, 36, 49, 64]

# Print at indices 1, 2, 3 and 4 not including 5
print(square_numbers[1:5])

# The in keyword

square_numbers = [1, 4, 9, 16, 25, 36, 49, 64]

guess = int(input("Name a square number less than 65. "))

if guess in square_numbers:
    print("Yes. Your guess of", guess, "is a square number.")
else:
    print("Your guess of", guess, "is not a square number.")
    
# The append keyword

square_numbers = [1, 4, 9, 16, 25, 36, 49, 64]

new_squares = [81, 100, 121, 144]

for index in new_squares:
    square_numbers.append(index)

print(square_numbers)
    
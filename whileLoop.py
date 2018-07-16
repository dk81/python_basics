# -*- coding: utf-8 -*-
"""
Created on Wed Apr 25 12:41:43 2018

@author: dk
"""

# while Loops in Python

'''
A while loop is a loop which repeats code statements while meeting a condition.
'''

# While loop statement:

'''
while condition:
    <put code here>
    <put code here>
    <put code here>
    ...
    
'''

# Example One (Printing Numbers From 1 to 8):
    
i = 1 #Initialize

while i <= 8:
    print(i)
    i = i + 1
    
# Example Two (Adding Numbers From 1 to 100):
   
#Initialize

i = 1 
total = 0

while i <= 100:
    total += i
    i += 1
    
print(total)

# Example Three - A Function For Adding Numbers From 1 to n.

def total_n(n):
    counter = 1
    total = 0
    if n >= 1 and type(n) == int:
        while counter <= n:
            total += counter        
            counter += 1
        return total
    else:
        print("Please enter a whole number that is 1 or greater.")
    
sumTotal = total_n(10)
print(sumTotal)
    
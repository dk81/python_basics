# -*- coding: utf-8 -*-
"""
Created on Sat Apr 28 21:39:15 2018

@author: dk
"""

# Tuples



## Examples Of Tuples

# Example One

even_numbers = (2, 4, 6, 8, 10, 12, 14, 16, 18, 20)

print(even_numbers)

# Example Two

students = ("Marie", "Marcus", "Harry", "Janey", "Linus")

for name in students:
    print(name)

for j in range(len(students)):
    print(students[j])

# Example Three - A Tuple With One Element

singleton = (100, )

print(singleton)
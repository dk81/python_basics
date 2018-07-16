# -*- coding: utf-8 -*-
"""
Created on Tue May  1 09:48:32 2018

@author: dk
"""

# Dictionaries In Python

places = {'Canada': 'Ottawa', 'Australia': 'Sydney', 'USA': 'Washington', 'Belgium': 'Brussels'}


## Format: dictionary[key]:
    
print(places['Canada'])

print(places['Belgium'])


## in and not in Keywords:
    
if 'Australia' in places:
    print('The capital of Australia is Sydney.')
    
if 'France' not in places:
    print('Error.')

## Adding to a dictionary:
    
places['Germany'] = 'Berlin'

print(places)

## Deleting From A Dictionary:
    
del places['Belgium']

print(places)

## for Loop In Dictionary:
    
for key in places:
    print(key, "-", places[key])



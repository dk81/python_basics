
### If - Else Statements

# Relational Operators In Conditions

a = 10
b = 8

# a greater than b?

print(a > b)

# a less than b?

print(a < b)

# a greater than or equal to b?

print(a >= b)

# a less than or equal to b?

print(a <= b)

# Is a equal to b?

print(a == b)

# Is a not equal to b?

print(a != b)

## If Statement

'''
if condition:
    < put code here >
    < put code here >
'''

# Example:
    
answer = int(input("What is my favourite number? "))

if answer == 8:
    print("You got my favourite number right!")



## If-Else Statements:

'''
if condition:
    < put code here >
    < put code here >
else:
    < put code here >
    < put code here >
    
'''

# Example:
    
answer = int(input("What is 5 times 10? "))

if answer == 50:
    print("You are correct!")
else:
    print("That answer is incorrect. The correct answer is 50.")




# -----------------------------------
#### If-Elif-Else Statements

## If-Else Statements:

'''
if condition1:
    < put code here >
    < put code here >
elif condition2:
    < put code here >
    < put code here >
elif condition3:
    < put code here >
    < put code here >
    
    ...
    
    
else:
    < put code here >
    < put code here >
    
'''

# Example:
    
guess = int(input("Guess the price of the new car. "))

if guess == 24000:
    print("You are correct!")
elif guess < 24000:
    print("Your guess is less than the actual price of the car.")
else:
    print("Your guess is more than the actual price of the car.")




    
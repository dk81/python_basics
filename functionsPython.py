## Functions In Python

''' A function is a group of statements designed to complete a task.
Functions may take inputs and return outputs.'''

# Defining A Function In Python

'''
def function_name():
    < code here >
    < code here >
    < code here >
    ...

'''

# Example Of A Function:
    
def say_hello():
    print("Hello there.")
    
    
# Function Calls:
    
say_hello()

# Multiple Functions

def say_goodbye():
    print("Goodbye.")
    
def hello_goodbye():
    say_hello()
    say_goodbye()
    
hello_goodbye()
    
# -----------------------------------

# Functions With Inputs / Arguments:
    
'''
def function_name(arg1, arg2, ... , argn):
    < code here >
    < code here >
    < code here >

'''


# Examples Of Functions With Inputs / Arguments:
    
    
# Example One

def multiply_twoNumbers(a, b):
    product = a * b
    print("The product of", a, "and", b, "is", product)
    
multiply_twoNumbers(5, 8)

# Example Two

def square_number(a):
    square = a ** 2
    print("Square Of", a, ":", square)
    
square_number(10)

# Example Three

def add_twoNumbers(a, b):
    return a + b

total = add_twoNumbers(1, 10)
print(total)
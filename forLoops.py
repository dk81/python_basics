### For Loops In Python

'''
A for loop is a count-controlled loop which repeats through code a certain
amount of times.
'''


## Structure Of For Loop

'''
for counter_variable in [value_1, value_2, ..., value_n]:
    < run code here >
    < run code here >
    ...
    
'''

## range():
    
# A useful piece in a for loop is the range() function.
# As an example range(3) is the same as the list [0, 1, 2]
    
    
## Examples

# Example One: Happy Birthday Five Times

def happy_bday_five():
    name = input("Today is your birthday. What is your name?")
    for i in range(5):
        print("Happy Birthday", name)
        
happy_bday_five()



# Example Two: Printing Odd Numbers From 1 to 20

def odd_one_twenty():
    print("The odd numbers from 1 to 20 will be printed.")
    for i in range(1, 20, 2):
        print(i)
        
odd_one_twenty()


# Example Three - Countdown

def number_countdown(n):
    for i in range(n, -1, -1):
        print(i)
        
number_countdown(20)
    
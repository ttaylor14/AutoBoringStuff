# Introduction to Python

# Chapter 2  Flow Control
# automatetheboringstuff.com/chapter2/

# Boolean Values

spam = True
spam

# True # true is not defined

# true = 2 + 2 # You can not assign to keyword


# Comparison Operators

'''
Operator

==
!=
<
>
<=
>=


Meaning

Equal to
Not equal to
Less than
Greater than
Less than or equal to
Greater than or equal to

These operators evaluate to True or False depending on the values you give them.
Lets try some operators now, starting with == and !=.

'''

42 == 42
42 == 99

# True
# False

2 != 3
# True

2 != 2
# False

'hello' == 'hello'
'hello' == 'Hello'
# True
# False

'dog' != 'cat'
# True

True == True
# True

True != False
# True

42 == 42.0
# True

42 == '42'
# False


42 < 100
42 > 100
# True
# False

42 < 42
# False

eggCount = 42
eggCount <= 42
# True

myAge = 29
myAge >= 10
# True

# Boolean Operators

# three Boolean operators (and, or, and not) are used to compare Boolean values.


True and True
True and False
# True
# False


True or False
False or False
# True
# False

not True
not not not not not True
# Flase
# True

(4 < 5) and (5 < 6)
(4 < 5) and (9 < 6)
# True
# False

(1 == 2) or (2 == 2)
# True

2 + 2 == 4 and not 2 + 2 == 5 and 2 * 2 == 2 + 2
# True


# order of operations. Star on left go to right...


# Elements of Flow Control

# Conditions
# The Boolean expressions you have seen so far could all be considered conditions,
# which are the same thing as expressions; condition is just a more specific name in
# the context of flow control statements. Conditions always evaluate down to a Boolean
# value, True or False.

name = 'Mary'
password = 'swordfish'
if name == 'Mary':
    print('Hello Mary')
    if password == 'swordfish':
        print('Access granted.')
    else:
        print('Wrong password.')


# If Statments
# If this condition is true, execute the code in the clause.

# The if keyword
# A condition (that is, an expression that evaluates to True or False)
# A colon
# Starting on the next line, an indented block of code (called the if clause)

if name == 'Alice':
    print('Hi, Alice.')

# Else Statment
# If this condition is true, execute this code. Or else, execute that code.

# The else keyword
# A colon
# Starting on the next line, an indented block of code (called the else clause)


name = 'Bob'
if name == 'Alice':
    print('Hi, Alice.')
else:
    print('Hello, stranger.')


# elif Statement
# elif statement is an else if statement that always
# follows an if or another elif statement. For when you may have a case where you want one
# of many possible clauses to execute.

# The elif keyword
# A condition (that is, an expression that evaluates to True or False)
# A colon
# Starting on the next line, an indented block of code (called the elif clause)

name = 'Bob'
age = 5
if name == 'Alice':
    print('Hi, Alice.')
elif age < 12:
    print('You are not Alice, kiddo.')


name = 'Dracula'
age = 4000
if name == 'Alice':
    print('Hi, Alice.')
elif age < 12:
    print('You are not Alice, kiddo.')
elif age > 2000:
    print('Unlike you, Alice is not an undead, immortal vampire.')
elif age > 100:
    print('You are not Alice, grannie.')


# The order of the elif statements does matter
# Remember that the rest of the elif clauses are automatically skipped once a True condition has been found


name = 'Dracula'
age = 4000
if name == 'Alice':
    print('Hi, Alice.')
elif age < 12:
    print('You are not Alice, kiddo.')
elif age > 100:
    print('You are not Alice, grannie.')
elif age > 2000:
    print('Unlike you, Alice is not an undead, immortal vampire.')


# Optionally, you can have an else statement after the last elif statement. In that case,
# it is guaranteed that at least one (and only one) of the clauses will be executed.

name = 'Bob'
age = 30
if name == 'Alice':
    print('Hi, Alice.')
elif age < 12:
    print('You are not Alice, kiddo.')
else:
    print('You are neither Alice nor a little kid.')


# Loop Statement
# You can make a block of code execute over and over again with a while statement.
# The code in a while clause will be executed as long as the while statements condition
# is True.

# The while keyword
# A condition (that is, an expression that evaluates to True or False)
# A colon
# Starting on the next line, an indented block of code (called the while clause)


# But at the end of a while clause, the program execution jumps back to the start of the while
# statement. The while clause is often called the while loop or just the loop.

spam = 0
if spam < 5:
    print('Hello, world.')
    spam = spam + 1

# Output Hello, world.


spam = 0
while spam < 5:
    print('Hello, world.')
    spam = spam + 1

# Output Hello, world.
# Hello, world.
# Hello, world.
# Hello, world.
# Hello, world.

name = ''                           # (1)
while name != 'your name':          # (2)
    print('Please type your name.')
    name = input()                  # (3)
print('Thank you!')                 # (4)

# Example Output:
'''
Please type your name.
Al
Please type your name.
Albert
Please type your name.
%#@#%*(^&!!!
Please type your name.
your name
Thank you!
'''


# Break Statement
# There is a shortcut to getting the program execution to break out of a
# while loops clause early. If the execution reaches a break statement, it immediately
# exits the while loops clause. In code, a break statement simply contains the break keyword.


while True:                         # (1)
    print('Please type your name.')
    name = input()                  # (2)
    if name == 'your name':         # (3)
        break                       # (4)
print('Thank you!')                 # (5)


# Continue Statement
# When the program execution reaches a continue statement, the program execution immediately
# jumps back to the start of the loop


# Trapped in an Infinite Loop?

# If you ever run a program that has a bug causing it to get stuck in an
# infinite loop, press CTRL-C. This will send a KeyboardInterrupt error to your program
# and cause it to stop immediately. To try it, create a simple infinite loop in the file
# editor, and save it as infiniteloop.py.


while True:
    print('Hello world!')

# When you run this program, it will print Hello world! to the screen forever, because
# the while statements condition is always True. In IDLEs interactive shell window,
# there are only two ways to stop this program: press CTRL-C or select Shell - restart
# Shell from the menu. CTRL-C is handy if you ever want to terminate your program
# immediately, even if its not stuck in an infinite loop.


while True:
    print('Who are you?')
    name = input()
    if name != 'Joe':  # (1)
        continue  # (2)
        print('Hello, Joe. What is the password? (It is a fish.)')
        password = input()  # (3)
    if password == 'swordfish':
        break  # (4)
print('Access granted.')  # (5)


# Truthy and Falsey Values

# There are some values in other data types that conditions will consider equivalent to
# True and False. When used in conditions, 0, 0.0, and (the empty string) are considered
# False, while all other values are considered True.


name = ''
while not name:  # (1)
    print('Enter your name:')
    name = input()
print('How many guests will you have?')
numOfGuests = int(input())
if numOfGuests:  # (2)
    print('Be sure to have enough room for all your guests.')  # (3)
print('Done')

# Example Output:
'''
name = ''
while not name: #(1)
    print('Enter your name:')
    name = input()
print('How many guests will you have?')
numOfGuests = int(input())
if numOfGuests: #(2)
    print('Be sure to have enough room for all your guests.') #(3)
print('Done')
'''


# for Loops and the range() Function

# what if you want to execute a block of code only a certain number of times? You can do
# this with a for loop statement and the range() function.


# In code, a for statement looks something like for i in range(5): and always includes the
# following:

# The for keyword
# A variable name
# The in keyword
# A call to the range() method with up to three integers passed to it
# A colon
# Starting on the next line, an indented block of code (called the for clause)


print('My name is')
for i in range(5):
    print('Jimmy Five Times (' + str(i) + ')')


# Output:

'''
My name is
Jimmy Five Times (0)
Jimmy Five Times (1)
Jimmy Five Times (2)
Jimmy Five Times (3)
Jimmy Five Times (4)
'''

# An Equivalent while Loop

# You can actually use a while loop to do the same thing as
# for loop; for loops are just more concise.

print('My name is')
i = 0
while i < 5:
    print('Jimmy Five Times (' + str(i) + ')')
    i = i + 1


# The Starting, Stopping, and Stepping Arguments to range()

# Some functions can be called with multiple arguments separated by a comma, and
# range() is one of them. This lets you change the integer passed to range() to
# follow any sequence of integers, including starting at a number other than zero.


for i in range(12, 16):
    print(i)

# The range() function can also be called with three arguments. The first two
# arguments will be the start and stop values, and the third will be the step argument.
# The step is the amount that the variable is increased by after each iteration.

for i in range(0, 10, 2):
    print(i)

#  you can even use a negative number for the step argument to make the for loop count down instead of up.

for i in range(5, -1, -1):
    print(i)


# Importing Modules

# Each module is a Python program that contains a related group of functions that can be embedded in your programs.


# The import keyword
# The name of the module
# Optionally, more module names, as long as they are separated by commas

import random
for i in range(5):
    print(random.randint(1, 10))

# The random.randint() function call evaluates to a random integer value between the two integers that you pass it.


# Ending a Program Early with sys.exit()

# The last flow control concept to cover is how to terminate the program. This always happens if the program execution
# reaches the bottom of the instructions. However, you can cause the program to terminate, or exit, by calling the sys.exit() function.

import sys

while True:
    print('Type exit to exit.')
    response = input()
    if response == 'exit':
        sys.exit()
    print('You typed ' + response + '.')

# This program has an infinite loop with no break statement inside. The only way this program will end is if the user enters exit, causing sys.exit() to be called.

# Practice Questions

# Q: 1. What are the two values of the Boolean data type? How do you write them?

# Q: 2. What are the three Boolean operators?

# Q: 3. Write out the truth tables of each Boolean operator (that is, every possible combination of Boolean values for the operator and what they evaluate to).

# Q: 4. What do the following expressions evaluate to?


(5 > 4) and (3 == 5)
not (5 > 4)
(5 > 4) or (3 == 5)
not ((5 > 4) or (3 == 5))
(True and True) and (True == False)
(not False) or (not True)

# Q: 5. What are the six comparison operators?

# Q: 6. What is the difference between the equal to operator and the assignment operator?

# Q: 7. Explain what a condition is and where you would use one.

# Q: 8. Identify the three blocks in this code:


spam = 0
if spam == 10:
    print('eggs')
    if spam > 5:
        print('bacon')
    else:
        print('ham')
    print('spam')
print('spam')


# Q: 9. Write code that prints Hello if 1 is stored in spam, prints Howdy if 2 is stored in spam, and prints
# Greetings! if anything else is stored in spam.

# Q: 10. What can you press if your program is stuck in an infinite loop?

# Q: 11. What is the difference between break and continue?

# Q: 12. What is the difference between range(10), range(0, 10), and range(0, 10, 1) in a for loop?

# Q: 13. Write a short program that prints the numbers 1 to 10 using a for loop. Then write an equivalent program
# that prints the numbers 1 to 10 using a while loop.

# Q: 14. If you had a function named bacon() inside a module named spam, how would you call it after importing spam?

# Extra credit: Look up the round() and abs() functions on the Internet, and find out what they do. Experiment with
# them in the interactive shell.

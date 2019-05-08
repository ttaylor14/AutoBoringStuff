# Introduction to Python

# Chapter 2  Flow Control
# automatetheboringstuff.com/chapter2/

### Boolean Values

spam = True
spam

# True # true is not defined

# true = 2 + 2 # You can not assign to keyword



### Comparison Operators

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
Let’s try some operators now, starting with == and !=.

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

### Boolean Operators

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


### Elements of Flow Control

# Conditions
# The Boolean expressions you’ve seen so far could all be considered conditions, 
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
# “If this condition is true, execute the code in the clause.”

# The if keyword
# A condition (that is, an expression that evaluates to True or False)
# A colon
# Starting on the next line, an indented block of code (called the if clause)

if name == 'Alice':
    print('Hi, Alice.')

# Else Statment
# “If this condition is true, execute this code. Or else, execute that code.”

# The else keyword
# A colon
# Starting on the next line, an indented block of code (called the else clause)


name = 'Bob'
if name == 'Alice':
    print('Hi, Alice.')
else:
    print('Hello, stranger.')


# elif Statement
# elif statement is an “else if” statement that always 
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
# The code in a while clause will be executed as long as the while statement’s condition 
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
# while loop’s clause early. If the execution reaches a break statement, it immediately 
# exits the while loop’s clause. In code, a break statement simply contains the break keyword.


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
# the while statement’s condition is always True. In IDLE’s interactive shell window, 
# there are only two ways to stop this program: press CTRL-C or select Shell ▸ restart 
# Shell from the menu. CTRL-C is handy if you ever want to terminate your program 
# immediately, even if it’s not stuck in an infinite loop.



while True:
      print('Who are you?')
  name = input()
  if name != 'Joe':       #(1)
    continue              #(2)
  print('Hello, Joe. What is the password? (It is a fish.)') 
  password = input()      #(3)
  if password == 'swordfish':
    break                 #(4)
print('Access granted.')  #(5)



# “Truthy” and “Falsey” Values

# There are some values in other data types that conditions will consider equivalent to 
# True and False. When used in conditions, 0, 0.0, and '' (the empty string) are considered
# False, while all other values are considered True. 


name = ''
while not name: #(1)
    print('Enter your name:')
    name = input()
print('How many guests will you have?')
numOfGuests = int(input())
if numOfGuests: #(2)
    print('Be sure to have enough room for all your guests.') #(3)
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



### for Loops and the range() Function
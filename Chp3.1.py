# Introduction to Python

# Chapter 3  Functions
# automatetheboringstuff.com/chapter3/

# Functions


def hello():
    print('Howdy!')
    print('Howdy!!!')
    print('Hello there.')


hello()

# Output:
'''
Howdy!
Howdy!!!
Hello there.
'''

# A major purpose of functions is to group code that gets executed multiple times.


def hello(name):
    print('Hello ' + name)


hello('Alice')
hello('Bob')

# Output:
# Hello Alice
# Hello Bob

# Return Values and return Statements

# The return keyword
# The value or expression that the function should return

import random


def getAnswer(answerNumber):
    if answerNumber == 1:
        return 'It is certain'
    elif answerNumber == 2:
        return 'It is decidedly so'
    elif answerNumber == 3:
        return 'Yes'
    elif answerNumber == 4:
        return 'Reply hazy try again'
    elif answerNumber == 5:
        return 'Ask again later'
    elif answerNumber == 6:
        return 'Concentrate and ask again'
    elif answerNumber == 7:
        return 'My reply is no'
    elif answerNumber == 8:
        return 'Outlook not so good'
    elif answerNumber == 9:
        return 'Very doubtful'


r = random.randint(1, 9)
fortune = getAnswer(r)
print(fortune)

# The None Value

# In Python there is a value called None, which represents the absence of a .
# None is the only value of the NoneType data type.
# (Other programming languages might call this value null, nil, or undefined.)
# Just like the Boolean True and False values, None must be typed with a capital N.

# This value-without-a-value can be helpful when you need to store something that won’t
# be confused for a real value in a variable.

# all function calls need to evaluate to a return value, print() returns None

spam = print('Hello!')
# Hello!

None == spam
# True

# Python adds return None to the end of any function definition with no return statement.

# The two strings appear on separate lines because the print() function automatically adds
# a newline character to the end of the string it is passed. However, you can set the end
# keyword argument to change this to a different string.

print('Hello', end='')
print('World')

# Output: HelloWorld

print('cats', 'dogs', 'mice')
# Output: cats dogs mice

# could replace the default separating string by passing the sep keyword argument

print('cats', 'dogs', 'mice', sep=',')
# Output: cats,dogs,mice


# Local and Global Scope

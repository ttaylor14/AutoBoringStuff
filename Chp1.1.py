# Introduction to Python

# Chapter 1  Python Basics
# automatetheboringstuff.com/chapter1/


# Entering Expressions into the Interactive Shell


2 + 2
# output should be 4

2

# out put will be 2

2 ** 3      # 8 - exponent
22 % 8      # 6 - modulus/remainder
22 // 8     # 2 - Integer Division/Floored quotient
22 / 8      # 2.75 - Division
3 * 5       # 15 - Multiplication
5 - 2       # 3 - subtraction
2 + 2       # 4 - Addition


# Python follows Order of Operations (precedence)


2 + 3 * 6
# 20
(2 + 3) * 6
# 30
48565878 * 578453
# 28093077826734
2 ** 8
# 256
23 / 7
# 3.2857142857142856
23 // 7
# 3
23 % 7
# 2
2 + 2
# 4
(5 - 1) * ((7 + 1) / (3 - 1))
# 16.0

# 5 +
# # this will result in an error because 5 has not been added to anything

# 42 + 5 + * 2
# # This will result in an error because two operations are given in a row


# The Integer, Floating-Point, and String Data Types

# 'Hello world!
# Error: SyntaxError: EOL while scanning string literal
# Forgot a ' or "


# String Concatenation and Replication


'Alice' + 'Bob'
# this will result in 'AliceBob'

# 'Alice' + 42
# This will result in an error because you can not add unlike data types


'Alice' * 5
# result: 'AliceAliceAliceAliceAlice'
# String Replicator

# 'Alice' * 'Bob'
# 'Alice' * 5.0
# These expressions make no sense to python


# Storing Values in Variables

spam = 40
spam

# Output = 40

eggs = 2
spam + eggs

# Output = 42

spam + eggs + spam

# output = 82

spam = spam + 2
spam

# Output = 42


spam = 'Hello'
spam
# 'Hello'

spam = 'Goodbye'
spam
# 'Goodbye'


'''
Table 1-3 has examples of legal variable names. You can name a variable anything as
long as it obeys the following three rules:

It can be only one word.
It can use only letters, numbers, and the underscore (_) character.
It can not begin with a number.

Table 1-3. Valid and Invalid Variable Names

Valid variable names
balance
currentBalance
current_balance
_spam
SPAM
account4

Invalid variable names

current-balance (hyphens are not allowed)
current balance (spaces are not allowed)
4account (ca not begin with a number)
42 (can not begin with a number)
total_$um (special characters like $ are not allowed)
hello (special characters like single quotes are not allowed)


Variable names are case-sensitive, meaning that spam, SPAM, Spam, and sPaM are four
different variables. It is a Python convention to start your variables with a lowercase
letter.

This book uses camelcase for variable names instead of underscores; that is, variables
lookLikeThis instead of looking_like_this. Some experienced programmers may point out that
the official Python code style, PEP 8, says that underscores should be used. I
unapologetically prefer camelcase and point to -A Foolish Consistency Is the Hobgoblin of
Little Minds- in PEP 8 itself:

-Consistency with the style guide is important. But most importantly: know when to be
inconsistent - sometimes the style guide just does not apply. When in doubt, use your best
judgment. -

'''


# Your First Program

# This program says hello and asks for my name.

print('Hello world!')
print('What is your name?')    # ask for their name
myName = input()
print('It is good to meet you, ' + myName)
print('The length of your name is:')
print(len(myName))
print('What is your age?')    # ask for their age
myAge = input()
print('You will be ' + str(int(myAge) + 1) + ' in a year.')

"""""
Output:
Hello world!
What is your name?
Al
It is good to meet you, Al
The length of your name is:
2
What is your age?
4
You will be 5 in a year.
"""

# Len() function

len('hello')
# 5

len('My very energetic monster just scarfed nachos.')
# 46

len('')
# 0

# The str(), int(), and float() Functions

str(29)
# '29'

print('I am ' + str(29) + ' years old.')
# I am 29 years old.

str(0)
# '0'

str(-3.14)
# '-3.14'

int('42')
# 42

int('-99')
# -99

int(1.25)
# 1

int(1.99)
# 1

float('3.14')
# 3.14

float(10)
# 10.0


spam = input()
# enter: 101

spam
# '101'

spam = int(spam)
spam
# 101

spam * 10 / 5
# 202.0

# int('99.99')
# int('twelve')

# Both will be an error

int(7.7)
# 7

int(7.7) + 1
# 8

print('What is your age?')  # ask for their age
myAge = input()
print('You will be ' + str(int(myAge) + 1) + ' in a year.')


42 == '42'
# False

42 == 42.0
# True

42.0 == 0042.000
# True


# Practice Questions


# Q:1. Which of the following are operators, and which are values?

# Operators: * - / +
# Values: 'hello' 88.8 5


# Q: 2. Which of the following is a variable, and which is a string?

# Variable: spam
# String: 'spam'

# Q: 3. Name three data types.

# Integer, String, Float

# Q: 4. What is an expression made up of? What do all expressions do?

# Expressions consist of values (such as 2) and operators (such as +), and
# they can always evaluate (that is, reduce) down to a single value.


# Q: 5. This chapter introduced assignment statements, like spam = 10.
# # What is the difference between an expression and a statement?

# You all store values in variables with an assignment statement.
# An assignment statement consists of a variable name, an equal sign
# (called the assignment operator), and the value to be stored.

# A statement value is stored in a variable. while an expression is done to an object.


# Q: 6. What does the variable bacon contain after the following code runs?

bacon = 20
bacon + 1

# bacon = 21

# Q: 7. What should the following two expressions evaluate to?

'spam' + 'spamspam'
# 'spamspamspam'

'spam' * 3
# 'spamspamspam'

# Q: 8. Why is eggs a valid variable name while 100 is invalid?

# 100 begins with a number, eggs does not

# Q: 9. What three functions can be used to get the integer,
# floating-point number, or string version of a value?

# str() int() float()


# Q: 10. Why does this expression cause an error? How can you fix it?

# you can not add an integer to a string before converting it to a string

# Extra Credit: round() function


# round(number[, ndigits])
"""
round() Parameters
The round() method takes two parameters:

number - number that is to be rounded
ndigits (Optional) - number upto which the given number is to be rounded

The round() method returns:

(If ndigits not provided) nearest integer to the given number
If two multiples are really close, rounding is done toward the even choice
(If ndigits given) floating point number rounded off to the ndigits digits
Always rounded to the closest multiple of 10 to the power minus ndigits
"""

round(7.7)
round(7.2)
round(4.334, 0)
round(4.55, 0)
round(4.6, 0)
round(4.5, 0)

round(4.556235, 3)

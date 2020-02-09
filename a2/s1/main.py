# Program Author:  Kaleb Newsom
#         Course:  CS 351 Programming Languages
#     Assignment:  Logic Programming Lab 2

# import logic methods from kanren
from kanren import run, var, membero
import random                           # import package that creates random numbers

x = list(range(1,70))                   # set x to a list of numbers from 1 to 69 inclusive
y = list(range(1,27))                   # set y to a list of numbers from 1 to 26 inclusive
random.shuffle(x)                       # randomly shuffle the list of numbers from 1 to 69 inclusive
random.shuffle(y)                       # randomly shuffle the list of numbers from 1 to 26

z = var()                               # let z be a logic variable
# let user know that the following statement will be the first 5 powerball numbers
print('These are your first 5 randomly chosen numbers to select on your powerball ticket!')
# display a tupple containing the first 5 numbers of the randomized list of numbers including numbers 1 to 69 inclusive
print(sorted(run(5, z, membero(z, x), membero(z, x), membero(z, x), membero(z, x), membero(z, x))))
# let user know that the following statement will be the 6th powerball number
print('This is your randomly chosen 6th powerball number to select on your powerball ticket!')
# display a tupple containing the 6th powerball number
print(sorted(run(1, z, membero(z, (y)))))
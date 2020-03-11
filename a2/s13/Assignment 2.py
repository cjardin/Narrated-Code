# Michael Martindill
# CS 351
# 2/7/2019
# The purpose of this program is to find the union of two sets by using logic programming with the kanren package

from kanren import run, eq, membero, var, conde

# Function to convert the inputted string into an array
def stringToArray(str):
    setArray = str.split(',')
    return setArray


print("Input two sets of numbers to find the union between them. (Separated by commas)")

set1 = input("Set 1: ")
set1 = set1.replace(" ", "")
set1Array = stringToArray(set1)

set2 = input("Set 2: ")
set2 = set2.replace(" ", "")
set2Array = stringToArray(set2)

x = var()
print("The union of these two sets is: ")
print(run(len(set1Array), x, membero(x, set1Array), membero(x, set2Array)))

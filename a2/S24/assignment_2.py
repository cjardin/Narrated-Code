'''
Name: Leouel Guanzon
Professor: Cary Jardin
Course: CS351 Programming Languages
Description: Logical Programming (Simple Family Tree) 
'''

from kanren import run, var, Relation, facts

parent = Relation()
member = var()

dad = input("Enter your father's name: ")
child1 = input("Enter your brother's/sister's name: ")
child2 = input("Enter your name: ")

facts(parent, (dad, child1),
              (dad, child2))

print("The father of ", child1, " is ")
print(run(1, member, parent(member, child1)))
print("The children of ", dad, " is ")
print(run(2, member, parent(dad, member)))

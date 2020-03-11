"""
Name: Kangnan Dong
Date: 3/8/2020
Assignment2 Goal: use kanren package to build a family tree
"""

import json
from kanren import Relation, facts, run, conde, var, eq

with open('relationships.json') as f:
    d = json.loads(f.read())
father = Relation()
mother = Relation()

for item in d['father']:
    facts(mother, (list(item.keys())[0], list(item.values())[0]))
for item in d['mother']:
    facts(father, (list(item.keys())[0], list(item.values())[0]))

def parent(x, y):
    return conde((father(x, y),), (mother(x,y),))
def grandparent(x, y):
    temp = var()
    return conde((parent(x, temp), parent(temp, y)))
def sibling(x, y):
    temp = var()
    return conde((parent(temp, x), parent(temp, y)))
def uncle(x, y):
    temp = var()
    return conde((father(temp, x), grandparent(temp, y)))

x = var()
output = run(0, x, (father, 'John', x))
for item in output:
    print(item)

output = run(0, x, (mother, x, 'William'))
for item in output:
    print(item)

output = run(0, x, parent(x, 'Adam'))
for item in output:
    print(item)

output = run(0, x, grandparent(x, 'Wayne'))
for item in output:
    print(item)

output = run(0, x, grandparent('Megan', x))
for item in output:
    print(item)

name = 'David'
output = run(0, x, sibling(x, name))

siblings = [x for x in output if x != name]
for item in siblings:
    print(item)

name = 'Tiffany'
name_father = run(0, x, father(x, name))[0]
output = run(0, x, uncle(x, name))
output = [x for x in output if x != name_father]
for item in output:
    print(item)
a, b, c = var(), var(), var()
output = run(0, (a,b), father(a, c), mother(b, c))
for item in output:
    print('Husband:', item[0], '<==> Wife:', item[1])
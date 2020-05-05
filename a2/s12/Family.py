# Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)] on win32
# Type "help", "copyright", "credits" or "license" for more information.
# Family relationships from The Godfather
# Translated from the core.logic example found in
# "The Magical Island of Kanren - core.logic Intro Part 1"
# http://objectcommando.com/blog/2011/11/04/the-magical-island-of-kanren-core-logic-intro-part-1/
from kanren import Relation, facts, run, conde, var, eq
from treelib import Node, Tree
import re

father = Relation()
mother = Relation()

facts(father, ('John', 'Jesse'),
      ('John', 'Calli'),
      ('Jim', 'Mindy'),
      ('Jim', 'Jimmy'),
      ('Hector', 'Michael'),
      ('Hector', 'Rachael'),
      ('Hector', 'Daniel'),
      ('Bruce', 'John'),
      ('Bruce', 'Terry'),
      ('Bruce', 'Lynda'),
      ('Bruce', 'Lorie'),
      ('Bruce', 'Barbara'),
      ('Bruce', 'Leslie'))

facts(mother, ('Mindy', 'Jesse'),
      ('Mindy', 'Calli'),
      ('Margie', 'Mindy'),
      ('Margie', 'Jimmy'),
      ('Leslie', 'Michael'),
      ('Leslie', 'Rachael'),
      ('Leslie', 'Daniel'),
      ('Berniece', 'John'),
      ('Berniece', 'Terry'),
      ('Berniece', 'Lynda'),
      ('Berniece', 'Lorie'),
      ('Berniece', 'Barbara'),
      ('Berniece', 'Leslie'),
      ('Lorie', 'Cassie'))

q = var()

print('Practicing Commands...')

print((run(0, q, father('John', q))))  # John is the father of who?

# ('Jesse', 'Calli')
print((run(0, q, father(q, 'Michael'))))  # Who is the father of Michael?


def parent(p, child):
    return conde([father(p, child)], [mother(p, child)])


# ('Hector',)
print((run(0, q, parent(q, 'Daniel'))))  # Who is a parent of Daniel?


# ('Hector', 'Leslie')
def grandparent(gparent, child):
    p = var()
    return conde((parent(gparent, p), parent(p, child)))


print((run(0, q, grandparent(q, 'Calli'))))  # Who is a grandparent of Calli?
# ('Bruce', 'Berniece', 'Margie', 'Jim')
print((run(0, q, grandparent('Jim', q))))  # Jim is a grandparent of whom?


# ('Calli', 'Jesse')
def sibling(a, b):
    p = var()
    return conde((parent(p, a), parent(p, b)))


def relationToString(root):
    for item in root:
        print(re.sub(r" ?\([^)]+\)", "", item))
    rootStr = ""
    for item in root:
        rootStr = rootStr + item
    return rootStr


# All spouses
x, y, z = var(), var(), var()

print((run(0, (x, y), (father, x, z), (mother, y, z))), '\n')
# (('Hector', 'Leslie'), ('Bruce', 'Berniece'), ('Jim', 'Margie'), ('John', 'Mindy'))

print('Building Bruce and Berniece Family Tree...')
print('The Children of Bruce and Berniece are:')
print((run(0, q, father('Bruce', q))))
print('The Children of Terry are:')
print((run(0, q, father('Terry', q))))
print('The Children of Lynda are:')
print((run(0, q, mother('Lynda', q))))
print('The Children of Barbara are:')
print((run(0, q, mother('Barbara', q))))
print('The Children of Lorie are:')
print((run(0, q, mother('Lorie', q))))
print('The Children of Leslie are:')
print((run(0, q, mother('Leslie', q))))
print('The Children of John are:')
print((run(0, q, father('John', q))), '\n')

print('Building Margie and Jim Family Tree...')
print('The Children of Margie and Jim are:')
print((run(0, q, father('Jim', q))))
print('The Children of Jimmy are:')
print((run(0, q, father('Jimmy', q))))
print('The Children of Mindy are:')
print((run(0, q, mother('Mindy', q))))

bruce = (run(0, q, father(q, 'John')))
john = (run(0, q, father(q, 'Jesse')))
leslie = (run(0, q, mother(q, 'Daniel')))
jesseAndCalli = (run(0, q, father('John', q)))
MichaelDanielRachael = (run(0, q, mother('Leslie', q)))

## Create the family tree
tree = Tree()
tree.create_node(relationToString(bruce), relationToString(bruce).lower())  # root node
tree.create_node(relationToString(john), relationToString(john).lower(), parent=relationToString(bruce).lower())
tree.create_node(relationToString(leslie), relationToString(leslie).lower(), parent=relationToString(bruce).lower())
tree.create_node(relationToString(jesseAndCalli), relationToString(jesseAndCalli).lower(),
                 parent=relationToString(john).lower())
tree.create_node(relationToString(MichaelDanielRachael), relationToString(MichaelDanielRachael).lower,
                 parent=relationToString(leslie).lower())
tree.show()
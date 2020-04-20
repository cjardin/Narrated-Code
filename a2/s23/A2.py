# Fernando Juarez - Assignment 2
# Professor Jardin - Section 2
# March 20, 2020
from kanren import Relation, facts, run, conde, var, eq

father = Relation()
mother = Relation()

facts(father, ('Homer', 'Bart'), ('Homer', 'Lisa'), ('Homer', 'Maggie'), ('Abe', 'Homer'), ('Clancy', 'Marge'))
facts(mother, ('Marge', 'Bart'), ('Marge', 'Lisa'), ('Marge', 'Maggie'), ('Mona', 'Homer'), ('Jacqueline', 'Marge'))

x = var()
print("Fernando's Detailed Simpsons Family Tree")
print()
print("Who are Homer's Children?")
print((run(0, x, father('Homer', x))))  # Homer is the father of?
print()
print("Who is Bart's Father?")
print((run(0, x, father(x, 'Bart'))))  # Who is Bart's father?
print()
print("Who is Lisa's Mother?")
print((run(0, x, mother(x, 'Lisa'))))  # Who is Lisa's Mother?


def parent(p, child):
    return conde([father(p, child)], [mother(p, child)])


print()
print("Who are Maggie's Parents?")
print((run(0, x, parent(x, 'Maggie'))))  # Bart's Parents?
print()
print("Who are Marge's Parents?")
print((run(0, x, parent(x, 'Marge'))))  # Marge's Parents?
print()
print("Who are Homer's Parents?")
print((run(0, x, parent(x, 'Homer'))))  # Homer's Parents?


def grandparent(gparent, child):
    y = var()
    return conde((parent(gparent, y), parent(y, child)))


print()
print("Who are Bart's Grandparents?")
print((run(0, x, grandparent(x, 'Bart'))))  # Who is a grandparent of Bart?

print()
print("Who are Abe's Grand Children?")
print((run(0, x, grandparent('Abe', x))))  # Abe is a grandparent of?
print()
print("Who are Jacqueline's Grand Children?")
print((run(0, x, grandparent('Jacqueline', x))))  # Jacqueline is a grandparent of?

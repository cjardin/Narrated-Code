#Brian Perez
#Program 2
#Note: first time using Python

import kanren
from kanren import run, eq, membero, var, conde, Relation, facts
from kanren import vars
x = kanren.var()
z = kanren.var()
y = kanren.var()
a, b, c = kanren.vars(3)
print(run(1, x, eq(x, 5)))

print(run(1, x, eq(x, z), eq(z, 3)))

print(run(1, x, eq((1,2), (1,x))))

print(run(2,x, membero(x, (1,2,3)), membero(x, (2,3,4))))
print(a, b, c)

parent = Relation()
facts(parent, ("Homer", "Bart"),("Homer", "Lisa"),("Abe",  "Homer"))

print(run(1, x, parent(x, "Bart")))

print(run(2, x, parent("Homer", x)))

print(run(1, x, parent(x, y), parent(y, 'Bart')))
def grandparent(x, z):
 return conde((parent(x, y), parent(y, z)))
print(run(1, x, grandparent(x, 'Bart')))

pokemon = Relation()
disadvantage = Relation()
Type = Relation()
facts(Type, ("Charmander", "Fire"), ("Squirtle", "Water"), ("Bulbasaur", "Grass"))
facts(pokemon, ("Charmeleon", "Charmander"), ("Wartortle", "Squirtle"), ("Ivysaur", "Bulbasaur"))
facts(pokemon, ("Charizard", "Charmeleon"), ("Blastoise", "Wartortle"), ("Venusaur", "Ivysaur"))
facts(disadvantage, ("Water", "Fire"), ("Fire", "Grass"), ("Grass", "Water"))

def evolutions(x, z):
    return conde((pokemon(x,y), pokemon(y, z)))

print("Welcome!!! This program will help you decide what starting pokemon to pick from.\n")

resp = input("What is your favorite Pokemon type? (Grass, Water, or Fire)")

if resp == "Fire": 
    print("You might want to pick ", run(1, x, Type(x, "Fire")))
    print("\nIt will evolve into a ", run(1, x,  pokemon(x, "Charmander")))
    print("\nIt will then evolve into a ", run(1, x,  evolutions(x, "Charmander")))
elif resp == "Water":
    print("You might want to pick ", run(1, x, Type(x, "Water")))
    print("\nIt will evolve into a ", run(1, x,  pokemon(x, "Squirtle")))
    print("\nIt will then evolve into a ", run(1, x,  evolutions(x, "Squirtle")))
elif resp == "Grass":
    print("You might want to pick ", run(1, x, Type(x, "Grass")))
    print("\nIt will evolve into a ", run(1, x,  pokemon(x, "Bulbasaur")))
    print("\nIt will then evolve into a ", run(1, x,  evolutions(x, "Bulbasaur")))

print("\nBut be carefull of ", run(1, x,  disadvantage(x, resp)), " Pokemon; They are strong against your type.")
print("\nGood luck!!!\n\nGoodbye....\n")

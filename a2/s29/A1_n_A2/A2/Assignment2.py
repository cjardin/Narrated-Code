#Dionisio de Leon
#CS 351
#Programming assigment 2
#First time using python

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
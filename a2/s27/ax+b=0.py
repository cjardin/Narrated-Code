from kanren import run,var,fact
from kanren.assoccomm import eq_assoccomm as eq
from kanren.assoccomm import commutative,associative
add='add' #Defining operations
mul='mul'
fact(commutative,mul) #Addition and multiplication are commutative and associative
fact(commutative,add)
fact(associative,mul)
fact(associative,add)
x = var()
print("This program solves variable x for the general equation \"ax + b = 0\" with the provided a and b from user")
print("Enter a: ")
a = int(input())
print("Enter b: ")
b = int(input());
expression = (add,(mul, a, x), b)
expr1 = expression
expression = (add,(mul, a, (-b/a)),b)
print("x = ",run(1,x,eq(expr1,expression)))
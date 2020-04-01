import kanren
from kanren import run, vars, membero, var, conde, Relation, fact, facts
from kanren.assoccomm import eq_assoccomm as eq
from kanren.assoccomm import commutative, associative


# Function for displaying intro statement
def intro():
    print("\n\tAssignment 2")
    print("\tLogic Programming\n")


# Function for displaying pizza statement
def pizza():
    print("\nPIZZA!!!!!!!!!!!!")


# Function for displaying practice statement
def practice():
    print("Practice with Kanren")


# Function for displaying results statement
def results():
    print("\n**Results**")


# Declare Variables
x = kanren.var()
z = kanren.var()

# Heading
intro()
practice()
print(run(1, x, eq(x, 5)))
print(run(1, x, eq(x, z), eq(z, 3)))
print(run(1, x, eq((1, 2), (1, x))))
print(run(2, x, membero(x, (1, 2, 3)), membero(x, (2, 3, 4))))

z = kanren.var('test')
print(z)

a, b, c = vars(3)
print(a)
print(b)
print(c)

# Defining operations
add = 'add'
mul = 'mul'

# Addition and multiplication are commutative and associative
fact(commutative, mul)
fact(commutative, add)
fact(associative, mul)
fact(associative, add)

x, y = var('x'), var('y')
r, s = var('r'), var('s')

# Two expressions to match
pattern = (mul, (add, 1, x), y)  # (1 + x) * y
expr = (mul, 2, (add, 3, 1))  # 2 * (3 + 1)
print(run(0, (x, y), eq(pattern, expr)))  # prints ((3, 2),) meaning
#   x matches to 3
#   y matches to 2

pattern = (add, (mul, 2, r), s)  # (2 * r) + s
expr = (add, 5, (mul, 6, 2))  # 5 + (6  * 2)
print(run(0, (r, s), eq(pattern, expr)))  # prints ((6, 5),) meaning
#   r matches to 6
#   s matches to 5

results()
pizza()
pizza = Relation()
pizza2 = Relation()
facts(pizza, ('Pepperoni', 'Sausage'), ('Pepperoni', 'Bacon'), ('Ham', 'Pepperoni'))
facts(pizza2, ('Pineapple', 'Ham'), ('Pineapple', 'Sardines'), ('Anchovies', 'Pineapple'))

print(run(1, x, pizza(x, 'Sausage')))
print(run(2, x, pizza('Pepperoni', x)))
print(run(3, x, pizza2(x, 'Ham')))
print(run(4, x, pizza2('Pineapple', x)))


def mypizza(x, z):
    y = var()
    return conde((pizza(x, y), pizza(y, z)))


print(run(1, x, mypizza(x, 'Sausage')))
print("Making the perfect pizza...")

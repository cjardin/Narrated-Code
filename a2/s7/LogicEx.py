from kanren import run, eq, membero, var, vars, Relation, facts, conde
x = var()
run(1, x, eq(x, 5))
print(run(1, x, eq(x, 5)))

z = var()
print(run(1, x, eq(x,z), eq(z,3)))

print(run(1, x, eq((1, 2), (1, x))))

print(run(2,x,membero(x, (1,2,3)), membero(x,(2,3,4))))

z = var('test')
print(z)

a, b, c = vars(3)
print(a)
print(b)
print(c)

parent = Relation()
facts(parent, ("Homer", "Bart"), ("Homer", "Lisa"), ("Abe", "Homer"))
print(run(1, x, parent(x, "Bart")))
print(run(2,x,parent("Homer", x)))

y = var()
print(run(1,x,parent(x,y) , parent(y, 'Bart')))

def grandparent(x, z):
    y = var()
    return conde((parent(x,y), parent(y,z)))
print(run(1,x,grandparent(x, 'Bart')))

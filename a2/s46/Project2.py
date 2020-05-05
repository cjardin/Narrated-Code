from kanren import run, eq, membero, var

x = var()
z = var()

print(run(1, x, eq(x, 5)))

print(run(1, x, eq((1, 2), (1, x))))

print(run(2, x, membero(x, (1, 2, 3)), membero(x, (2, 3, 4))))
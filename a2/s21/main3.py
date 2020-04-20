from kanren import run, eq, membero, var, conde
x = var()
run(1, x, eq((1, 2), (1, x)))
print (run(1, x, eq((1, 2), (1, x))))
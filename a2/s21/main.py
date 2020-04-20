from kanren import run, eq, membero, var, conde
x = var()
run(1, x, eq(x, 5))
print (run(1, x, eq(x, 5)))

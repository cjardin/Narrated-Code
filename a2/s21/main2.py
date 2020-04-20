from kanren import run, eq, membero, var, conde
z = var()
x = var()
run(1, x, eq(x, z), eq(z, 3))
print (run(1, x, eq(x, z), eq(z, 3)))
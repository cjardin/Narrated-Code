from kanren import run, eq, membero, var, conde
print("****TEST KANREN AGAINST AN INPUTTED VALUE*****\r")
val = input("Enter your value: ")
print("You Entered:", (val))
x = var()
z = var()
z2 = var()
z = run(1, x, eq(x, val))
z2 = z[0]
if (z2 == val):
    print("CONGRATULATIONS, WE HAVE A MATCH:", z2, " == ", val)
else:
    print("SORRY, WE COULDN'T FIND A MATCH")


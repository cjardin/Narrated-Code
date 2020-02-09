from kanren import run, var, membero
import random

x = list(range(1,70))
y = list(range(1,27))
random.shuffle(x)
random.shuffle(y)

z = var()
print('These are your first 5 randomly chosen numbers to select on your powerball ticket!')
print(sorted(run(5, z, membero(z, x), membero(z, x), membero(z, x), membero(z, x), membero(z, x))))
print('This is your randomly chosen 6th powerball number to select on your powerball ticket!')
print(sorted(run(1, z, membero(z, (y)))))
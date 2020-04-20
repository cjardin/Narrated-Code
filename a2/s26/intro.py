from kanren import run, var, fact
from kanren.assoccomm import eq_assoccomm as eq
from kanren.assoccomm import commutative, associative

add = 'add'
mul = 'mul'

fact(commutative, mul)
fact(commutative, add)
fact(associative, mul)
fact(associative, add)

x, y = var('x'), var('y')

pattern = (mul, (add, 1, x), y)                
expr    = (mul, 2, (add, 3, 1))                
print(run(0, (x,y), eq(pattern, expr)))

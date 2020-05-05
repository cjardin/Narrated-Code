from account import Account
from kanren import unifiable, run, var, eq, membero, variables
from kanren.core import lall
from kanren.arith import add, gt, sub, lt

unifiable(Account)  # Register Account class

accounts = (Account('Adam', 'Smith', 1, 20),
            Account('Carl', 'Marx', 2, 3),
            Account('John', 'Rockefeller', 3, 1000))

# optional name strings are helpful for debugging
first = var('first')
last = var('last')
ident = var('ident')
balance = var('balance')
newbalance = var('newbalance')

# Describe a couple of transformations on accounts
source = Account(first, last, ident, balance)
target = Account(first, last, ident, newbalance)

theorists = ('Adam', 'Carl')
# Give $10 to theorists
theorist_bonus = lall((membero, source, accounts),
                      (membero, first, theorists),
                      (add, 10, balance, newbalance))

# Take $10 from anyone with more than $100
tax_the_rich = lall((membero, source, accounts),
                    (gt, balance, 100),
                    (sub, balance, 10, newbalance))

print("Take $10 from anyone with more than $100")
print((run(0, target, tax_the_rich)))

print("Give $10 to theorists")
print((run(0, target, theorist_bonus)))

stimulus = (Account('Donald', 'Trump', 4, 362000000),
            Account('Jon', 'Snow', 5, 65000),
            Account('Lebron James', 'Smith', 6, 37000000),
            Account('Naruto', 'Uzumaki', 7, 43000))

qualified = lall((membero, source, stimulus),
                 (lt, balance,75000),
                 (add, 1200, balance, newbalance))
                 
not_qualified = lall((membero, source, stimulus),
                     (gt, balance, 75000),
                     (add, 0, balance, newbalance))
                     
print("Sorry you make too much money")
print((run(0, target, not_qualified)))

print("Give $1200 stimulus checks to qualified Americans")
print((run(0, target, qualified)))

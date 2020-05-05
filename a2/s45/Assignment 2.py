from kanren import isvar,run,membero
from kanren.core import success,fail,goaleval,condeseq,eq,var
from sympy.ntheory.generate import prime,isprime
import itertools as it

def prime_test(n):
    if isvar(n):
        return condeseq([(eq,n,p)] for p in map(prime,it.count(1)))
    else:
        return success if isprime(n) else fail


def one():
    return (run(int(a), n, prime_test(n)))


def two():
    i = int
    i = 0
    result = False
    temp = var()
    temp = run(int(a), n, prime_test(n))
    while i < int(a):
        if(int(a) == int(temp[i])):
            result = True
            i = i+1
        else:
            i = i+1
    if result == True:
        return("{} is prime".format(a))
    else:
        return("{} is not prime".format(a))

def three():
    i = int
    i = 0
    factor = []
    temp = var()
    result = False
    temp = run(int(a), n, prime_test(n))
    while i < int(a):
        if(int(a) == int(temp[i])):
            result = True
            i = i+1
        else:
            i = i+1
    if result == True:
        return("{} is a prime number".format(a))
    else:
        i = 0
        while int(temp[i]) < int(a):
            if(int(a)%int(temp[i]) == 0):
                factor.append(int(temp[i]))
                i = i+1
            else:
                i = i+1

    return(factor)


def four():
    i = int
    i = 1
    num = []
    while i <= int(a):
        num.append(i)
        i = i+1

    return((set(run(0, n, (membero, n, num), (prime_test, n)))))


def five():
    i = int
    i = 0
    temp = var()
    temp = run(int(a), n, prime_test(n))

    while int(temp[i]) < int(a):
        i = i+1

    i = i-1
    if int(temp[i+1]) == int(a):
        return("{} is a prime number".format(a))

    else:
        j = int
        k = int
        j = int(a) - int(temp[i])
        k = int(temp[i+1]) - int(a)
        if j < k:
            return("{} is the closest prime number".format(temp[i]))
        elif k < j:
            return("{} is the closest prime number".format(temp[i+1]))
        else:
            return("{} and {} are the closest prime numbers".format(temp[i], temp[i+1]))


def six():
    temp = var()
    temp = run(int(a), n, prime_test(n))
    i = int
    i = 0
    z = int
    z = 0

    while int(temp[i]) < int(a):
        i = i+1

    if int(temp[i]) == int(a):
       j = int
       k = int
       jresult = False
       kresult = False
       j = int(temp[i]) + 6
       k = int(temp[i]) - 6
       temp = run(int(j), n, prime_test(n))

       while z < int(j):
           if (int(j) == int(temp[z])):
               jresult = True
               z = z + 1
           else:
               z = z + 1

       z = 0

       while z < int(k):
           if (int(k) == int(temp[z])):
               kresult = True
               z = z + 1
           else:
               z = z + 1

       if  jresult == True and kresult == False:
           return("{} is a Sexy Prime with {}".format(a, str(j)))
       elif kresult == True and jresult == False:
           return("{} is a Sexy Prime with {}".format(a, str(k)))
       elif jresult == True and kresult == True:
            return("{} is a Sexy Prime with {} and {}".format(a, str(j), str(k)))
       else:
           return("{} does not have a Sexy prime".format(a))

    else:
        return("{} is not a prime number".format(a))


def seven():
    return("Thank you for using this program")

def choice(argument):
    switcher = {
        1: one,
        2: two,
        3: three,
        4: four,
        5: five,
        6: six,
        7: seven
    }
    func = switcher.get(argument, lambda: "Invalid choice")
    print(func())

n = var()
x = var()
a = int
b = int
b = 0
a = input("Please enter the number that you wish to discover some fun prime facts about: ")
print("What would you like to do?")
print("Enter 1 for the first {} primes".format(a))
print("Enter 2 to see if {} is prime".format(a))
print("Enter 3 to get the prime factors of {}".format(a))
print("Enter 4 to get all primes from the first {} integers".format(a))
print("Enter 5 to find the closest prime number to {}".format(a))
print("Enter 6 to check if {} has a Sexy Prime counterpart".format(a))
print("Enter 7 to exit")

while int(b) != 7:
    b = input()
    choice(int(b))

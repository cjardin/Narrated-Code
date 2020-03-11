from kanren import run, eq, membero, vars, conde, Relation, facts, var
from unification.match import *
from art import *

def menu():
    tprint("Logic  Based  Programming!!")
    print("===========\n")
    print("Options:\n")
    print("1. Logic based programming examples")
    print("2. Calculate fibonacci number")
    print("3. Encript a message")
    print("4. Decript a message")
    print("5. Exit")
    
    option = input("Please Select the Calculation Option: ")
    print(option)
    option_int = int(option)
    if option_int < 6:
        if option_int == 1:
            logicBased()
        if option_int == 2:
            getFib()
        if option_int == 3:
            encrypt()
        if option_int == 4:
            decrypt()
        if option_int == 5:
            exit_func()
    else: # if the input is above 6
        print("Wrong option!\n")
        print("Try again...")
        menu() # loops menu function

### basic logic programming taken from github ###
def logicBased():
    x  = var()
    print(run(1,x,eq(x,5)))
    z = var()
    print(run(1,x,eq(x,z),
            eq(z,3)))

    print(run(1,x,eq((1,2), (1,x))))

    print(run(2, x, membero(x, (1,2,3)),
              membero(x, (2,3,4))))

    z = var('test')
    print(z)

    a, b, c = vars(3)
    print(a)
    print(b)
    print(c)

    parent = Relation()
    facts(parent, ("Homer", "Bart"),
                  ("Homer", "Lias"),
                  ("Abe", "Homer"))
    print(run(2, x, parent("Homer", x)))

    y = var()
    print(run(1, x, parent(x, y),
              parent(y, 'Bart')))

    def grandparent(x, z):
        y = var()
        return conde((parent(x,y), parent(y,z)))

    print(run(1, x, grandparent(x, 'Bart')))
    menu() #calls the menu function (a menu loop)

### base case ###
@match(0)
def fib(n):
    return 0

### base case ###
@match(1)
def fib(n):
    return 1

### base case ###
@match(n)
def fib(n):
    #fib solved with recurtion
    return fib(n - 1) + fib(n - 2) #calls itself

### get the fib number from the function fib ###
def getFib():
    #asks for the fib number
    n = int(input("What fib number would you like solved for? \n")) 
    print(fib(n)) #prints the output from fib function
    menu()


### basic encrypter shifts depending on the input to give original text ###         
def encrypt():
    s = int(input("Input the shift of the cipher:\n"))
    z = var(s)
    print(s)
    text = input("Input message to be encripted:\n")
    result = ""
   # transverse variable text
    for i in range(len(text)):
        char = text[i]
          # shift uppercase characters to right
        if (char.isupper()):
            result += chr((ord(char) + s - 65) % 26 + 65)
          #  print(text[i])
             # shift lowercase characters to the right
        else:
             result += chr((ord(char) + s - 97) % 26 + 97)
    print(result)
    menu()

### basic decrypher shifts depending on the input to give original text ###
def decrypt(): 
    s = int(input("Input the shift of the cipher:\n")) 
    z = var(s)
    print(s)
    text = input("Input message to be decrypted:\n")
    i = 0
    result = ""
   # transverse variable text
    for i in range(len(text)):
        char = text[i]
          # shift uppercase characters to left
        if (char.isupper()):
            result += chr((ord(char) - s - 65) % 26 + 65)
          #  print(text[i])
             # shift lowercase characters to left
        else:
             result += chr((ord(char) - s - 97) % 26 + 97)
    print(result)
    menu()

### exits program ###
def exit_func():
    exit

menu() #driver

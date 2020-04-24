#/bin/python
''' Ezer Patlan, CS351, Instructor: Mr. Cary Jardin
Kanren/Python Libraries
'''
from kanren import isvar, run, membero, facts, Relation
from kanren.assoccomm import eq_assoccomm as eq
from kanren.assoccomm import commutative, associative
from kanren.core import success, fail, goaleval,conde, condeseq, eq, var, everyg
from kanren.goals import permuteq
from sympy.ntheory.generate import prime, isprime
import itertools as it
import json
import numpy as np


'''
Logic Programming using kanren libraries
Incorporating a representing knowledge of kanren library and 
find the relationship of how many employees from the database 
have the same job type. The prime number functions from kanren were implemented,
to minimize the quantity of the database.
'''
'''
prime function to check whether it is a prime or not
'''
def prime_check(x):
    '''
    if is a variable
    '''
    if isvar(x):
        '''
        return the sequence of prime numbers
        '''
        return condeseq([(eq,x,p)] for p in map(prime, it.count(1)))
    else:
        '''
        else if is successful then check is prime and if is not then it fails
        '''
        return success if isprime(x) else fail

'''
read the json file and store in data
'''
# read json
with open('profile2.json') as f:
    data = json.load(f)

'''
find the total number of employees
'''
total_employees = np.arange(1,len(data),1);

'''
intialize variable n
'''
n = var()
'''
check the array and filter the numbers that are prime numbers
'''
result_id=run(0,n,(membero,n,(total_employees)),(prime_check,n))

'''
the attributes is for the user to read the data
'''
attributes = ['index','prime','first','last','jobtype'];
print('\nHere are all the prime numbers from the database:')
'''
print the attributes
'''
print('\n'+'\t'.join(attributes))
print('='*57)
'''
for loop prints the prime numbers of all employees
'''
for index,i in enumerate(result_id):
    print(index,data[i-1]["id"],data[i-1]["firstName"],data[i-1]["lastName"],data[i-1]["jobType"])

'''
Initialize the relations and variables
'''

# Initialize the relations:
jobType = Relation()
x = var()
y = var()
z = var()

'''
store the employee data into the facts to build our relationship and constraints using the Kanren libraries
'''
for index,i in enumerate(result_id):
    facts(jobType,(data[i-1]["jobType"],data[i-1]["firstName"],data[i-1]["lastName"],str(data[i-1]["id"])))

'''
print the solutions and find out how many jobtype they do correspond for each question
'''
findType = ['Engineer','Architect','Consultant','Producer','Manager']
for i in findType:
    '''
    the x,y,z are empty variables and are going to fillout as output solution and find the correlation and
    print the names of the employees that belong in that specific profession.
    '''
    output = run(0, (x,y,z), jobType(i,x,y,z))
    attributesResults= ['firstname','lastname','prime']
    print('\nList the names of the '+i+':')
    print('\n'+'\t'.join(attributesResults))
    print('='*57)
    # Extract the output
    for item in output:
        print('\t\t'.join([str(x) for x in item]))
    
    print('*'*57)



'''
Sudoku Function - possible(y,x,n) and solve(grid)
written by Dr. Thorsten Altenkirch on a recursive Sudoku solver.
Modifing the code and incorporated into the kanren libraries to test
puzzle algorithm.
'''
'''
Possible Function
It finds the missing number by giving the location coordinates of the cell.
For example, x and y are the index of the board, once located the cell.
It will began searching numbers inside the 3x3 matrix
and if the input number does not match the numbers inside the small grid.
The input number will be store inside the empty cell from the 3x3 matrix grid.
'''
def possible(y,x,n):
    ''' initialize variables'''
    global grid
    array=[]
    ''' initialize for loop and if true there is no number similar to the
    input number inside the row or column of the grid or board.'''
    for i in range(0,9):
        if grid[y][i]==n:
            if grid[i][x]==n:
                return False
    ''' initialize variables and calculate the index location of the board.'''
    output=var()
    x0=(x//3)*3
    y0=(y//3)*3
    ''' initialize a for loop and store the values inside array'''
    for i in range(0,3):
        for j in range(0,3):
            array.append(grid[y0+i][x0+j])
    ''' Applying Kanren functions into the Sudoku algorithm.
    The functions are use to implement a logic program to verify
    whether the input variable is identical to the numbers inside the array.
    If there is no numbers identical to the numbers inside the array, then
    the function will return True.'''
    find_number=run(1,output,eq(output,n),membero(output,array))
    if len(find_number) != 0:
        return False
    return True


''' solve function is a recursive function. It will go through every cell of the grid
and apply the possible function. If the input is True then inside the if statement, it will
store the input into the grid cell. After, it will recursive into the solve function again, until
it solves all empty cells from the sudoku puzzle.'''
def solve(grid):
    for y in range(9):
        for x in range(9):
            if grid[y][x] == 0:
                for n in range(1,10):
                    if possible(y,x,n):
                        grid[y][x] = n
                        grid=solve(grid)
    return grid   



'''
grid Data
'''
print("\n")
print("Input Sudoko")
grid = [[5,3,0,0,7,0,0,0,0],
        [6,0,0,1,9,5,0,0,0],
        [0,9,8,0,0,0,0,6,0],
        [8,0,0,0,6,0,0,0,3],
        [4,0,0,8,0,3,0,0,1],
        [7,0,0,0,2,0,0,0,6],
        [0,6,0,0,0,0,2,8,0],
        [0,0,0,4,1,9,0,0,5],
        [0,0,0,0,8,0,0,7,9]]

''' Print the output and store the output'''
print(np.matrix(grid))
print("\n")
print("Solve Sudoku")
result = solve(grid)
print(np.matrix(result))
print("\n")

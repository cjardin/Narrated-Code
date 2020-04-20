#/bin/python
''' Ezer Patlan, CS351, Instructor: Mr. Cary Jardin
Kanren/Python Libraries
'''
from kanren import isvar, run, membero, facts, Relation
from kanren.assoccomm import eq_assoccomm as eq
from kanren.assoccomm import commutative, associative
from kanren.core import success, fail, goaleval,conde, condeseq, eq, var
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

#Emanuel Ordonez
#Assignment 2
#CS 351

import kanren
from kanren import run, var, conde, Relation, facts

cor = 'CS 351'
prof = 'Cary Jardin'

#assigning professor to a course
course = Relation()
facts(course,(cor, prof))

#assigning professor to all students
professor = Relation()

#value to help use run
def studies(c,student):
        return conde((course(c,prof),professor(prof,student)))

#Menu for app
print('\n\nCourse Menu')
print('_____________________________')
print('1: Course Name')
print('2: Professor Name')
print('3: Add a student')
print('4: Students in course')
print('5: Quit')
print('_____________________________\n')


while True:
    try:
        num = int(input('Enter your choice: '))
    except:
        print('MUST BE AN INTEGER')
        break
    
    if num == 1:
        print(cor,'\n')

    elif num == 2:
        x= kanren.var()
        print(run(0,x,course(cor,x)),'\n')
            
    elif num == 3:
        stu = input('Enter Student Name: ')
        facts(professor,(prof,stu))
        print(stu , ' has been added to students\n')
            
    elif num == 4:
        y=kanren.var()
        print(run(0,y,studies('CS 351',y)),'\n')
            
    elif num == 5:
        exit()
            
    else:
        print('MUST BE AN IN BETWEEN 1-5\n')

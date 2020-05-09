from kanren import run, eq, membero, vars, conde, Relation, facts, var


#Austin Bradstreet, 004880497
#CS-351, 1st attempt at using Python


care = 'Austin'
shel = 'Valley of Animal Friends'


caretaker = Relation()

shelter = Relation()
facts(shelter,(shel, care))

animal_name = Relation()

def contains(s,animal):

        return conde((shelter(s,care),caretaker(care,animal)))



print('\nAnimal Shelter menu')
print('______________________')
print('1: Animal Shelter Name')
print('2: Caretaker Name')
print('3: Animals in shelter')
print('4: Add animals')
print('5: Add name to animal')
print('6: exit')
print('_______________________\n')


while True:
    try:
        num = int(input('Enter a number for a category '))
    except:
        print('Sorry, please enter a number between 1 and 6')
        break
    
    if num == 1:
        print(shel,'\n')

    elif num == 2:
        x= kanren.var()
        print(run(0,x,caretaker(care,x)),'\n')
            
    elif num == 3:
        y= kanren.var()
        print(run(0,y,contains('Dog',y)),'\n')

    elif num == 4:
        ani = input('Enter type of animal ')
        facts(caretaker,(care,ani))
        print(ani , ' has been added to the list of animals\n')

    elif num == 5:
        name = input('Enter name for animal ')
        facts(animal_name,(ani,name))
        print('This animal has been named ' , name '\n')
            
    elif num == 6:
        exit()
            
    else:
        print('Sorry, please enter a number between 1 and 6\n')

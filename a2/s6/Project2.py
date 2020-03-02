#project 2-Author: Luke Landon- Class CS 351- Note First time programing ever in Python
import kanren 
from kanren import run, eq, membero, var, conde, Relation, facts
import random 
x = kanren.var()
print(run(1, x, eq(x, 5)))
#asks for a number x such that x is equal to z and z is equal to 3
z = kanren.var()
print(run(1,x, eq(x,z),eq(z,3)))
#asks for a number x such that 1,2 equals 1,x 
print(run(1,x, eq((1,2),(1,x))))
#uses membero twice to ask for 2 values of x such that x is a member of 1,2,3 and that x is a member of 2,3.4
print(run(2, x, membero(x, (1, 2, 3)), membero(x, (2, 3, 4))))
#creates a logic variable
z = kanren.var('test')
print(z)
#creates multiple logic variables at once
a, b, c = var('a'), var('b'), var('c')
print(a)
print(b)
print(c)
#creates a parent relationship and uses it to state facts about who is related to who
parent = Relation()
facts(parent, ("Homer", "Bart"),("Homer", "Lisa"),("Abe",  "Homer"))
print(run(1, x, parent(x, "Bart")))
print(run(2, x, parent("Homer", x)))
#uses intermediate variables for complex queries
y = var()
print(run(1, x, parent(x, y), parent(y, 'Bart')))
#express the grandfather relationship seperatly using conde
def grandparent(x, z):
 y = var() 
 return conde((parent(x, y), parent(y, z)))
print(run(1, x, grandparent(x, 'Bart')))

#in this logic it connects the data values to specific days and their grandparent 
#relationship: an example would be Tuesday and its classes-each class then is 
#connected to a time so if you call a relationship of a day it will give you the
#classes you take on that day. If you call the grandparents of that day it will 
#give you the time of each one of those classes connected to Tuesday. This makes 
#a way to create a calender using parent and grandparent calls for specific days

dayCal = Relation()#creates a relationship called dayCal
#puts facts into dayCal and connects the parents and grandparent of each
facts(dayCal, ("Cs 441", "Tuesday"), ("Cs 485","Tuesday"), ("Cs 351","Tuesday"), ("Math 242","Tuesday"))
facts(dayCal, ("9:00-10:15", "Cs 441"), ("1:00-2:15","Cs 485"), ("2:30-3:45","Cs 351"), ("4:00-5:15","Math 242"))
facts(dayCal, ("Cs 441", "Thursday"), ("Cs 485","Thursday"), ("Cs 351","Thursday"), ("Math 242","Thursday"))
facts(dayCal, ("Homework","Monday"), ("Job work", "Monday"))
facts(dayCal, ("8:00-12:00","Homework"), ("1:00 - 9:15","Homework"))
facts(dayCal, ("Homework","Wednesday"), ("Job work", "Wednesday"))
facts(dayCal, ("Homework","Friday"), ("Job work", "Friday"))
#creates the relationship of grandparents to dayCal
def grandparent(x, z):
 y = var() 
 return conde((dayCal(x, y), dayCal(y, z)))
#prints out each days relationship in order of monday to friday
print("\n This is my schedule for the week \n")
print("Monday: ")
print(run(4, x, dayCal(x,"Monday")))
print("\n These are the times:")
print(run(4, x, grandparent(x, 'Monday')))
print("\n Tuesday: ")
print(run(4, x, dayCal(x,"Tuesday")))
print("\n These are the times:")
print(run(4, x, grandparent(x, 'Tuesday')))
print("\n Wednesday: ")
print(run(4, x, dayCal(x,"Wednesday")))
print("\n These are the times:")
print(run(4, x, grandparent(x, 'Wednesday')))
print("\n Thursday: ")
print(run(4, x, dayCal(x,"Thursday")))
print("\n These are the times:")
print(run(4, x, grandparent(x, 'Thursday')))
print("\n Friday: ")
print(run(4, x, dayCal(x,"Friday")))
print("\n These are the times:")
print(run(4, x, grandparent(x, 'Friday')))
print("\n")

x1 = list(range(1,5))    #creates a list that will hold 4 values randomized from 1-4
musicBox = []            #creates a empty list to hold the notes of the musicbox
random.shuffle(x1)       #randomizes the galues in x1
i = 0                       
while i < 4:             #loops through i untill it is is 4
	if x1[i] == 1:       #checks to see if the value of the list is 1
		musicBox.append("A") 	#adds A to the music box
	if x1[i] == 2:       #checks to see if the value of the list is 2
		musicBox.append(" B") 	#adds B to the music box
	if x1[i] == 3:       #checks to see if the value of the list is 3
		musicBox.append("  C") 	#adds C to the music box
	if x1[i] == 4:       #checks to see if the value of the list is 4
		musicBox.append("   D") #adds D to the music box
	i+=1                 #adds 1 to i
print("Notes for Music Box")
print(*musicBox, sep = "\n") #prints all values in the music box on a new line








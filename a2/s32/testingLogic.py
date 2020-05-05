from kanren import run, eq, membero, var, conde, vars, Relation, facts 

price = Relation()
userRatings = Relation()
screenSize = Relation()
pixelDensity = Relation()
numOfCores = Relation()
weight = Relation()

print("Apple Iphone 11 Pro VS Samsung Galaxy S20 Ultra")
print()

facts(price, ('1000', 'Iphone 11'), ('1200', 'S20'))
facts(userRatings, ('4.7', 'Iphone 11'), ('4.6', 'S20'))
facts(screenSize, ('5.8 inches', 'Iphone 11'), ('6.9 inches', 'S20'))
facts(pixelDensity, ('358 PPI', 'Iphone 11'), ('511 PPI', 'S20'))
facts(numOfCores, ('6 Core', 'Iphone 11'), ('8 Core', 'S20'))

print("If answer Iphone then enter 1, if S20 then enter 2")
answer = input("Which do you think has a better price? ")

applePrice = (run(1,x,price(x,"Iphone 11")))[0]
samsungPrice = (run(1,x,price(x,"S20")))[0]
if answer == "1":
	print("You are right! The Iphone only costs $", applePrice)
elif answer == "2":
	print("You are wrong! The Samsung costs $", samsungPrice, " which is more than ", (int(samsungPrice) - int(applePrice)), " dollars")
else:
	print("Wrong input!")

print()

answer = input("Which do you think has a better rating? ")

appleRating = (run(1,x,userRatings(x,"Iphone 11")))[0]
samsungRating = (run(1,x,userRatings(x,"S20")))[0]
if answer == "1":
	print("You are right! The Iphone is a better reviewed phone at a ", appleRating, " out of 5")
elif answer == "2":
	print("You are wrong! The Samsung has a rating of ", samsungRating, " out of 5, which is less than ", round(float(appleRating) - float(samsungRating), 2), " points than samsung")
else:
	print("Wrong input!")

print()

answer = input("Which do you think has a bigger size? ")

appleSize = (run(1,x,screenSize(x,"Iphone 11")))[0] 
samsungSize = (run(1,x,screenSize(x,"S20")))[0]
if answer == "1":
	print("You are right! The S20 is a better reviewed phone at ", samsungSize)
elif answer == "2":
	print("You are wrong! The IPhone is ", appleSize, " , which is less than ", round(float(samsungSize[0:3]) - float(appleSize[0:3]), 2), " inches than samsung")
else:
	print("Wrong input!")

print()

answer = input("Which do you think has a bigger pixel density(PPI)? ")

applePixel = (run(1,x,pixelDensity(x,"Iphone 11")))[0] 
samsungPixel = (run(1,x,pixelDensity(x,"S20")))[0]
if answer == "1":
	print("You are right! The S20 is said to be ", samsungPixel, " pixels per inch")
elif answer == "2":
	print("You are wrong! The IPhone is ", applePixel, " , which is about ", (float(samsungPixel[0:3]) - float(applePixel[0:3])), " less pixels per inch than Samsung")
else:
	print("Wrong input!")

print()

answer = input("Which do you think has a bigger pixel density(PPI)? ")

appleCores = (run(1,x,numOfCores(x,"Iphone 11")))[0] 
samsungCores = (run(1,x,numOfCores(x,"S20")))[0]
if answer == "1":
	print("You are right! The S20 has ", samsungCores, " cores")
elif answer == "2":
	print("You are wrong! The IPhone has ", appleCores, " , which is ", (int(samsungCores[0]) - int(appleCores[0])), " less cores than Samsung")
else:
	print("Wrong input!")
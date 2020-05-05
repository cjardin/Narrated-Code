from kanren import run, eq, membero, var, conde, Relation, facts


def check(nb, listing):
    if (nb == 0):
        print (" You have not any " + listing)
        return (0)
    else:
        return (1)

def show(y, listing):
    for v in y:
        result.append(v)
        for i in range(len(result)):
            result[i]
    print (" You have " + str(i + 1) + " " + listing + " :")
    for i in range(len(result)):
        print ("==> " + result[i])
    
employee = Relation()
Trainee = Relation()
traineenb = 0
managernb = 0
managednb = 0


username = input(" Hello, I'am doing the listing of the employees and they're managers\n What is your name ?\n")
print(" Welcome " + username + "!\n")

Employees = input(" You have to add your manager, the people you are managing and your trainee if you have one\n Enter the keyword you need to enter ?\n Manager, Managed, Trainee\n")

while (1):
    if (Employees == "Trainee" or Employees == "trainee"):
        trainee = input(" Enter the name of your trainee\n")
        facts(Trainee,   (username, trainee))
        traineenb += 1
    if (Employees == "Managed" or Employees == "managed"):
        sidekick = input(" Enter the name of the person managed by you\n")
        facts(employee,   (username, sidekick))
        managednb += 1
    if (Employees == "Manager" or Employees == "manager"):
        manager = input(" Enter the name of your manager\n")
        facts(employee,   (manager, username))
        managernb += 1
    if (Employees == "stop" or Employees == "STOP" or Employees == "Stop"):
        break
    Employees = input(" Who do you wan't to add now ?\n Trainee, Manager, Managed or STOP\n")
                    
listing = input(" What do you want to know ?\n Who is your Trainee, Manager or Managed ?\n")
x = var()
y = var()
i = 0
result = []
while (1):
    if ((listing== "Trainee" or listing == "trainee") and check(traineenb, listing) == 1):
        y = run(traineenb, x, Trainee(username, x))
        show(y, listing)
    if ((listing == "Managed" or listing == "managed") and check(managednb, listing) == 1):
        y = run(managednb, x, employee(username, x))
        show(y, listing)
    if ((listing == "manager" or listing == "Manager") and check(managernb, listing) == 1):
        y = run(managernb, x, employee(x, username))
        show(y, listing)
    if (listing == "stop" or listing == "Stop" or listing == "STOP"):
        break
    y = var()
    listing = input(" What do you want to know ?\n Who is your Trainee, Manager or Managed or STOP?\n")


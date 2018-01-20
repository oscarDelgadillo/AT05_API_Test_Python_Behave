from CommercialEmployee import CommercialEmployee
from ProductionEmployee import ProductionEmployee


def readAmountEmployee():
    while True:
        print("Please intro the amount of the employee")
        cant = input()
        try:
            cant = int(cant)
            if cant > 2 and cant < 16:
                return cant
            print("Only numbres in range 3 to 15")
        except ValueError:
            print("ATTENTION: You must enter a whole number.")

def readTheName(i):
    print(f"Enter the {i} name:")
    name=input()

def readThePiece(i):
    while True:
        print(f"Enter the {i} pieces:")
        pie=input()
        try:
            pie = int(pie)
            if pie >= 0 :
                return pie
            print("Only numbres in range 3 to 15")
        except ValueError:
            print("ATTENTION: You must enter a whole number.")

def readThePieceDef(i):
    while True:
        print(f"Enter the {i} pieces defective:")
        pie=input()
        try:
            pie = int(pie)
            if pie >= 0 :
                return pie
            print("Only numbres in range 3 to 15")
        except ValueError:
            print("ATTENTION: You must enter a whole number.")

def readTheDepartament(i):
    print(f"Enter the departament (commercial or production) ")
    dep=input()
    if dep == "commercial":
        return  "commercial"
    return "production"


listPerson=[]

def loadEmployee():
    cant = readAmountEmployee()
    for i in range(1, cant+1):
        name=readTheName(i)
        dep=readTheDepartament(i)

        employee=0
        if(dep=="commercial"):
            price = readThePiece(i)
            employee =CommercialEmployee(name, price, dep, i)
        else:
            price = readThePiece(i)
            price2 = readThePieceDef(i)
            employee = ProductionEmployee(name, price, price2, dep, i)

        listPerson.append(employee)



def printList():
    print(f"List of the Employee {len(listPerson)}")
    for i in range(0, len(listPerson)):
        print(listPerson[i].getEmployee())

loadEmployee()
printList()
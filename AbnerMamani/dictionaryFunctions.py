

myDictionary={}
def readTheCantOfDictionari():
    while True:
        print("Please enter the number of items in your Dictionary")
        cant=input()
        try:
            cant = int(cant)
            return cant
        except ValueError:
            print("ATTENTION: You must enter a whole number.")

def loadDictionary():
    global myDictionary
    cant=readTheCantOfDictionari()
    for i in range(1, cant + 1):
        print(f"Plase enter the {i} Key :")
        myKey=input()
        print(f"Plase enter the {i} value :")
        myValue=input()
        myDictionary[myKey]=myValue
def printDictionaryKey():
    print(myDictionary.keys())

def printDictionaryValues():
    print(myDictionary.values())


def printDictionary():
    print(myDictionary)

def keyExistsInDictionary(k):
    if k in myDictionary.keys():
        return True
    else:
        return False

def valueExistsInDictionary(va):
    if va in myDictionary.values():
        return True
    else:
        return False

def readAnewKey():
    while True:
        key=input()
        if keyExistsInDictionary(key):


loadDictionary()
printDictionaryKey()
printDictionaryValues()
printDictionary()

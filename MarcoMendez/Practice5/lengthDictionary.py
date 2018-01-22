dict ={}

def lengthDictionary():
    length = int(input(" Dictionary size... "))
    i = 0
    while (i < length):
        key = input(" put key ")
        value = input(" put value ")
        dict[key] = value
        i += 1
    return dict

def printKeysDictiory():
    print(dict.keys())

def printValuesDictiory():
    values = dict.values()
    print("Dictonary values", values)

def printDictiory():
    print("Dictonary ", dict)

def printKeyExistInDictiory(key):
    print("Key "f"{key}"" = exist" if key in dict else "Key "f"{key}"" =  not exist")

def printValueExistInDictiory(value):
    print("Value "f"{value}"" = exist" if value in dict.values() else "Value "f"{value}"" =  not exist")

def getDirectory():
    return dict

#lengthDictionary()
#printKeysDictiory()
#printValuesDictiory()
#printDictiory()
#printKeyExistInDictiory("hola")
#printKeyExistInDictiory("5")
#printValueExistInDictiory("10")
#printValueExistInDictiory("hello")

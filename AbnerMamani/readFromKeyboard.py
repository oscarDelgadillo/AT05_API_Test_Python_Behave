
#Function to read only integer
def readInteger():
    while True:
        print("please enter the number of items in your list")
        cant = input()
        try:
            cant = int(cant)
            return cant
        except ValueError:
            print ("ATTENTION: You must enter a whole number.")

#Function to load the list
def readFronKeyboard():
    cant=readInteger() #input()
    list=[]
    for i in range(1,int(cant)+1):
        print(f"enter the {i} element")
        list.append(input())
    return list

#Function to display de list
def displayTheList(li):
    print(li)

displayTheList( readFronKeyboard())

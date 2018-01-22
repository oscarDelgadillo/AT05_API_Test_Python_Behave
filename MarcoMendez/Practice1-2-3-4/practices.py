def practice1():
    longuitud = int (input(" List size? "))
    size = longuitud
    list = []
    i = 0
    print(size,type(longuitud))
    while(i < longuitud):
        value = input(" value ")
        list.insert(i,value)
        i += 1
    return list

def practice2():
   print( practice1() )

practice2()
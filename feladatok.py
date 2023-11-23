def elso(lista):
    for i in range(0,len(lista),1):
        print(lista[i], end=", ")

def masodik(lista):
    osszeg:float = 0
    for i in range(0,len(lista),1):
        if lista[i] > 0:
            osszeg+=lista[i]
    return osszeg

def harmadik(lista):
    osszeg:float = 0
    for i in range(0,len(lista),1):
        if lista[i] < 0:
            osszeg+=lista[i]
    return osszeg

def negyedik(lista):
    osszeg:float = 0
    for i in range(0,len(lista),1):
        if lista[i] % 1 ==0:
            osszeg+=1
    return osszeg

def otodik(lista):
    osszeg:float = 0
    szamlalo:float = 0
    atlag:float = 0
    for i in range(0,len(lista),1):
        if lista[i] % 3 == 0:
            osszeg+=lista[i]
            szamlalo+=1
    atlag=osszeg/szamlalo
        
    return atlag

def hatodik(lista):
    max:float = 0
    for i in range(0,len(lista),1):
        if lista[i] > max:
            max = lista[i]
    return max

def hetedik(lista):
    min:float = 0
    for i in range(0,len(lista),1):
        if lista[i] < min:
            min = lista[i]
    return min
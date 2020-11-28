import random

rows = int(input("Ingrese la cantidad de filas:"))
columns = int(input("Ingrese la cantidad de columnas:"))

c = 0

while rows > c:
    x = 0
    a = []
    while columns > x:
        a.append(random.randint(-(rows*columns), rows*columns))
        x += 1
    print(a)
    c += 1
    
    
    
    


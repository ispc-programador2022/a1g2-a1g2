def potencia (b,e):
    p = b ** e
    return p
    
b=int(input("Ingrese un valor para la base B: "))
e=int(input("Ingrese un valor para el exponente E: "))
p = potencia (b,e)
print ("La potencia de B elevado al exponente E es igual a: ", p)
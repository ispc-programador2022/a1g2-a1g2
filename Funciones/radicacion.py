def radicacion (a,n):
    b = pow(a,1/n)
    return b
    
a=int(input("Ingrese un valor para el radicando A: "))
n=int(input("Ingrese un valor para el índice N: "))
b = radicacion (a,n)

if a < 0:
    print ("A debe ser no negativo para que exista su raiz")
else:
    print ("La raiz es igual a: ", b)
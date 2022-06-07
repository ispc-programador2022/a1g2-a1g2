#Funcion resta que debe retornar la resta de 2 parametros

def resta(a,b):
    c=a-b
    return c

a=int(input("Digite valor A: "))
b=int(input("Digite valor B: "))
c=resta(a,b)
print("El Resultado de la resta es: ",c)
from genrnd import genrnd
def genrndsum():
    x = genrnd()
    suma = 0
    for i in x:
        suma += i
    return suma

print(genrndsum())
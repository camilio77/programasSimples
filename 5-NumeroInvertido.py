#invertir los numeros de una cadena de numeros
cadena = input("ingrese cadena de 3 numeros: \n")
invertir = ""
for i in range(len(cadena)):
    invertir += cadena[-(i+1)]
print(invertir)
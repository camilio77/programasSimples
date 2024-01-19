#devolver la parte decimal de un numero decimal
dato = abs ( float ( input("ingrese un numero con decimales: \n")))
dec = dato - (int(dato))
print(f"la parte decimal de {dato} es {dec}")
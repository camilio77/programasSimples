#calcular la hipotenusa
cat1 = float(input("ingrese el largo del cateto opuesto: \n"))
cat2 = float(input("ingrese el largo del cateto abyasente: \n"))
H = ((cat1 ** 2) + (cat2 ** 2)) ** 0.5
print(f"la hipotenusa tiene una longitud de {H}")
#calcular la hora dentro de un numero especifico de horas
ho = float (input("ingrese la hora actual: \n"))
de = float (input("ingrese el numero de horas: \n"))
ht = (ho + de) % 24
if(ht > 12):
    m = "pm"
    ht = ht - 12
else:
    m = "am"
print(f"dentro de {round(de)} horas el reloj marcara las {round(ht,2)} {m}")
#calcular la hora dentro de un numero especifico de horas
ho = float (input("ingrese la hora actual: \n"))
des = float (input("ingrese el numero de horas: \n"))
ht = (ho + des)
if(ht > 12):
    m = "pm"
    ht = ht - 12
else:
    m = "am"
print(f"dentro de {round(des)} horas el reloj marcara las {round(ht,2)} {m}")
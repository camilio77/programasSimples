#calcular nota necesaria para pasar con nota de 60
c1 = float(input("ingrese la nota del primer certamen: \n"))
c2 = float(input("ingrese la nota del segundo certamen: \n"))
nl = float(input("ingrese la nota del laboratorio: \n"))

nc = (60 - nl * 0.3) / 0.7
c3 = 3 * nc - c1 - c2

print(f"necesita obtener {c3} en el tercer certamen para aprovar con 60")
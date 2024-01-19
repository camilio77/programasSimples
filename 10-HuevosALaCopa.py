#calcular lo que se demorara en estar listo un huevo en estar cocinado a la copa
import math
to = float ( input ("ingrese la temperatura original del huevo: \n"))
print("¿el huevo es grande o pequeño?")
M = int(input("1. huevo pequeño \n2. huevo grande \n"))
if M == 1:
    M = 47
elif M == 2:
    M = 67
t = (((M ** (2/3)) * ((3.7 * (1.038 ** (1/3))))) / ((0.0054 * (math.pi ** 2)) * (((4 * math.pi)/3) ** (2/3)))) * math.log((0.76) * ((to - 100)/(70 - 100)))
t = round(t)
print(f"el huevo se demorara {t} segundos en estar preparado a la copa")
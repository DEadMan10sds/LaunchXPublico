#División de piso -> doble diagonal, divide y redondea hacia abajo -> //
#Jerarquía -> Paréntesis -> Exponentes -> Multiplicación y división -> Suma y resta

from ast import parse


tierrra_distancia = 149597870
jupiter_distancia = 7778547200

distancia_planetas = abs(tierrra_distancia - jupiter_distancia)
distancia_planetas_millas = distancia_planetas * 0.621

print(distancia_planetas)
print(distancia_planetas_millas)

planeta1 = input("¿Cuál es la distancia del primer planeta?")
planeta2 = input("¿Cuál es la distancia del segundo planeta?")

planeta1 = int(planeta1)
planeta2 = int(planeta2)

distancia = abs(planeta1 - planeta2)
distancia_millas = distancia * 0.621

print("Distancia: " + str(distancia))
print("Distancia en millas: " + str(distancia_millas))
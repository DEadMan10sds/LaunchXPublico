##################################################
#Ejercicio 1
##################################################

text = """Interesting facts about the Moon. The Moon is Earth's only satellite. There are several interesting facts about the Moon and how it affects life here on Earth. 
On average, the Moon moves 4cm away from the Earth every year. This yearly drift is not significant enough to cause immediate effects on Earth. The highest daylight temperature of the Moon is 127 C."""

frase_separada = text.split('. ')

busqueda = {"average", "temperature", "distance"}

for frase in frase_separada:
    for clave in busqueda:
        if(clave in busqueda):
            print(frase)
            break

for frase in frase_separada:
    for clave in busqueda:
        if(clave in busqueda):
            print(frase.replace('C', 'Celcius'))
            break

##################################################
#Ejercicio 2
##################################################
name = "Moon"
gravity = 0.00162
planet = "Earth"

titulo = f'datos de gravedad sobre {name}'

#Plantilla Tierra
plantillla_hechos = f"""{'-'*80}
                    Planeta: {planet}
                    Gravedad en {name}: {gravity * 1000} m/s2"""

#Unir cadenas
cadena = f"""{titulo.title()} {plantillla_hechos}"""
print(plantillla_hechos)


#Plantilla marte
name = 'Marte'
gravity = 0.00143
planet = 'Ganímedes'

print(plantillla_hechos) ##Muestra los datos de la luna de nuevo

plantilla_Marte = f"""{'-'*80}
                    Planeta: {planet}
                    Gravedad en {name}: {gravity * 1000} m/s2"""

print(plantilla_Marte.format(nombre=name, planeta=planet, gravedad=gravity*1000))

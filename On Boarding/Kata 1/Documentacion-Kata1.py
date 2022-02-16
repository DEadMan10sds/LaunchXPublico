#program.py

from dis import dis
from traceback import print_tb


sum = 1+2
print(sum)

print('Hola mundo desde la consola')

#Mi turno
sun = 1 + 1 #3
product = sum * 2
print(product) #6

#Tipos de datos
#Numeros -> unt, float, complex
#texto -> str (string)
#booleano -> bool Python no requiere declaración de tipo de dato, es como Js

#Declaracion de variable 
distancia_a_alfa_centauri = 4.367

#Obtenemos su tipo de dato, en este caso será float
type(distancia_a_alfa_centauri)

#LOS OPERADORES FUNCIONAN IGUAL QUE EN OTROS LENGUAJES -> Nota: Funciona el === ??

#Importar de librería datetime el módulo date
from datetime import date

#Obtener fecha actual
date.today()

#Mostrar fecha en consola
print(date.today())


#Para mostrar la fecha junto a un texto hay que hacer un parse
print("Hoy es: " + str(date.today()))

#Pedir datos al usuario
print("Hola usuario, bienvenido al programa\n")
name = input("Cual es tu nombre: ")
print("Hola " + name + ", Tienes acceso al sistema")

resultado = 0
print("Calculadora")
operacion = input("Selecciona una operacion \n1.- Suma\n2.- Resta\n3.- Multiplicación\n4.- División\n->")
numero1 = input("Numero 1: ")
numero2 = input("Numero 2: ")

operacion = int(operacion)
numero1 = int(numero1)
numero2 = int(numero2)

if((operacion > 0) and (operacion < 5)):
    #Esto debería hacerse con un switch, pero no existe en python :(
    if(operacion == 1): resultado = numero1 + numero2
    else:
        if(operacion == 2): resultado = numero1 - numero2
        else:
            if(operacion == 3): resultado = numero1 * numero2
            else:
                if((operacion == 4) and (numero2 > 0)): resultado = numero1 / numero2
                else: print("No puedes dividir sobre 0")
print("Resultado: " + str(resultado))

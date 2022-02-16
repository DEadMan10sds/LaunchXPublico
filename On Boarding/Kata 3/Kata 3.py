velocidad_asteroide = 49

if(velocidad_asteroide > 25): print("Mira arriba! un asteroide!!!")
else: print("El asteroide no va a llegar a la tierra")


velocidad2_asteroide = 19
if(velocidad2_asteroide > 20): 
    print("Hay una luz brillante en el cielo!!!") #Cambiar por >= para eliminar un if
elif(velocidad2_asteroide == 20): 
    print("Una luz brillante en el cielo!!!")
else: 
    print("No pasa nada")

asteroide_dimensiones = 25
velocidad3_asteroide = 30

if(asteroide_dimensiones > 25 and velocidad3_asteroide > 25): print("Un asteroide se acerca a la tierra")
elif(asteroide_dimensiones > 25 and velocidad3_asteroide < 25): print("Va a pasar un asteroide")
elif(asteroide_dimensiones < 25 and velocidad3_asteroide > 25): print("Una luz brillante en el cielo!!!")
else: print("No pasa nada")
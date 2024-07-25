# agrega libreria 
from cgi import print_directory
import math

# solicitar datos a usuario

Peso = float(input("Ingrese su peso en kg:\n>"))
Altura = float(input("Ingrese su altura en cm:\n>"))

# convertir cm a metros

Altura1 = Altura / 100

# Calculo IMC

IMC = Peso / math.pow(Altura1, 2)

# Mostrar Resultado IMC 

print(f"Su IMC es {round(IMC,2)}")
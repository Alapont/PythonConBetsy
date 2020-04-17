import math
import random

def pitagoras (cateto1, cateto2):
    return math.sqrt(cateto1**2+cateto2**2)


# pi a cañonazos 
# π= 4(area circulo)/(area cuadrado)
cantidadDeBalas = 1000000
balasCuadrado = 0
balasCirculo = 0
for bala in range(cantidadDeBalas):
    x=random.uniform(-1,1)
    y=random.uniform(-1,1)
    balasCuadrado += 1
    if (pitagoras(x,y) <= 1):
        #dentro del circulo
        balasCirculo += 1
    # else:
        # fuera del circulo


# π= 4(area circulo)/(area cuadrado)
_pi=4*balasCirculo/balasCuadrado
_tau=8*balasCirculo/balasCuadrado

# print("π es igual a "+ str(_pi)+ " y te has ido por "+ str(abs(math.pi-_pi)))
print("𝜏 es igual a "+ str(_tau)+ " y te has ido por "+ str(abs(math.tau-_tau)))


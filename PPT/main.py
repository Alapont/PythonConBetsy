import random
from string import Template
import os

def piedraPapelTijera(jugador1,jugador2):
    solucionesJ1={
        "piedra":{
            "piedra":"empate",
            "papel":"pierde",
            "tijera":"gana"
        },
        "papel":{
            "piedra":"gana",
            "papel":"empate",
            "tijera":"pierde"
        },
        "tijeras":{
            "piedra":"pierde",
            "papel":"gana",
            "tijera":"empate"
        }
    }
    return solucionesJ1[jugador1][jugador2]


def preguntarJugador():
    print("Elige \"piedra\",\"papel\" o \"tijeras\"\n> ",end='')
    eleccion=input()
    return eleccion
    #aqui preguntaremos al jugador, pero ahora ha decididio que papel

def preguntarMaquina():
    eleccionMaquina=random.choice(["piedra","papel","tijera"])
    return eleccionMaquina

def jugar(): #bucle principal de jugar
    eleccionJugador=preguntarJugador()
    eleccionMaquina=preguntarMaquina()
    resultado=piedraPapelTijera(
        eleccionJugador,
        eleccionMaquina
    )
    salida=Template("Has elegido: $jugador, la maquina ha elegido: $maquina.\n El resultado es $resultado")
    print(
        salida.substitute(
            jugador=eleccionJugador,
            maquina=eleccionMaquina,
            resultado=resultado
        )
    )

salida = False
while not(salida):
    print("puedes \"jugar\" o \"salir\"\n> ",end='')
    lectura = input ()
    if (lectura=="salir"):
        print("Adeus")
        salida=True
    elif (lectura=="jugar"):
        jugar()        
    else:
        print ("no entiendo "+lectura)

#fin de while

"""
Read
Eval
Print
Loop
"""
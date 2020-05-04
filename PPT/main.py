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
    jugadas[eleccion] += 1
    return eleccion
    preguntarMaquinaRandom()

def preguntarMaquina():
    # usar el que tiene menos valores de jugadas
    if jugadas ["tijera"] > jugadas ["papel"] :
        # papel y piedra
        if jugadas ["papel"] > jugadas ["piedra"] :
            return "piedra" 
        else : 
            return "papel"
    else :
        # tijeras o  piedra
        if jugadas ["tijera"] > jugadas ["piedra"]:
            return "piedra"
        else:
            return "tijera"

def preguntarMaquinaRandom():
    eleccionMaquina=random.choice(["piedra","papel","tijera"])
    # el que tenga menos partidas de eleccionJugador
    return eleccionMaquina

def jugar(): #bucle principal de jugar
    eleccionJugador=preguntarJugador()
    eleccionMaquina=preguntarMaquina()
    resultado=piedraPapelTijera(
        eleccionJugador,
        eleccionMaquina
    )

    # if resultado == "gana":
    #     partidas["gana"] += 1
    # elif resultado == "empate":
    #     partidas["empate"] += 1
    # else: # "pierde"
    #     partidas["pierde"] += 1
    partidas[resultado] += 1

    salida=Template("Has elegido: $jugador, la maquina ha elegido: $maquina.\n El resultado es $resultado")
    print(
        salida.substitute(
            jugador=eleccionJugador,
            maquina=eleccionMaquina,
            resultado=resultado
        )
    )

jugadas={
    "piedra":0,
    "papel":0,
    "tijera":0
}
partidas={
    "gana":0,
    "empate":0,
    "pierde":0
}
contador=Template("G:$ganadas E:$empatadas P:$perdidas")
salida = False
while not(salida):
    print(
        contador.substitute(
            ganadas=partidas["gana"],
            empatadas=partidas["empate"],
            perdidas=partidas["pierde"]
        )
    )
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

import random

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
    return "papel"
    #aqui preguntaremos al jugador, pero ahora ha decididio que papel

def preguntarMaquina():
    eleccionMaquina=random.choice(["piedra","papel","tijera"])
    return eleccionMaquina

print(
    piedraPapelTijera(
        preguntarJugador(),
        preguntarMaquina()
    )
)
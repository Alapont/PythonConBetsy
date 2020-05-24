# Persona
import random
from string import Template


class Persona:
    # Constructor por parametros
    def __init__(self, nombre="Pontástico"):
        self.presentacion = Template(
            "Holi, me llamo: $nombre y tengo los calcetines de color $calcetines")
        self.nombre = nombre
        self.colorDeCalcetines = random.choice(["blanco", "magenta", "furcia"])

    def presentate(self):

        print(self.presentacion.substitute(
            nombre=self.nombre,
            calcetines=self.colorDeCalcetines
        ))
    # ToDo: emborracharse

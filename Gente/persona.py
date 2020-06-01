# Persona
import random
from string import Template

MAX_HIGADO=100

class Persona:
    # Constructor por parametros
    def __init__(self, nombre="Pontástico",idioma='es-es'):
        self.nombre = nombre
        self.presentacion = getPresentacion(idioma)
        self.colorDeCalcetines = random.choice(["blanco", "magenta", "furcia"])
        self.dinero=100
        self.higado=0

    def presentate(self):
        print(self.presentacion.substitute(
            nombre=self.nombre,
            calcetines=self.colorDeCalcetines
        ))
    
    def beber(self, bebida, coste):
        if( coste < self.dinero ):
            self.dinero = self.dinero - coste
            self.higado = self.higado + bebida
            if self.higado >= MAX_HIGADO:
                self.potar()
        else: #no bebo
            pass

    def potar(self):
        print(self.name+"🤮")

def getPresentacion(idioma):        
    if (idioma=="es-es"):
        return Template(
            "Holi, me llamo: $nombre y tengo los calcetines de color $calcetines"
        )
    elif (idioma=="de"):
        return Template(
            "Hallo, ich bin $nombre und ich hasse $calcetines Socken"
        )
    elif (idioma=="fr"):
        return Template(
            "Bonjour, Je m'apelle $nombre, et j'ai des chausettes $calcetines"
        )
    elif (idioma=="ru"):
        return Template(
            "Здравствуйте, меня зовут $nombre и у меня красные $color"
        )
    else: # valor por defecto
        return Template(
            "🤫"
        )

aux = Persona()
aux.beber(10,0)
print("fin de pruebas")
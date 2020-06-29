import persona
from discoteca import Discoteca
from string import Template
# Usamos personas

nombres = ["Pepe", "Juan", "Dieter", "Kinþaswinþs",
           "Бладимир Путин", "Obama", "TechnoViking", "Betsy"]
hain = Discoteca(nombre="Hain")
# otraDiscoteca=Discoteca()

for nombre in nombres:
    print(nombre)
    aux = persona.Persona(nombre,idioma='de')
    hain.añadirColaEntrar(aux)

for tic in range(0, 18):
    print(tic)
    hain.intentarPasar()


import persona
from string import Template
#Usamos personas

nombres = ["Pepe", "Juan", "Dieter", "Kinþaswinþs","Бладимир Путин","Obama", "TechnoViking","Betsy"]
lista = []
hain=[]

def escupir (persona):
    # print("heute leider nicht +persona.nombre)
    print("Que te jodan "+persona.nombre)

for nombre in nombres :
    print(nombre)
    aux=persona.Persona (nombre)
    if (nombre=="Betsy"):
        aux.presentacion=Template("hallo, ich bin $nombre und ich hasse $calcetines Socken")

    lista.append ( aux )

for p in lista :
    p.presentate()
    if (p.colorDeCalcetines != "blanco") :
        hain.append(p)
    else:
        escupir(p)

# En Hain solo hay gente sin calcetines blancos

pass
import persona
#Usamos personas

nombres = ["Pepe", "Juan", "Dieter", "Kinþaswinþs","Бладимир Путин","Obama", "TechnoViking","Betsy"]
lista = []
hain=[]

def escupir (persona):
    print("Que te jodan "+persona.nombre)

for nombre in nombres :
    print(nombre)
    lista.append ( persona.Persona (nombre) )


for p in lista :
    p.presentate()
    if (p.colorDeCalcetines != "blanco") :
        hain.append(p)
    else:
        escupir(p)

# En Hain solo hay gente sin calcetines blancos

pass
import persona
#Usamos personas

lista = []
nombres = ["Pepe", "Juan", "Dieter", "Kinþaswinþs"]

for nombre in nombres :
    print(nombre)
    lista.append ( persona.Persona (nombre) )

pass

for p in lista :
    p.presebtate()
    

pass
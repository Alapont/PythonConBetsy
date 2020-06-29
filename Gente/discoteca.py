# Discoteca unts unts

class Discoteca:
    # Constructor por parametros
    def __init__(self, nombre="club momentos",aforoMaximo=100):
        self.nombre = nombre
        self.aforoMaximo=aforoMaximo
        self.dinero=0
        self.colaEntrada=[]
        self.genteDentro=[]

    def añadirColaEntrar(self, persona):
        self.colaEntrada.append(persona)

    def intentarPasar (self):
        if ( len (self.genteDentro) < self.aforoMaximo):
            siguiente=self.colaEntrada.pop(0)
            if (siguiente.colorDeCalcetines != "blanco"):
                self.genteDentro.append(siguiente)
            else :
                # print("heute leider nicht +siguiente.nombre)
                print("Que te jodan "+siguiente.nombre)
        else:
            print("no hay mas hueco")


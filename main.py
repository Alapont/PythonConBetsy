#!/c/Users/pablo/AppData/Local/Programs/Python/Python38/python
import math

print("Hola Pablo")

# función para ver funciones
# nombre: persona a la que saludo
# años: años de la persona que saludo
def my_function(nombre, años):
    print("Holiii " + nombre +", tienes " )
    print( años )
    print( "años 💩")
    
# El cuadrado de una hipotenusa de un triangulo rectángulo es igual a la suma de los dos catetos al cuadrado
# h=√(c²+c²)
def pitagoras(cateto1, cateto2):

    return math.sqrt(cateto1*cateto1+cateto2**2)

my_function("Quevedo", pitagoras (3, 4) )

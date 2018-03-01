# Funcion ln(x+2) - sin(x) = 0

import numpy
from matplotlib import pyplot
def func( x ):
    return numpy.log(x+2) - numpy.sin(x)

 
# Derivada 
# 1/(x+2) - cos(x)
def derivFunc( x ):
    return (1/(x+2)) - numpy.cos(x)

 
# Metodo de Newton
def newtonRaphson( x ):
    lista1 = []

    h = func(x) / derivFunc(x)
    while abs(h) >= 1E-5:

        h = func(x)/derivFunc(x)
        lista1.append(abs(h))

        # x(i+1) = x(i) - f(x) / f'(x)
        x = x - h
        print("x ->", x)



        
    print("El valor x donde se intersectan es : ",
                             "%.11f"% x)

#se utiliza x0=-1.5 en vez de x0=1 como lo dice el enunciado
#esto porque 1 no es una valor valido para el metodo, 
#pues no se encuentra dentro del intervalo de la interseccion
#un intervalo valido sería [-1.7,-1.4]
 
x0 = -1.5
newtonRaphson(x0)

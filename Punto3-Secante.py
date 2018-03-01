import numpy
import sys
def secant(f, x0, x1, e):
    f_x0 = f(x0)
    f_x1 = f(x1)
    iteration_counter = 0
    while abs(f_x1) > e and iteration_counter < 1000:
        try:
            denominator = float(f_x1 - f_x0)/(x1 - x0)
            x = x1 - float(f_x1)/denominator
        except ZeroDivisionError:
            print ("division por 0")
            sys.exit(1)     
        x0 = x1
        x1 = x
        f_x0 = f_x1
        f_x1 = f(x1)
        iteration_counter += 1
        
    if abs(f_x1) > e:
        iteration_counter = -1
    return x, iteration_counter

def f(x):
  #f(x) = ln(x+2) - sin(x)
    return (numpy.log(x + 2)-numpy.sin(x))

#intervalo [-1.7,-1.4]
x0 = -1.7;   x1 = -1.4

solution, no_iterations = secant(f, x0, x1, e=1.0e-7)

if no_iterations > 0:    # Solution found
    print ("Numero de iteraciones: %d" % (2 + no_iterations))
    print ("El valor de x donde se intersectan es:  %f" % (solution))
else:
    print ("No se encontró solución!")
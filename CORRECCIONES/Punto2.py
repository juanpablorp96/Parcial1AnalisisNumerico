import math

def f(x):
	return math.exp(x)

def g(x):
	if(f(x) != 0):
		return (f(x+f(x))-f(x))/f(x)
	return 0

def aitken():
	x=1 #punto inicial
	it=0 #iteraciones
	while(abs(f(x))>=1E-6 and it<1000000):
		if(g(x)!=0):
			x=x-(f(x)/g(x))
			it=it+1
		if(g(x)==0):
			it=1000000
			return "cambiar punto de inicio"
	if(abs(f(x))<1E-8):
		print("La función no convergente en:" + str(x))
	else:
		print("La sucesión no es convergente")


aitken()
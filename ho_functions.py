### HO Function ###
def suma_uno(valor):
    return valor+1

def cuadrado(valor):
    return valor*valor

def multiplicacion(valor1,valor2,f): #f la voy a usar para llamar a una funcion.
    return f(valor1*valor2)

print(multiplicacion(3,3,suma_uno)) #Quiero que me sume uno
print(multiplicacion(3,3,cuadrado)) #Quiero que me de el cuadrado

#### Closures ####

def sumar_diez():
    def add(value):
        return value +10
    return add
add_closure = sumar_diez()
print(add_closure(10))

##### HO Built in ######

#Map
lista = [1,2,3,4,5,6,7,8]
lista_dos = list(map(cuadrado,lista )) #Muy buena f
print(lista_dos)
lista_tres = list(map(lambda numero:numero+1,lista )) # Es decir recorre y modifica los  valores(No la principal)
print(lista)

#Filter
def par(numero):
    if numero % 2 == 0:
        return True
    

filtrado_par= list(filter(par,lista_dos)) # O sea me retorna lo filtrado
filtrado_impar = list(filter(lambda numero:numero%2,lista_dos)) #Lo interesante de esto es que 0 = true y 1 = false, por eso devuelve solo impares
print(filtrado_par)
print(filtrado_impar)

#Reduce
from functools import reduce

print(reduce(lambda numero1,numero2:numero1+numero2,lista)) #Necesita que la funcion tenga 2 variables,ejecuta y el valor retornado sera el siguiente numero1.
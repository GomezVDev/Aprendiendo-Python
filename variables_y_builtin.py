# En este archivo voy a poner lo más interesante, tengo conocimiento de 1er año, unicamente estoy practicando la syntaxis de python

# Se puede variables en una sola linea
nombre,edad,apodo = "Valentin", 'veinticuatro',"Chiche"

#Asi como 
informacion_primo ={
    'nombre.primo' : 'Hernan' , #Notese que de esta manera hay que usar : y ademas una ,
    'edad.primo' : 'Veinticinco' ,
    'apodo.primo' : 'Diestrax'  # Ya al final no utilizo ,
    }

print(nombre,edad,apodo,'\n')
print(informacion_primo)
print('nombre.primo') # Va a imprimir literalmente nombre.primo
#print(informacion_primo[0]) De la manera que esta declarada lsa variable, no se encuentra indexado

#input
nombre_input = input("Ingrese su nombre :")
edad_input = input("Ingrese su edad: ")
print(nombre_input)
print(edad_input)

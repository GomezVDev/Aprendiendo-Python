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


#Print en una sola linea con format (f) es como en c.
print(f'El tipo de dato de edad_input es : {type(edad_input)} , y si lo inteo seria {type(int(edad_input))} y como lo estoy haciendo en la misma linea el dato finalmente queda como {type(edad_input)}' ) # O sea no cambia si no lo guardo.
print(f"El nombre ingresado es : {nombre_input} y la edad ingresada : {edad_input} años.")

""""
Bueno aca termino con esta parte, las demas funciones builtin las voy a ir viendo cuando las necesite, con eso ya vi suficiente de variables, es muy sencillo al ser tan dinamico

"""
mi_lista = ["Valentin","Gomez",24,"Chiche"] 
segunda_lista = ["Hernan","Martinez",25,"Diestrax"]
print(len(mi_lista))
print(mi_lista.count("Valentin")) #Voy a buscar si aparence mi nombre
print(mi_lista.count("gomez")) #Voy a buscar si aparence mi apellido con g minuscula
print(mi_lista.count(str)) #Voy a buscar cuantos str hay, NO funciona.
print(mi_lista+segunda_lista) 
tercer_lista = ["Hola mundo"]
print(tercer_lista[0])
# print(tercer_lista[1]) Out of range.
mi_lista.append("Argentina") #Agrega al final de la lista
mi_lista.insert(5,"River Plate") #Agrega en el indice que le indico
#print(mi_lista)
mi_lista.insert(5,"Pilar") #Lo cambia? NO!inserta y mueve lo que estaba en su lugar para la derecha
print(mi_lista)
mi_lista.remove("Pilar") #Elimina la primer coincidencia y tiene que ser igual
print(mi_lista)
mi_lista.reverse() #Reversa literalmente
print(mi_lista)
print(mi_lista.reverse()) #None, pero de todas maneras SI REVERSA.
print(mi_lista)
print(mi_lista.pop()) #Elimina el que le indico y me lo retorna, vacio es el ultimo y vuelvo a repetir, si invoco a la funcion afecta DIRECTAMENTE a la lista
print(mi_lista)
del mi_lista[3] #Simplmente lo elimina
print(mi_lista)
lista_reslpado = mi_lista.copy()
mi_lista.clear() #Limpia la lista
print(mi_lista)
print(lista_reslpado) #Deberia haberse guardado...SI

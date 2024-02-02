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
mi_lista.insert(5,"Buenos Aires") #Lo cambia? NO!inserta y mueve lo que estaba en su lugar para la derecha
print(mi_lista)
mi_lista.remove("Buenos Aires") #Elimina la primer coincidencia y tiene que ser igual
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
primera_tupla = ("Valentin","Gomez",24) #Tripla
#primera_tupla[2] = 25 NO! Es inmutable.
segunda_tupla = ("Argentina","River Plate")
tercer_tupla = primera_tupla+segunda_tupla
print(tercer_tupla) 
tercer_tupla = list(tercer_tupla) #La reasigno como lista.
print(type(tercer_tupla))
tercer_tupla.insert(5,"Buenos Aires")
print(tercer_tupla)
tercer_tupla = tuple(tercer_tupla)#Reasigno nuevamente.
primer_dict = {
    "Nombre":"Valentin",
    "Apellido":"Gomez",
    "Edad":25,
    "Lenguajes":{"Python","C"}
    }
#print(primer_dict)
print(primer_dict.get("Lenguajes","Nombre"))#No crashea pero el nombre no lo imprime
print(primer_dict.get("Nombre")) 
print(primer_dict["Nombre"])
primer_dict["Nombre"] = "Blas"
print(primer_dict["Nombre"])
#nombre,apellido = primer_dict.get("Nombre","Apellido") too many values to unpack (expected 2)
nombre = primer_dict.get("Nombre")
apellido = primer_dict.get("Apellido")
print(f"El nombre geteado es {nombre} y el {apellido}")
primer_dict["Club"] = "River Plate" #Agrega al final
print(primer_dict)
segundo_dict = dict.fromkeys(primer_dict)
print(segundo_dict) #Me sirve para crear otro "vacio" en base al que ya tengo (Hay más pero esta es una buena utilidad)
lista_rango = [i for i in range(0,11)]
print(lista_rango)
lista_rango2 = [i+2 for i in range(0,11)]
print(lista_rango2)
lista_rango2 = [i*2 for i in range(0,11)]
print(lista_rango2)
lista_rango2 = [i*i for i in range(0,11)]
print(lista_rango2)
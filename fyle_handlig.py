### Manejo de ficheros ###

#.txt file
import os
# txt_file =open("./my_file.txt", "w") #Overwrites con w+ tambien
txt_file =open("./my_file.txt", "r+") #No Ow.Y r&w 
#print(txt_file.read())
#txt_file.write("\nArgentina") #Escribe al final o sea = River PlateArgentina
                              #Le agrego \n para ver si escribe abajo = Si! Lo comento para que no siga agregando.
lista_leida = txt_file.readlines()#Lee la linea, siguiente ya que arriba leí.
#print(txt_file.readline(1))#No lee nada, o sea espacio en blanco, ya que arriba leí, no puedo especificar
#print(txt_file.readlines())#Me lee todo y crea un array
#print(txt_file.readlines())#Array vacio
array_agregado = ["Messi\n","9/12/18\n"]
#txt_file.write(array_agregado) write() argument must be str, not list
# for line in txt_file.readlines(): # O sea voy iterando el array que se forma.
#     print(line)
print(lista_leida)
lista_limpia = [elemento.strip() for elemento in lista_leida] #El strip limpia lo indeseado al principio y final(espacios y \n etc)
lista_a_texto = ','.join(lista_limpia)
print(lista_a_texto)

txt_file.close()

#os.remove("./my_file.txt") Lo borra

# .json file

import json

json_file = open("./json_file.json","w+")

json_test ={
        "Nombre":"Valentin",
        "Edad" : 25,
        "Apellido" : ["Gomez","Acevedo"],
        "Website": "https://github.com/GomezVDev"
    }

json.dump(json_test,json_file,indent=0) #Con dump, escribo el fichero.
json_file.close()
# open("./json_file.json","r") Una vez cerrado no puedo volver a abrilo asi
# print(json_file.readlines())

# Vuelve a abrir el archivo en modo de lectura
with open("./json_file.json", "r") as json_file:
    # Lee y muestra las líneas del archivo
    contenido = json_file.readlines()
    print(contenido)

json_dict = json.load(open("./json_file.json")) #Lo parseo de JSON --> DICT, mucha utilidad.
print(json_dict)
print(json_dict["Apellido"][0]) #Gomez

#Csv

import csv # Esto puede ser un excel

nuevo_csv = open("./csv_file.csv","w+")
csv_writer = csv.writer(nuevo_csv)
csv_writer.writerow(["Nombre","Apellido","Edad"])
csv_writer.writerow(["Valentin","Gomez",24])

nuevo_csv.close()

with open("./csv_file.csv","r+") as csv_file:
    for line in csv_file.readlines():
        print(line)



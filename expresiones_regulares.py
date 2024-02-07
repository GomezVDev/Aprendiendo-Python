###Expresiones regulares###
import re #Funcionalidad para EP
##match##
cadena = "Esta es la cadena"
cadena_2 = "Mi nombre es Valentin y mi apellido es Gomez"

print(re.match("Esta es",cadena_2))
print(re.match("cadena",cadena_2))#None ya que match, es desde el principio

span = re.match("Esta es",cadena) # Guardo los datos del match
inicio,final = span.span() #Guardo el rango SPAN, que es una DUPLA.
print(cadena[:final]) #Segun yo esto deberia funcionar.ACTUALLY YES.
print(cadena[:span.end()]) #Variacion mas sencilla. 

##search##

#Es lo mismo que match, en el sentido de lo que retorna, pero no necesariamente tiene que ser desde el principio.

datos_search = re.search("Valentin",cadena_2,re.I)#Solo la primer ocurrencia.
print(cadena_2[datos_search.start():datos_search.end()])#Imprime Valentin!

##findall##

datos_findall = re.findall("Es",cadena_2,re.I) #No CS(por el re.I) y LAS ocurrencias.
print(datos_findall)
print(len(datos_findall))


##split##

datos_split = re.split(" ",cadena) #Crea un lista a partir del separador que le inidco.
print(datos_split)
print(type(datos_split))

##sub##

cadena_3 = "Esta És la cadena en uso"
datos_sub= re.sub("[E|É]s","es",cadena_3,)# el | me permite +1 opción e icluso seguir.
print(datos_sub) #Modifica todas las coincidencias
print(type(datos_sub))


######### Patterns ##########
pattern = r'[Nn]ombre|Valentin'
print(re.findall(pattern,cadena_2))

#Reviar regex101.com

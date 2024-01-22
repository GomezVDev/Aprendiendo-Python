cadena_de_prueba = "Hola como estas"
cadena_numerica = 12345
cadena_numerica_str = "12345"
print(cadena_de_prueba.isalpha())
print(cadena_numerica_str.isalpha())
print("La cadena %s es numerica? Respuesta :%s " %(cadena_numerica_str,str(cadena_numerica_str.isnumeric())))
#La linea de arriba, si bien funciona, no es recomendada, ahora se recomienda el uso de format


#print(cadena_numerica.isnumeric()) No puedo aplicar estos comandos a un int
print(str(cadena_numerica).isnumeric()) # Si o si tengo que hacerlo str para usar estas funciones
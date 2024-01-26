########## FUNCIONES Y EXCEPT ###############

def prueba(var_1,var_2):
    try:
        resultado = var_1 + var_2
        print(f'El resultado es : {resultado}')
    except TypeError as Error:
        print(f"Has intentado {Error}")
        print(f"Igualmente lo resuelvo y el resultado es : {int(var_1)+int(var_2)} ")
        eleccion = input("Quiere agregar otro numero ? :")
        if eleccion == "Si" or eleccion== "si":
            numero1 = int(input("Agregue el primer numero :"))
            numero2 = int(input("Ingrese el segundo numero: "))
            prueba(numero1,numero2) #Esto genera que cada vez que la vuelvo a llamar me imprima "Gracias.."
    #Si no hay error va a entrar al else        
    else:
         eleccion = input("Quiere agregar otro numero ? :")
         if eleccion == "Si" or eleccion== "si":
            numero1 = int(input("Agregue el primer numero :"))
            numero2 = int(input("Ingrese el segundo numero: "))
            prueba(numero1,numero2) 
    #Si pone que no en ambos condicionales, el programa finaliza con un saludo
    #finally:
    #   print("Gracias por usar nuestra App")
    #probando cambios 

################
var_1 = input("Ingrese primer numero: ")
var_2 = int(input("Ingrese el segundo numero: "))
prueba(var_1,var_2)
print("Gracias por usar nuestra App")
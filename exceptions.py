var_1 = input("Ingrese primer numero: ")
var_2 = input("Ingrese el segundo numero: ")

def prueba(var_1,var_2):
    try:
        resultado = var_1 + var_2
        print(f'El resultado es : {resultado}')
    except TypeError as Error:
        print(f"Has intentado {Error}")
        print(f"Igualmente lo resuelvo y el resultado es : {int(var_1)+int(var_2)} ")
        
    finally:
        print("Gracias por usar nuestra App")

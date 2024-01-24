class Persona:
    def __init__(self,nombre,apellido):
        #Metodo de instancia
        self.nombre = nombre       #Publicas
        self.__apellido = apellido #Privada
    
    def saludar(self):
        print(f"Hola mi nombre es {self.nombre} y mi apellido es {self.apellido}")
    
    def despedirse(self):
        print(f"Hasta luego!")
    
    #Metodo estatico
    @staticmethod
    def saludar_random(nombre_random):
        #Va a saludar a un nombre random.
        print(f"Hola {nombre_random} como estas?")


persona_1 = Persona("Valentin","Gomez")
persona_2 = Persona("Hernan","Martinez")
print(f"{persona_1.nombre} va caminando por la calle y se encuentra con {persona_2.nombre} entonces se presentan \n")
persona_1.saludar() # Quiero que se presente Valentin
persona_2.saludar()
print(f"Luego aparece alguien llamado Ian y entonces {persona_1.nombre} saluda.")
Persona.saludar_random("Ian")

#Dato adicional.
persona_1.nombre = "Blas" #Pueden cambiar sus variables.
print(persona_1.nombre)




    

        
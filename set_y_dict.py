primer_set = {} #Se inicializa como DICCIONARIO
print(type(primer_set))

primer_set = {"Valentin","Gomez",24}
print(type(primer_set))
print(len(primer_set))
#print(primer_set[0]) 'set' object is not subscriptable
primer_set.add("River plate")
print(primer_set) #No es ordenada
primer_set.add("River plate")
print(primer_set) #No admite repetidos
print("Valentin" in primer_set)
primer_set.remove("Valentin")
print(primer_set)
print("Valentin" in primer_set)
print(primer_set)
primer_set.add("Valentin")
segundo_set = {"Buenos Aires","Mate"}
tercer_set = primer_set.union(segundo_set) 
print(tercer_set.union({2025}))
print(tercer_set)#A diferencia de las listas, si la modifico en un print, no afecta al objeto en si, solamente en la ejecucion.
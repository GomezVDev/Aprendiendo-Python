sum_dos_valores = lambda primer_valor,segundo_valor:primer_valor+segundo_valor #Anonima, en una linea.

suma_uno= sum_dos_valores(1,2)
print(suma_uno)
suma_dos = sum_dos_valores(sum_dos_valores(1,2),sum_dos_valores(1,2))
print(suma_dos)


nombre_alumno = input("Decime tu Nombre y Apellido: ")
nota_1 = int(input("¿Cuál fue tu primera nota? "))
nota_2 = int(input("¿Y la segunda? "))
nota_3 = int(input("por último, decime tu tercer nota: "))
promedio = (nota_1 + nota_2 + nota_3) / 3
print("Entonces, " + nombre_alumno + ", tu promedio es: " + str(promedio))
# Salida en Consola: Decime tu Nombre y Apellido: Natalia Rodicio
# ¿Cuál fue tu primera nota? 8
# ¿Y la segunda? 9
# por último, decime tu tercer nota: 8
# Entonces, Natalia Rodicio, tu promedio es: 8.333333333333334
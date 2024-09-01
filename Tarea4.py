# Definir calificaciones

calif_1 = 10
calif_2 = 7
calif_3 = 4

print(calif_1, calif_2, calif_3)

#Definir los pesos correspondientes a cada calificacion

peso_1 = 0.15
peso_2 = 0.35
peso_3 = 0.50

print(peso_1, peso_2, peso_3)

#Calculamos el promedio ponderado

promedio_ponderado = (calif_1 * peso_1) + (calif_2 * peso_2) + (calif_3 * peso_3)
print("El promedio ponderado de las calificaciones es:", promedio_ponderado)

#Denir matriz original
matriz = [[1, 1, 1, 3], [2, 2, 2, 7], [3, 3, 3, 9], [4, 4, 4, 13]]
print(matriz)

# Recorremos cada fila de la matriz

for fila in matriz:
    # Calculamos la suma de los primeros tres valores
    suma = sum(fila[:3])
    # Actualizamos el cuarto valor para que sea igual a la suma
    fila[3] = suma

print("Matriz corregida:")
for fila in matriz:
    print(fila)


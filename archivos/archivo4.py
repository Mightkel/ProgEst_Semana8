#Crea un programa que permita guardar n cantidad de notas en un archivo, leer las notas, calcular el promedio, la nota mas alta y la nota mas baja.
notas = []
n = int(input("Ingrese la cantidad de notas a ingresar: "))
print("==================")
for i in range(n):
    nota = float(input(f"Ingrese la nota #{i+1}: "))
    notas.append(nota)
    
promedio = sum(notas) / len(notas)

alta  = 0
for i in notas:
    if i > alta:
        alta = i

baja = 100

for i in notas:
    if i < baja:
        baja = i
        
print("=== Resultados ===")
print(f"Notas ingresadas: {notas}")
print(f"Promedio de notas: {promedio}")
print(f"Nota más alta: {alta}")
print(f"Nota más baja: {baja}")

datos = f"Notas: {notas}\nPromedio: {promedio:.2f}\nNota más alta: {alta}\nNota más baja: {baja}\n\n"

with open("notas.txt", "a", encoding="utf-8") as archivo:
    archivo.write(datos)
    
print("==================")
print("Datos guardados.")
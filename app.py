#Cree una aplicacion que lea los datos de un estudiante: nombres, apellidos, nota. 
# Calcular el promedio de las notas, la nota mas alta y la nota mas baja.
# Mostrar los 3 con mayor nota
while True:
    try:
        estudiantes = int(input("Ingrese la cantidad de estudiantes a registrar: "))
        if estudiantes <= 0:
            raise ValueError("Debe registrar al menos un estudiante.")
        break
    except ValueError as e:
        print(f"Error: {e}")
mejores = []
notas = []

for i in range(estudiantes):
    nombres = input("Ingrese sus nombres y apellidos: ")

    while True:
        try:
            nota = float(input("Ingrese la nota: "))
            if nota < 0 or nota > 100:
                raise ValueError("La nota debe estar entre 0 y 100.")
            break
        except ValueError:
            print(f"Error: {ValueError}")
    print("==================")
    notas.append(nota)
        
    mejores.append({"Estudiante": nombres, "Nota": nota})
    mejores.sort(reverse=True, key=lambda mejor: mejor["Nota"])
    del mejores[3:]

    datos = f"Nombres: {nombres.title()}\nNota: {nota}\n\n"

    with open("notas.txt", "a", encoding="utf-8") as archivo:
        archivo.write(datos)
alta = max(notas)
baja = min(notas)
promedio = sum(notas) / len(notas)
with open("notas.txt", "a", encoding="utf-8") as archivo:
    archivo.write(f"=== Mejores 3 Estudiantes ===\n")
    for estudiante in mejores:
        archivo.write(f"Estudiante: {estudiante['Estudiante']} | Nota: {estudiante['Nota']}\n")
    archivo.write(f"\nPromedio: {promedio:.2f}\nNota más alta: {alta}\nNota más baja: {baja}\n\n==================\n")
        
print("=== Resultados ===")
print(f"Notas ingresadas: {len(notas)}")
print(f"Promedio de notas: {promedio:.2f}")
print(f"Nota más alta: {alta}")
print(f"Nota más baja: {baja}")
print("=== Mejores 3 Estudiantes ===")
for estudiante in mejores:
    print(f"Estudiante: {estudiante['Estudiante']} | Nota: {estudiante['Nota']}\n")

print("==================")
print("Datos guardados.")
    
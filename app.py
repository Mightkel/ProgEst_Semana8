#Cree una aplicacion que lea los datos de un estudiante: nombres, apellidos, nota. 
# Calcular el promedio de las notas, la nota mas alta y la nota mas baja.
# Mostrar los 3 con mayor nota
estudiantes = int(input("Ingrese la cantidad de estudiantes a registrar: "))
mejores = []
for i in estudiantes:
    nombres = input("Ingrese sus nombres: ")
    apellidos = input("Ingrese sus apellidos: ")
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

    datos = f"Nombres: {nombres.title()}\nApellidos: {apellidos.title()}\nNotas: {notas}\nPromedio: {promedio:.2f}\nNota más alta: {alta}\nNota más baja: {baja}\n\n"

    with open("notas.txt", "a", encoding="utf-8") as archivo:
        archivo.write(datos)
    
    mejores.append(f"Estudiante: {nombres.title()}{apellidos.title()} Nota: {alta}")
    
    
    print("==================")
    print("Datos guardados.")
    
#Multiplicacion de matrices cuadradas

matrizA = []
matrizB = []
matrizC = []
print("=== Matriz 1 ===")
for i in range(2):
    matrizA.append([])
    for j in range(2):
        x = int(input(f"Digite el valor #{i},{j}: "))
        matrizA[i].append(x)
        
for i in matrizA:
    print(i)

print("=== Matriz 2 ===")
for i in range(2):
    matrizB.append([])
    for j in range(2):
        x = int(input(f"Digite el valor #{i},{j}: "))
        matrizB[i].append(x)
    
for i in matrizB:
    print(i)
    
print("=== Multiplicacion de matrices ===")

for i in range(len(matrizA)):
    matrizC.append([])
    for j in range(len(matrizA)):
        matrizC[i].append(matrizA[i][j] * matrizB[j][i])
        
for i in matrizC:
    print(i)
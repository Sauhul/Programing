filas = int(input("¿Cuántas FILAS quieres? "))
columnas = int(input("¿Cuántas COLUMNAS quieres? "))
matriz = []

print(f"Creando matriz {filas}x{columnas}")

for i in range(filas):
    fila = []                    
    for j in range(columnas):
        valor = int(input(f"Fila{i} Col{j}: "))  
        fila.append(valor)       
    matriz.append(fila)          

print("Tu matriz:")
for fila in matriz:              
    print(fila)
inventario = []

def agregar_producto(inventario):
    try:
        producto = input("Ingrese el nombre del producto: ")
        precio = float(input("Ingrese el precio del producto: "))
        inventario.append({"nombre": producto, "precio": precio})
        print("Lista actual:", inventario)  
    except :
        print("Ingrese un numero valido")

def mostrar_inventario(inventario):
    for producto in inventario:
        
        nuevo_producto = {"nombre" : producto,}

        
        
        
        print(f"Nombre:{producto["nombre"]}, Precio:{producto["precio"]}")


def calcular_estadisticas(inventario):
    
    valor_total = 0
    total_productos = 0

    for producto in inventario:
        valor_total += producto["precio"]
        total_productos += 1
    
    promedio = valor_total / total_productos

    if total_productos <= 0:
        print("No hay productos")
    else:
        print("Buscando productos...")    


    print(f"Total de productos es: {total_productos}")
    print(f"Valor total: {valor_total}")
    print(f"El precio promedio es: {promedio}")    
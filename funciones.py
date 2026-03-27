inventario = [{"nombre": "Manzana", "precio": 1.0}, {"nombre": "Pera", "precio": 2.0}, {"nombre": "Mango", "precio": 3.0}]

def agregar_producto(inventario):
    producto = input("Ingrese el nombre del producto: ")
    precio = float(input("Ingrese el precio del producto: "))
    inventario.append({"nombre": producto, "precio": precio})
    print("Lista actual:", inventario)  

def mostrar_inventario(inventario):
    for i in inventario:
        print(i)
          
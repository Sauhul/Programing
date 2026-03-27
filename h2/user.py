from funciones import*
opcion = ""


while opcion != "4":
    print("Menu")
    print("1. Agregar producto")
    print("2. Mostrar inventario") 
    print("3. Calcular estadisticas")
    print("4. Salir")

    opcion = input("Ingrese una opcion: ")

    if opcion == "1":
        agregar_producto(inventario)
    elif opcion == "2":
        mostrar_inventario(inventario)
    elif opcion == "3":
         calcular_estadisticas(inventario)    

              
            
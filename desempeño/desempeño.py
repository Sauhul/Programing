from funciones import*
opcion = ""

while opcion != "6":
    
    
        print("--------Students---------")
        print("1. New student")
        print("2. Show Students")
        print("3. Search student")
        print("4. Update the student")
        print("5. Remove Student")
        print("6. Exit")

        opcion = input("Search your student:  ")
        
        
        if opcion == "1":
            agregar_estudiante(estudiantes)
            
        elif opcion == "2":
            mostrar_estudiante(estudiantes)   
            
        elif opcion == "3":
            buscar_estudiante()    
        
        elif opcion == "4":
            actualizar_estudiante(estudiantes)
            
        elif opcion == "5":
            eliminar_estudiante(estudiantes)
        
        elif opcion == "6":
            print("Saliendo del programa")
        else:
            print("Elija una opcion valida")    
            
                 
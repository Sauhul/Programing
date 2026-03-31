estudiantes = [] 

def agregar_estudiante(inventario):

    
        try:
            id = int(input("Ingrese el id: "))
            nombre = str(input("Ingrese el nombre : "))
            edad = int(input("Ingrese la edad: "))
            curso = str(input("Ingrese el curso: "))
            estado = str(input("Ingrese el estado: "))
            inventario.append({"id": id,"nombre": nombre, "edad": edad, "curso" : curso, "estado" : estado})
        except :
            print("Ingrese un numero valido")

def mostrar_estudiante(estudiantes):
    for i in estudiantes:
        print(f"ID: {i['id']}, Name: {i['nombre']}, Age: {i['edad']}, Grade: {i['curso']}, State: {i['estado']}")

    if estudiantes == []:
        print("El inventario esta vacio, agregue productos.")  
        
def buscar_estudiante():
    
    nombre_estudiante = input("introduzca el nombre de su estudiante:  ")
    
    encontrado = None
    
    for i in estudiantes:
        if i["nombre"] == nombre_estudiante:
            encontrado = i
            break
    
    if encontrado:
        print(f"Resultado: {encontrado['nombre']}")
    else:
        print("No se encontro ningun estudiante con ese Nombre")    
        return None
        
def actualizar_estudiante(estudiantes):
    
    estudiante = buscar_estudiante(estudiantes)
    
    
    if estudiante is not None:
        
        cambio = input("Ingrese el nuevo nombre: ")
        
        
        estudiante["nombre"] = cambio
        print("¡Nombre actualizado!")
    else:
        
        print("No se puede actualizar un estudiante que no existe.")

def eliminar_estudiante(estudiantes):
   
    estudiante_a_borrar = buscar_estudiante(estudiantes)
    
   
    if estudiante_a_borrar is not None:
        
        estudiantes.remove(estudiante_a_borrar)
        print(f"¡El estudiante {estudiante_a_borrar['nombre']} ha sido eliminado!")
    else:
        print("Operación cancelada: El estudiante no existe.")        
        
        
        
        
        
        

    
        
    
    
    
    
        
    
    
    
              
        
    


print("╔══════════════════════════════════════╗")
print("║     CALCULADORA  GEOMÉTRICA          ║")
print("║     Figuras 2D y 3D                  ║")
print("╚══════════════════════════════════════╝")

input("Presiona Enter para continuar...")




tipo = 0
 

 
while tipo != 10:
  
    print("1. Figuras 2D")
    print("2. Figuras 3D")
    print("10. Salir")

    tipo = -1
    while tipo == -1:

        
        try:
            tipo = int(input("Escoja su tipo de figura: "))
            if tipo != 1 and tipo != 2 and tipo != 10:
                print("Opción no válida. Por favor, elija 1, 2 o 10.")
                tipo = -1
        except:
            print("Por favor, introduce un número válido.")
            tipo = -1
            
        if tipo == 10:
            print("Gracias por usar la calculadora. ¡Hasta luego!")
            exit()

        
        if tipo == 1:
            print("1. Cuadrado")
            print("2. Rectángulo")
            print("3. Triángulo rectángulo")
            print("4. Círculo")
            print("5. Trapecio")
            print("0. Volver al menú principal")

            try:
                figura = int(input("Escoja su figura: "))
            except:
                print("Por favor, introduce un número válido.")
                exit()

            if figura == 0:
                continue    

            if figura == 1:
                lado = float(input("Introduce el lado del cuadrado: "))
                area = lado ** 2
                perimetro = 4 * lado
                print(f"Área: {area}")
                print(f"Perímetro: {perimetro}")

            elif figura == 2:
                base = float(input("Introduce la base: "))
                altura = float(input("Introduce la altura: "))
                area = base * altura
                perimetro = 2 * (base + altura)
                print(f"Área: {area}")
                print(f"Perímetro: {perimetro}")

            elif figura == 3:
                base    = float(input("Introduce el cateto base: "))
                altura  = float(input("Introduce el cateto altura: "))
                angulo_a = float(input("Introduce el ángulo A (distinto de 90°): "))

                hipotenusa = (base ** 2 + altura ** 2) ** 0.5
                angulo_b   = 90 - angulo_a  
                angulo_c   = 90              

                print(f"Hipotenusa : {hipotenusa:.2f}")
                print(f"Ángulo A   : {angulo_a}°")
                print(f"Ángulo B   : {angulo_b}°")
                print(f"Ángulo C   : {angulo_c}°  (recto)")
                print(f"Suma total : {angulo_a + angulo_b + angulo_c}°")

            
            elif figura == 4:
                radio = float(input("Introduce el radio: "))
                area = 3.1416 * radio ** 2
                perimetro = 2 * 3.1416 * radio
                print(f"Área: {area}")
                print(f"Perímetro: {perimetro}")

            elif figura == 5:
                base_mayor = float(input("Introduce la base mayor: "))
                base_menor = float(input("Introduce la base menor: "))
                altura = float(input("Introduce la altura: "))
                area = ((base_mayor + base_menor) / 2) * altura
                perimetro = float(input("Introduce el perímetro: "))
                print(f"Área: {area}")
                print(f"Perímetro: {perimetro}")

        
        elif tipo == 2:
            print("1. Esfera")
            print("2. Cubo")
            print("3. Cilindro")
            print("4. Cono")
            print("0. Volver al menú principal")

            try:
                figura = int(input("Escoja su figura: "))
            except:
                print("Por favor, introduce un número válido.")
                exit()

            if figura == 0:
                continue

            if figura == 1:
                radio = float(input("Introduce el radio de la esfera: "))
                area = 4 * 3.1416 * radio ** 2
                volumen = (4/3) * 3.1416 * radio ** 3
                print(f"Área: {area}")
                print(f"Volumen: {volumen}")
            elif figura == 2:
                lado = float(input("Introduce el lado del cubo: "))
                area = 6 * lado ** 2
                volumen = lado ** 3
                print(f"Área: {area}")
                print(f"Volumen: {volumen}")
            elif figura == 3:
                radio = float(input("Introduce el radio del cilindro: "))
                altura = float(input("Introduce la altura del cilindro: "))
                area = 2 * 3.1416 * radio * (radio + altura)
                volumen = 3.1416 * radio ** 2 * altura
                print(f"Área: {area}")
                print(f"Volumen: {volumen}")
            elif figura == 4:
                radio = float(input("Introduce el radio del cono: "))
                altura = float(input("Introduce la altura del cono: "))
                area = 3.1416 * radio * (radio + (altura ** 2 + radio ** 2) ** 0.5)
                volumen = (1/3) * 3.1416 * radio ** 2 * altura
                print(f"Área: {area}")
                print(f"Volumen: {volumen}")
            else:
                print("Opción no válida.")
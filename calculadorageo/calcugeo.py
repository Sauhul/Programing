print("-----Calculadora Geométrica-----")
print("Calculadora de figuras 2D y 3D.")

print("1. Figuras 2D")
print("2. Figuras 3D")
print("10. Salir")

try:
    tipo = int(input("Escoja su tipo de figura: "))
except:
    print("Por favor, introduce un número válido.")
    exit()

# ─── MENÚ 2D ───
if tipo == 1:
    print("1. Cuadrado")
    print("2. Rectángulo")
    print("3. Triángulo rectángulo")
    print("4. Círculo")
    print("5. Trapecio")

    try:
        figura = int(input("Escoja su figura: "))
    except:
        print("Por favor, introduce un número válido.")
        exit()

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
        base = float(input("Introduce el cateto base: "))
        altura = float(input("Introduce el cateto altura: "))
        angulo_a = float(input("Introduce el ángulo A: "))

        hipotenusa = (base ** 2 + altura ** 2) ** 0.5
        angulo_b = 180 

    
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

# ─── MENÚ 3D ───
elif tipo == 2:
    print("1. Esfera")
    print("2. Cubo")
    print("3. Cilindro")
    print("4. Cono")

    try:
        figura = int(input("Escoja su figura: "))
    except:
        print("Por favor, introduce un número válido.")
        exit()

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
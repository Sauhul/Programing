import math

# ─────────────────────────────────────────────
#   UTILIDADES
# ─────────────────────────────────────────────

def pedir_numero(mensaje):
    """Pide un número positivo al usuario y valida la entrada."""
    while True:
        try:
            valor = float(input(mensaje))
            if valor <= 0:
                print("  ⚠  El valor debe ser mayor que 0. Inténtalo de nuevo.")
            else:
                return valor
        except ValueError:
            print("  ⚠  Entrada no válida. Escribe un número.")

def separador():
    print("\n" + "─" * 45 + "\n")

def pausar():
    input("\nPresiona Enter para continuar...")


# ─────────────────────────────────────────────
#   FIGURAS PLANAS (2D)
# ─────────────────────────────────────────────

def circulo():
    separador()
    print("  CÍRCULO")
    r = pedir_numero("  Radio: ")
    area      = math.pi * r ** 2
    perimetro = 2 * math.pi * r
    separador()
    print(f"  Área       = {area:.4f}")
    print(f"  Perímetro  = {perimetro:.4f}")
    pausar()

def cuadrado():
    separador()
    print("  CUADRADO")
    l = pedir_numero("  Lado: ")
    area      = l ** 2
    perimetro = 4 * l
    separador()
    print(f"  Área       = {area:.4f}")
    print(f"  Perímetro  = {perimetro:.4f}")
    pausar()

def rectangulo():
    separador()
    print("  RECTÁNGULO")
    b = pedir_numero("  Base: ")
    h = pedir_numero("  Altura: ")
    area      = b * h
    perimetro = 2 * (b + h)
    separador()
    print(f"  Área       = {area:.4f}")
    print(f"  Perímetro  = {perimetro:.4f}")
    pausar()

def trapecio():
    separador()
    print("  TRAPECIO")
    B  = pedir_numero("  Base mayor (B): ")
    b  = pedir_numero("  Base menor (b): ")
    h  = pedir_numero("  Altura (h): ")
    l1 = pedir_numero("  Lado izquierdo: ")
    l2 = pedir_numero("  Lado derecho: ")
    area      = ((B + b) / 2) * h
    perimetro = B + b + l1 + l2
    separador()
    print(f"  Área       = {area:.4f}")
    print(f"  Perímetro  = {perimetro:.4f}")
    pausar()

def menu_2d():
    while True:
        separador()
        print("  FIGURAS PLANAS — ¿Cuál quieres calcular?\n")
        print("  1. Círculo")
        print("  2. Cuadrado")
        print("  3. Rectángulo")
        print("  4. Trapecio")
        print("  0. Volver al menú principal")
        opcion = input("\n  Elige una opción: ").strip()
        if   opcion == "1": circulo()
        elif opcion == "2": cuadrado()
        elif opcion == "3": rectangulo()
        elif opcion == "4": trapecio()
        elif opcion == "0": break
        else: print("  ⚠  Opción no válida.")


# ─────────────────────────────────────────────
#   FIGURAS 3D
# ─────────────────────────────────────────────

def esfera():
    separador()
    print("  ESFERA")
    r = pedir_numero("  Radio: ")
    volumen    = (4 / 3) * math.pi * r ** 3
    superficie = 4 * math.pi * r ** 2
    separador()
    print(f"  Volumen     = {volumen:.4f}")
    print(f"  Superficie  = {superficie:.4f}")
    pausar()

def cubo():
    separador()
    print("  CUBO")
    l = pedir_numero("  Arista (l): ")
    volumen    = l ** 3
    superficie = 6 * l ** 2
    separador()
    print(f"  Volumen     = {volumen:.4f}")
    print(f"  Superficie  = {superficie:.4f}")
    pausar()

def cilindro():
    separador()
    print("  CILINDRO")
    r = pedir_numero("  Radio de la base: ")
    h = pedir_numero("  Altura: ")
    volumen    = math.pi * r ** 2 * h
    superficie = 2 * math.pi * r * (r + h)
    separador()
    print(f"  Volumen     = {volumen:.4f}")
    print(f"  Superficie  = {superficie:.4f}")
    pausar()

def cono():
    separador()
    print("  CONO")
    r = pedir_numero("  Radio de la base: ")
    h = pedir_numero("  Altura: ")
    g          = math.sqrt(r ** 2 + h ** 2)   # generatriz (calculada automáticamente)
    volumen    = (1 / 3) * math.pi * r ** 2 * h
    superficie = math.pi * r * (r + g)
    separador()
    print(f"  Generatriz  = {g:.4f}  (calculada automáticamente)")
    print(f"  Volumen     = {volumen:.4f}")
    print(f"  Superficie  = {superficie:.4f}")
    pausar()

def menu_3d():
    while True:
        separador()
        print("  FIGURAS 3D — ¿Cuál quieres calcular?\n")
        print("  1. Esfera")
        print("  2. Cubo")
        print("  3. Cilindro")
        print("  4. Cono")
        print("  0. Volver al menú principal")
        opcion = input("\n  Elige una opción: ").strip()
        if   opcion == "1": esfera()
        elif opcion == "2": cubo()
        elif opcion == "3": cilindro()
        elif opcion == "4": cono()
        elif opcion == "0": break
        else: print("  ⚠  Opción no válida.")


# ─────────────────────────────────────────────
#   TEOREMA DE PITÁGORAS
# ─────────────────────────────────────────────

def pitagoras():
    while True:
        separador()
        print("  TEOREMA DE PITÁGORAS  —  c² = a² + b²\n")
        print("  ¿Qué lado desconoces?\n")
        print("  1. Hipotenusa (c)  →  datos: catetos a y b")
        print("  2. Cateto (a)      →  datos: hipotenusa c y cateto b")
        print("  3. Cateto (b)      →  datos: hipotenusa c y cateto a")
        print("  0. Volver al menú principal")
        opcion = input("\n  Elige una opción: ").strip()

        if opcion == "1":
            separador()
            a = pedir_numero("  Cateto a: ")
            b = pedir_numero("  Cateto b: ")
            c = math.sqrt(a ** 2 + b ** 2)
            separador()
            print(f"  Hipotenusa c = √({a}² + {b}²) = {c:.4f}")
            pausar()

        elif opcion == "2":
            separador()
            c = pedir_numero("  Hipotenusa c: ")
            b = pedir_numero("  Cateto b: ")
            if c <= b:
                print("  ⚠  La hipotenusa debe ser mayor que cualquier cateto.")
            else:
                a = math.sqrt(c ** 2 - b ** 2)
                separador()
                print(f"  Cateto a = √({c}² - {b}²) = {a:.4f}")
            pausar()

        elif opcion == "3":
            separador()
            c = pedir_numero("  Hipotenusa c: ")
            a = pedir_numero("  Cateto a: ")
            if c <= a:
                print("  ⚠  La hipotenusa debe ser mayor que cualquier cateto.")
            else:
                b = math.sqrt(c ** 2 - a ** 2)
                separador()
                print(f"  Cateto b = √({c}² - {a}²) = {b:.4f}")
            pausar()

        elif opcion == "0":
            break
        else:
            print("  ⚠  Opción no válida.")


# ─────────────────────────────────────────────
#   MENÚ PRINCIPAL
# ─────────────────────────────────────────────

def menu_principal():
    while True:
        print("\n" + "═" * 45)
        print("       CALCULADORA GEOMÉTRICA")
        print("═" * 45)
        print("\n  1. Figuras planas  (área y perímetro)")
        print("  2. Figuras 3D      (volumen y superficie)")
        print("  3. Teorema de Pitágoras")
        print("  0. Salir\n")
        print("═" * 45)
        opcion = input("\n  Elige una opción: ").strip()

        if   opcion == "1": menu_2d()
        elif opcion == "2": menu_3d()
        elif opcion == "3": pitagoras()
        elif opcion == "0":
            print("\n  ¡Hasta luego!\n")
            break
        else:
            print("  ⚠  Opción no válida. Intenta de nuevo.")


# ─────────────────────────────────────────────
#   PUNTO DE ENTRADA
# ─────────────────────────────────────────────

if __name__ == "__main__":
    menu_principal()
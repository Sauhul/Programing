suma_total = 0
numero = float(input("Ingresa un número : "))

while numero != 0:
    suma_total += numero
    numero = float(input("Ingresa otro número : "))

print(f"La suma total es: {suma_total}")
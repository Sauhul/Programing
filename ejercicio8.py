n1 = float(input("Ingresa el primer número: "))
n2 = float(input("Ingresa el segundo número: "))

if n1 == n2:
    print("Son iguales.")
elif n1 > n2:
    print(f"{n1} es mayor que {n2}.")
else:
    print(f"{n2} es mayor que {n1}.")
opcion = "0"
saldo = 0.0 

while opcion != "4":
    print("\n========  Bienvenido al banco ===========")
    print(f"Saldo actual: ${saldo:.2f}")
    print("1. Consultar saldo")
    print("2. Retirar dinero")
    print("3. Depositar dinero")
    print("4. Salir")
    opcion = input("Selecciona una opción (1, 2, 3 o 4): ")

    if opcion == "1":
        print(f"Tu saldo actual es: ${saldo:.2f}")

    elif opcion == "2":
        try:
            entrada = input("Ingresa el monto a retirar: ").replace(",", ".")
            monto_retiro = float(entrada)
            
            if monto_retiro <= 0:
                print("Error: El monto debe ser un número positivo.")
            elif monto_retiro > saldo:
                print("Fondos insuficientes. No se puede realizar el retiro.")
            else:
                saldo -= monto_retiro
                print(f"Has retirado ${monto_retiro}. Tu nuevo saldo es: ${saldo:.2f}")
        except ValueError:
            print("Error: Debes ingresar un número válido (ejemplo: 10.50).")

    elif opcion == "3":
        try:
            entrada = input("Ingresa el monto a depositar: ").replace(",", ".")
            monto_deposito = float(entrada)
            
            if monto_deposito <= 0:
                print("Error: El monto a depositar debe ser mayor a cero.")
            else:
                saldo += monto_deposito
                print(f"Has depositado ${monto_deposito}. Tu nuevo saldo es: ${saldo:.2f}")
        except ValueError:
            print("Error: Debes ingresar un número válido.")

    elif opcion == "4":
        print("Gracias por usar nuestros servicios. ¡Hasta luego!")
    else:
        print("Opción no válida. Por favor, selecciona una opción del 1 al 4.")

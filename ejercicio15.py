clave_correcta = "2009"
entrada = input("Introduce la contraseña: ")

while entrada != clave_correcta:
    print("Contraseña incorrecta.")
    entrada = input("Inténtalo de nuevo: ")

print("Acceso concedido.")
clave = "2009"
iniciador = 0

entrada = input("introduce tu contraseña")
if len(entrada) > 4:
    print("la contraseña no puede tener mas de 4 cararacteres")
    exit()

arr1 = list(clave)
arr2 = list(entrada)
len(arr1) == len(arr2)

for i in range (len(arr1)):
    if arr1[i] == arr2[i] :
        iniciador += 1

    if entrada == clave:    
      print("contraseña correcta") 
      exit()
    else:
        print(f"Contraseña incorrecta, has acertado {iniciador} digitos de la posicion correspondiente")
        print("Intentelo de nuevo")

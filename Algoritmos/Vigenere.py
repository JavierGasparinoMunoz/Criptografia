def cifrar_vigenere(texto, clave):
    texto_cifrado = '' #Variable que guardara el texto cifrado
    clave_extendida = clave #Se inicializa una variable claveExtendida que tendra el valor de la clave dada
    while len(clave_extendida) < len(texto): #Se pregunta en el bucle hasta que sean del mismo tamaño
        clave_extendida += clave #esto es para que tengan el mismo tamaño que el texto que se quiere cifrar

    for i in range(len(texto)): #Se recorre cada letra del alfabeto que se va a cifrar
        caracter_texto = texto[i]
        caracter_clave = clave_extendida[i] #Se obtiene la letra que correponde a la clave extendida
        if caracter_texto.isalpha(): #Se comprueba si cada letra del texto es una letra del alfabeto con isalpha()
            valor_letra_texto = ord(caracter_texto.upper()) - ord('A') #Valor numerico de la letra del texto(va de 0 a 25)
            valor_letra_clave = ord(caracter_clave.upper()) - ord('A') #Valor numerico de la letra de la clave
            valor_letra_cifrada = (valor_letra_texto + valor_letra_clave) % 26 #Valor numerico de la letra cifrada(Se suman los dos campos)
            caracter_cifrado = chr(valor_letra_cifrada + ord('A')) #El  valor numerico obtenido se convierte a una letra
        else: #Si la letra del texto no es una letra del alfabeto, el caracter del  cifrado es el mismo que el original
            caracter_cifrado = caracter_texto
        texto_cifrado += caracter_cifrado

    return texto_cifrado


def descifrar_vigenere(texto_cifrado, clave):
    texto_descifrado = '' #Variable que guardara el texto descifrado
    clave_extendida = clave #Se inicializa una variable claveExtendida que tendra el valor de la clave dada
    while len(clave_extendida) < len(texto_cifrado): #Se pregunta en el bucle hasta que sean del mismo tamaño
        clave_extendida += clave #esto es para que tengan el mismo tamaño que el texto cifrado que se quiere descifrar

    for i in range(len(texto_cifrado)): #Se recorre cada letra del texto cifrado que se va a descifrar
        caracter_texto_cifrado = texto_cifrado[i]
        caracter_clave = clave_extendida[i] #Se obtiene la letra que correponde a la clave extendida
        if caracter_texto_cifrado.isalpha(): #Se comprueba si cada letra del texto cifrado es una letra del alfabeto con isalpha()
            valor_letra_texto_cifrado = ord(caracter_texto_cifrado.upper()) - ord('A') #Valor numerico de la letra del texto(va de 0 a 25)
            valor_letra_clave = ord(caracter_clave.upper()) - ord('A') #Valor numerico de la letra de la clave
            valor_letra_descifrada = (valor_letra_texto_cifrado - valor_letra_clave) % 26 #Valor numerico de la letra cifrada(Se restan los dos campos)
            caracter_descifrado = chr(valor_letra_descifrada + ord('A')) #El  valor numerico obtenido se convierte a una letra
        else: #Si la letra del texto cifrado no es una letra del alfabeto, el caracter del descifrado es el mismo que el original
            caracter_descifrado = caracter_texto_cifrado
        texto_descifrado += caracter_descifrado

    return texto_descifrado


while True:
    # Menu con las distintas opciones
    print("-------------------------------")
    print("Seleccione una opción:")
    print("1. Cifrar texto con Vigenère")
    print("2. Descifrar texto con Vigenère")
    print("3. Salir")
    print("-------------------------------")

    #Lectura de la opcion del menu
    opcion = input("Opción: ")

    # Opcion para el cifrado
    if opcion == '1':
        texto = input("Ingrese el texto a cifrar: ")
        clave = input("Ingrese la clave: ")
        texto_cifrado = cifrar_vigenere(texto, clave)
        print("Texto cifrado: ", texto_cifrado)

    # Opcion para el descifrado
    elif opcion == '2':
        texto_cifrado = input("Ingrese el texto cifrado: ")
        clave = input("Ingrese la clave: ")
        texto_descifrado = descifrar_vigenere(texto_cifrado, clave)
        print("Texto descifrado: ", texto_descifrado)

    # Opcion para salir del programa
    elif opcion == '3':
        break

    # Opción que ocurre si no has introducido niguna de las opciones correctas
    else:
        print("Opción inválida. Intente de nuevo.")
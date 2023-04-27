def cifrar_vigenere(texto, clave):
    textoCifrado = '' #Variable que guardara el texto cifrado
    claveExtendida = clave #Se inicializa una variable claveExtendida que tendra el valor de la clave dada
    while len(claveExtendida) < len(texto): #Se pregunta en el bucle hasta que sean del mismo tamaño
        claveExtendida += clave #esto es para que tengan el mismo tamaño que el texto que se quiere cifrar

    for i in range(len(texto)): #Se recorre cada letra del alfabeto que se va a cifrar
        caracter = texto[i]
        caracterClave = claveExtendida[i] #Se obtiene la letra que correponde a la clave extendida
        if caracter.isalpha(): #Se comprueba si cada letra del texto es una letra del alfabeto con isalpha()
            valorTexto= ord(caracter.upper()) - ord('A') #Valor numerico de la letra del texto(va de 0 a 25)
            valorClave = ord(caracterClave.upper()) - ord('A') #Valor numerico de la letra de la clave
            valorCifrada = (valorTexto+ valorClave) % 26 #Valor numerico de la letra cifrada(Se suman los dos campos)
            caracterCifrado = chr(valorCifrada + ord('A')) #El  valor numerico obtenido se convierte a una letra
        else: #Si la letra del texto no es una letra del alfabeto, el caracter del  cifrado es el mismo que el original
            caracterCifrado = caracter
        textoCifrado += caracterCifrado

    return textoCifrado


def descifrar_vigenere(textoCifrado, clave):
    textoDescifrado = '' #Variable que guardara el texto descifrado
    claveExtendida = clave #Se inicializa una variable claveExtendida que tendra el valor de la clave dada
    while len(claveExtendida) < len(textoCifrado): #Se pregunta en el bucle hasta que sean del mismo tamaño
        claveExtendida += clave #esto es para que tengan el mismo tamaño que el texto cifrado que se quiere descifrar

    for i in range(len(textoCifrado)): #Se recorre cada letra del texto cifrado que se va a descifrar
        caracter = textoCifrado[i]
        caracterClave = claveExtendida[i] #Se obtiene la letra que correponde a la clave extendida
        if caracter.isalpha(): #Se comprueba si cada letra del texto cifrado es una letra del alfabeto con isalpha()
            valorTexto = ord(caracter.upper()) - ord('A') #Valor numerico de la letra del texto(va de 0 a 25)
            valorClave = ord(caracterClave.upper()) - ord('A') #Valor numerico de la letra de la clave
            valorDescifrada = (valorTexto - valorClave) % 26 #Valor numerico de la letra cifrada(Se restan los dos campos)
            caracterDescifrado = chr(valorDescifrada + ord('A')) #El  valor numerico obtenido se convierte a una letra
        else: #Si la letra del texto cifrado no es una letra del alfabeto, el caracter del descifrado es el mismo que el original
            caracterDescifrado = caracter
        textoDescifrado+= caracterDescifrado

    return textoDescifrado


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
        textoCifrado = cifrar_vigenere(texto, "Vigenere")
        print("Texto cifrado: ", textoCifrado)

    # Opcion para el descifrado
    elif opcion == '2':
        textoCifrado = input("Ingrese el texto cifrado: ")
        textoDescifrado = descifrar_vigenere(textoCifrado, "Vigenere")
        print("Texto descifrado: ", textoDescifrado)

    # Opcion para salir del programa
    elif opcion == '3':
        break

    # Opción que ocurre si no has introducido niguna de las opciones correctas
    else:
        print("Opción inválida. Intente de nuevo.")

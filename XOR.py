def cifrar_xor(mensaje, clave):
    mensaje_codificado = ""
    for i in range(len(mensaje)):
        # Obtenemos el código ASCII de cada carácter del mensaje y de la clave
        mensaje_ascii = ord(mensaje[i])
        clave_ascii = ord(clave[i % len(clave)])
        # Realizamos la operación XOR entre los códigos ASCII
        resultado_xor = mensaje_ascii ^ clave_ascii
        # Convertimos el resultado a un carácter y lo agregamos al mensaje codificado
        mensaje_codificado += chr(resultado_xor)
    return mensaje_codificado

def descifrar_xor(mensaje_codificado, clave):
    mensaje_descifrado = ""
    for i in range(len(mensaje_codificado)):
        # Obtenemos el código ASCII de cada carácter del mensaje codificado y de la clave
        mensaje_codificado_ascii = ord(mensaje_codificado[i])
        clave_ascii = ord(clave[i % len(clave)])
        # Realizamos la operación XOR entre los códigos ASCII
        resultado_xor = mensaje_codificado_ascii ^ clave_ascii
        # Convertimos el resultado a un carácter y lo agregamos al mensaje descifrado
        mensaje_descifrado += chr(resultado_xor)
    return mensaje_descifrado

# Menú principal
while True:
    opcion = input("Seleccione una opción:\n1. Cifrar mensaje\n2. Descifrar mensaje\n3. Salir\n")
    if opcion == "1":
        mensaje = input("Ingrese el mensaje a cifrar: ")
        clave = input("Ingrese la clave: ")
        mensaje_codificado = cifrar_xor(mensaje, clave)
        print("Mensaje cifrado: " + mensaje_codificado)
    elif opcion == "2":
        mensaje_codificado = input("Ingrese el mensaje cifrado: ")
        clave = input("Ingrese la clave: ")
        mensaje_descifrado = descifrar_xor(mensaje_codificado, clave)
        print("Mensaje descifrado: " + mensaje_descifrado)
    elif opcion == "3":
        break
    else:
        print("Opción inválida. Intente de nuevo.")
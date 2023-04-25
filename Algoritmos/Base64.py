def codificar_base64(cadena,listaCaracteres):

    # Se convierte la cadena entera a cadena de bits
    cadenaBits = ''
    for caracter in cadena:
        cadenaBits += format(ord(caracter), '08b')

    # Si la cantidad de bits no es un múltiplo de 6, se agregan ceros al final hasta que sea un multiplo de 6
    while len(cadenaBits) % 6 != 0:
        cadenaBits += '0'

    # Se crea la variable bloques que contendra cada bloque de 6 bits
    bloques = []
    for i in range(0, len(cadenaBits), 6):
        bloques.append(cadenaBits[i:i + 6])

    #Se crea la cadena codificada
    cadenaCodificada = ''
    for bloque in bloques:
        indice = int(bloque, base=2)
        cadenaCodificada += listaCaracteres[indice]

    # Si la cantidad de caracteres de la codificación no es un múltiplo de 4, se agregan = al final
    while len(cadenaCodificada) % 4 != 0:
        cadenaCodificada += '='

    # Se devuelve la cadena ya codificada
    return cadenaCodificada


def decodificar_base64(cadenaCodificada,listaCaracteres):

    # Se eliminan los signos de igual del final
    cadenaCodificada = cadenaCodificada.rstrip('=')

    # Se convierte a una cadena de bits
    cadenaBits = ''
    for caracter in cadenaCodificada:
        indice = listaCaracteres.index(caracter)
        cadenaBits += format(indice, '06b')

    # Si la cantidad de bits no es un múltiplo de 8, se eliminan los bits adicionales del final
    while len(cadenaBits) % 8 != 0:
        cadenaBits = cadenaBits[:-1]

    # Se convierte la cadena de bits a una cadena de caracteres
    cadenaDecodificada = ''
    for i in range(0, len(cadenaBits), 8):
        caracter = chr(int(cadenaBits[i:i + 8], base=2))
        cadenaDecodificada += caracter


    return cadenaDecodificada

if __name__ == '__main__':
    while True:
        print("-----------------------")
        print("Seleccione una opción")
        print("1. Codificar texto Base64")
        print("2. Decodificar texto Base64")
        print("3. Salir")
        print("-----------------------")
        opcion = input("Ingrese una opción: ")

        # Se crea una lista con los caracteres que se utilizarán en la codificación o decodificacion
        listaCaracteres = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

        if opcion == "1":
            cadenaBase64 = input("Introduce la cadena que quieres codificar/decodifcar: ")
            textoCifrado = codificar_base64(cadenaBase64,listaCaracteres)
            print("El texto codificado es: ", textoCifrado)

        elif opcion == "2":
            cadenaBase64 = input("Introduce la cadena que quieres codificar/decodifcar: ")
            textoDescifrado = decodificar_base64(cadenaBase64,listaCaracteres)
            print("El texto descifrado es: ", textoDescifrado)

        elif opcion == "3":
            print("Saliendo....")
            break

        else:
            print("Opción inválida.")
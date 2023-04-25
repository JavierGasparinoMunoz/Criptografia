def rot_n(texto, n):
    resultado = "" #Se inicializa la variable resultado que va a contener la cadena codificada o decodificada
    for caracter in texto:
        if caracter.isalpha(): #Comprueba que la cadena solo este compuesta por letras
            mayus = caracter.isupper() #Se guarda en una variable si la letra es mayuscula para que posteriormente se cambie a mayuscula si es así
            caracter = caracter.lower() #Se pasa la letra a minuscula
            codigo = ord(caracter) - 97 #Se obtiene la posicion de la letra minuscula
            codigo = (codigo + n) % 26 #Se le suma el desplazamiento y se asegura que no se obtiene un caracter fuera del abecedario
            caracter = chr(codigo + 97) #Se pasa a letra con el desplazamiento ya incluido
            if mayus: #En caso de que la letra fuese una mayuscula, esta se cambiara de nuevo a mayuscula
                caracter = caracter.upper() #Se pasa a mayusucula
        resultado += caracter #Se introduce la letra codificada/decodificada a la cadena
    return resultado

if __name__ == '__main__':
    while True:
        print("-----------------------")
        print("Seleccione una opción")
        print("1. Codificar texto ROT-N/Cesar")
        print("2. Decodificar texto ROT-N/Cesar")
        print("3. Salir")
        print("-----------------------")
        opcion = input("Ingrese una opción: ")
        if opcion == "1":
            cadenaCode= input("Introduce la cadena que quieres codificar: ")
            n = int(input("Introduce una N (Número de desplazamientos para codificar): "))
            textoCifrado = rot_n(cadenaCode,n)
            print("El texto resultante es: ", textoCifrado)
        elif opcion == "2":
            cadenaDecode = input("Introduce la cadena que quieres decodificar: ")
            for i in range(1,27): #Debido a que hay 27 caracteres en el alfabeto ingles y no queremos que se repita el desplazamiento, hacemos fuerza bruta hasta con 27 n
                textoDescifrado = rot_n(cadenaDecode,-i)
                print(i,"El texto descifrado es: ", textoDescifrado)
        elif opcion == "3":
            print("Saliendo....")
            break
        else:
            print("Opción inválida.")


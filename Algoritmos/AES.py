from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import base64

key = b"SeguridadInforma"  # Clave de 16 bytes
iv = b"SeguridadInforma"   # IV de 16 bytes

def aes_cbc_encrypt(data):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    encrypted = cipher.encrypt(pad(data.encode(), AES.block_size))
    return base64.b64encode(encrypted)

def aes_cbc_decrypt(data):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted = cipher.decrypt(base64.b64decode(data))
    return unpad(decrypted, AES.block_size).decode()

# Menú principal
while True:
    opcion = input("Seleccione una opción:\n1. Cifrar mensaje\n2. Descifrar mensaje\n3. Salir\n")
    if opcion == "1":
        mensaje = input("Introduzca el mensaje a cifrar: ")
        mensaje_cifrado = aes_cbc_encrypt(mensaje)
        print("Mensaje cifrado: ", mensaje_cifrado.decode())
    elif opcion == "2":
        mensaje_cifrado = input("Introduzca el mensaje cifrado: ")
        mensaje_descifrado = aes_cbc_decrypt(mensaje_cifrado.encode())
        print("Mensaje descifrado: ", mensaje_descifrado)
    elif opcion == "3":
        break
    else:
        print("Opción inválida. Intente de nuevo.")


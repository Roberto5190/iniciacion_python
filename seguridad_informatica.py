from cryptography.fernet import Fernet
import bcrypt
import re

# ---------- A. Cifrado y Descifrado de datos ----------

# Generar una clave y crear el objeto Fernet
clave = Fernet.generate_key()
cifrador = Fernet(clave)

def cifrar_mensaje(mensaje):
    return cifrador.encrypt(mensaje.encode())

def descifrar_mensaje(mensaje_cifrado):
    return cifrador.decrypt(mensaje_cifrado).decode()

# ---------- B. Hashing de contraseñas ----------

def hashear_contrasena(contrasena):
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(contrasena.encode(), salt)
    return hashed

def verificar_contrasena(contrasena, hashed):
    return bcrypt.checkpw(contrasena.encode(), hashed)

# ---------- C. Prevención de inyecciones simples ----------

def entrada_segura(usuario_input):
    # Evitar comandos peligrosos, scripts, o caracteres especiales
    if re.search(r"[;$|&`<>]", usuario_input):
        return False
    return True

# ---------- Prueba del sistema ----------

if __name__ == "__main__":
    print("🔐 DEMO SEGURIDAD EN PYTHON")

    # A. Cifrado / Descifrado
    texto = "Información secreta"
    cifrado = cifrar_mensaje(texto)
    print(f"Cifrado: {cifrado}")
    print(f"Descifrado: {descifrar_mensaje(cifrado)}")

    # B. Hashing de contraseñas
    contrasena = "mi_contraseña_segura123"
    hash_guardado = hashear_contrasena(contrasena)
    print(f"Hash guardado: {hash_guardado}")
    print("¿Contraseña correcta?", verificar_contrasena("mi_contraseña_segura123", hash_guardado))

    # C. Prevención básica
    entrada = input("Introduce un nombre de usuario: ")
    if entrada_segura(entrada):
        print(f"Entrada aceptada: {entrada}")
    else:
        print("🚫 Entrada peligrosa detectada y rechazada.")

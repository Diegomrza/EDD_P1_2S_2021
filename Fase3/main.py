from cryptography.fernet import Fernet
import hashlib

class estudiante:
    def __init__(self, carnet, nombre, edad, correo, password) -> None:
        self.carnet = carnet
        self.nombre = nombre
        self.edad = edad
        self.correo = correo
        self.password = password

lista = []

clave = Fernet.generate_key()

f = Fernet(clave)

info = f.encrypt(b'Hola buenas tardes')
print(info.decode())
f2 = f.decrypt(info)
print(f2.decode())

'''for x in range(2):
    carnet = bytes(201901429)
    nombre = b"Diego Abraham Robles Meza"
    edad = bytes(int(23))
    correo = b'diegomrza98@gmail.com'
    password = b'Marihuana7291384650'
    
    fCarnet = f.encrypt(carnet)
    fNombre = f.encrypt(nombre)
    fEdad = f.encrypt(edad)
    fCorreo = f.encrypt(correo)
    fPassword = f.encrypt(password)
    nuevo = estudiante(fCarnet, fNombre, fEdad, fCorreo, fPassword)
    lista.append(nuevo)'''

cadena = 'Diego abraham Robles meza'
cadena1 = 'Alan abraham Robles meza'
cadena = cadena.encode()
print(cadena)

cadena = cadena.decode()
print(cadena[0:5])

cadena2 = hashlib.sha256(cadena.encode())
cadena3 = hashlib.sha256(cadena.encode())
print('C2: ', cadena2.hexdigest())
print('C3: ', cadena3.hexdigest())

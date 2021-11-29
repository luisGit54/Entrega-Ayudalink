import requests

from Datos.Modelos.REST import rest


def validar_credenciales(usuario, clave):
    body = {"nombre": usuario,
            "clave": clave}
    respuesta = requests.post(f'{rest.API_URL}/login',json=body)
    return respuesta.status_code ==200


def crear_usuario(usuario, clave):
    body= {"nombre": usuario,
           "clave": clave}
    respuesta = requests.post(f'{rest.API_URL}/usuarios',json=body)
    return respuesta.status_code == 200

def obtener_usuarios():
    respuesta = requests.get(f'{rest.API_URL}/usuarios')
    return respuesta.json()
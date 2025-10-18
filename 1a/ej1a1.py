"""
Enunciado:
Introducción básica a la biblioteca requests de Python.
La biblioteca requests permite realizar peticiones HTTP de forma sencilla.

En este ejercicio, aprenderás a:
1. Realizar una petición GET a una API pública
2. Interpretar una respuesta en formato texto plano
3. Manejar errores en peticiones HTTP

Tu tarea es completar la función indicada para realizar una consulta básica
a la API de ipify.org, un servicio estable que proporciona la IP pública.
"""

import requests

URL = "https://api.ipify.org"

def get_user_ip():
    """
    Realiza una petición GET a api.ipify.org para obtener la dirección IP pública
    en formato texto plano.

    Returns:
        str: La dirección IP si la petición es exitosa
        None: Si ocurre un error en la petición
    """
    # Completa esta función para:
    # 1. Realizar una petición GET a la URL https://api.ipify.org (sin parámetros)
    # 2. Verificar si la petición fue exitosa (código 200)
    # 3. Devolver el texto de la respuesta directamente (contiene la IP)
    # 4. Devolver None si hay algún error
    #pass

    """
            response.raise_for_status()

            Podria evaluar el codigo con un ifelse o algo similar a a un swithc else 
            pero utilizo raise_for_Status para que en caso de un código de error salte una excepcion:

            NO reiventar la rueda.
            Pero por lo que leo en el enunciado, hay que hacerlo a mano.
            """ 

    """
    try:
        response = requests.get(url = URL)
        if response.status_code != 200:
            return None
        print(f"Obtenido: {response}\n")
    except RequestException as e:
        print(f"Error al obtener la url {URL}\n") 
        return None
    """
    #Llamo la url con el objeto request y obtengo la respuesta en response
    try:
        response = requests.get(url = URL)
        #Check del codigo.
        if response.status_code != 200:
            return None
        # OJO!!!  que nos devuelven un array de bytes, no un string por lo que antes de devolverlo lo tengo que decodificar
        return response.content.decode()
    except Exception as e:
        """
        Aqui deberian ir todas las excepciones que manerjo pero como me especifican que ante cualquier error devuelva None,
        le pongo el catch Excception generico.
        """
        return None

if __name__ == "__main__":
    # Ejemplo de uso de la función
    ip = get_user_ip()
    if ip:
        print(f"Tu dirección IP pública es: {ip}")
    else:
        print("No se pudo obtener la dirección IP")

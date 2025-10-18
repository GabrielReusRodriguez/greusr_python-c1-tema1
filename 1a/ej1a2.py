"""
Enunciado:
Continuando con la biblioteca requests de Python.
En este ejercicio, aprenderás a trabajar con respuestas en formato JSON.

En este ejercicio, aprenderás a:
1. Realizar una petición GET a una API pública
2. Interpretar una respuesta en formato JSON
3. Extraer información específica de un objeto JSON

Tu tarea es completar la función indicada para realizar una consulta a la API
de ipify.org usando el formato JSON, que es más estructurado que el texto plano.
"""

import requests


URL="https://api.ipify.org?format=json"

def get_user_ip_json():
    """
    Realiza una petición GET a api.ipify.org para obtener la dirección IP pública
    en formato JSON.

    Returns:
        str: La dirección IP si la petición es exitosa
        None: Si ocurre un error en la petición
    """
    # Completa esta función para:
    # 1. Realizar una petición GET a la URL https://api.ipify.org?format=json
    # 2. Verificar si la petición fue exitosa (código 200)
    # 3. Convertir la respuesta a formato JSON
    # 4. Extraer y devolver la IP del campo "ip" del objeto JSON
    # 5. Devolver None si hay algún error

    try:
        response = requests.get(url = URL)
        if response.status_code != 200:
            return None
        #Transformo el json a un diccionario Python.
        json_data = response.json()
        #Accedo al campo ip del diccionario.
        return json_data["ip"]

    except Exception as e:
        return None


def get_response_info():
    """
    Obtiene información adicional sobre la respuesta HTTP al consultar la API.
    
    Returns:
        dict: Diccionario con información de la respuesta (tipo de contenido,
              tiempo de respuesta, tamaño de la respuesta)
        None: Si ocurre un error en la petición
    """
    # Completa esta función para:
    # 1. Realizar una petición GET a la URL https://api.ipify.org?format=json
    # 2. Verificar si la petición fue exitosa (código 200)
    # 3. Crear y devolver un diccionario con:
    #    - 'content_type': El tipo de contenido de la respuesta
    #    - 'elapsed_time': El tiempo que tardó la petición (en milisegundos)
    #    - 'response_size': El tamaño de la respuesta en bytes
    # 4. Devolver None si hay algún error
    #pass
    try:
        response = requests.get(url = URL)
        if response.status_code != 200:
            return None
        # Tengo la respuesta por lo que accedo a los campos que necesito.
        info_data = {}
        # El content type lo saco de la cabecera http de la respuesta Content-Type
        info_data["content_type"] = response.headers["Content-Type"]
        """ 
            El tiempo de la peticion lo saco del propio rsponse elapsed  pero OJO!! que elapsed es un objeto timedelta https://docs.python.org/3/library/datetime.html
             para obtener el numero de segundos hay que usar la funcion total_seconds() 
        """
        info_data["elapsed_time"] = response.elapsed.total_seconds()
        """ El tamaño de la respuesta lo saco de la cabecera http de la respuesta Content-Length 
                PEEEEEEEEEEEERO esa web no incluye esa cabecera asi que le hago un len
        """
        info_data["response_size"] = len(response.content) 
        return info_data
    except Exception as e:
        return None

if __name__ == "__main__":
    # Ejemplo de uso de las funciones
    ip = get_user_ip_json()
    if ip:
        print(f"Tu dirección IP pública es: {ip}")
        
        # Mostrar información adicional de la respuesta
        info = get_response_info()
        if info:
            print("\nInformación de la respuesta:")
            print(f"Tipo de contenido: {info['content_type']}")
            print(f"Tiempo de respuesta: {info['elapsed_time']} ms")
            print(f"Tamaño de la respuesta: {info['response_size']} bytes")
    else:
        print("No se pudo obtener la dirección IP")

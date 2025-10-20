"""
Enunciado:
Manejo avanzado de errores HTTP con la biblioteca requests de Python.

En este ejercicio, aprenderás a:
1. Realizar peticiones a diferentes URLs que generarán distintos códigos de estado HTTP
2. Diferenciar entre varios tipos de errores HTTP (4xx, 5xx)
3. Manejar redirecciones (códigos 3xx)
4. Extraer información detallada de las respuestas de error
5. Procesar respuestas JSON con información específica sobre el estado

Tu tarea es completar la función request_with_error_handling para manejar adecuadamente
diferentes tipos de respuestas HTTP, incluyendo errores cliente (4xx), errores servidor (5xx)
y redirecciones (3xx).

Nota: El servidor httpstatuses.maor.io devuelve respuestas JSON con la siguiente estructura:

{
    "code": 404,
    "description": "Not Found"
}

Deberás comprobar que el código en el encabezado HTTP coincide con el campo "code"
en el cuerpo JSON y usar el campo "description" para proporcionar información detallada.
"""

import requests

def request_with_error_handling(url):
    """
    Realiza una petición GET a la URL proporcionada y maneja los diferentes tipos de
    respuestas HTTP que puedan ocurrir.

    Args:
        url (str): La URL a la que se realizará la petición

    Returns:
        dict: Un diccionario con la siguiente información:
            - success (bool): True si la petición fue exitosa (código 2xx), False en otro caso
            - status_code (int): El código de estado HTTP
            - is_redirect (bool): True si la respuesta es una redirección (código 3xx)
            - redirect_url (str, opcional): URL de redirección si is_redirect es True
            - error_type (str, opcional): "client_error" para 4xx, "server_error" para 5xx
            - message (str): Un mensaje descriptivo sobre el resultado de la petición
    """
    # Completa esta función para manejar diferentes tipos de respuestas HTTP
    # Debes gestionar al menos:
    # - Respuestas exitosas (códigos 2xx)
    # - Redirecciones (códigos 3xx)
    # - Errores del cliente (códigos 4xx)
    # - Errores del servidor (códigos 5xx)
    #   pass
    resp_info = { 
        'success' : None,
        'status_code' : None,
        'is_redirect' : None,
 #       'redirect_url' : None,
#        'error_type' : None,
        'message' : None
    }
    
    try:
        # LLamada get de la url.
        """ 
            Para poder pasar los tests, he de indicar que NO siga los redirects ya que si no,
            intenta conectar a la url de la redirect que NO existe y cuela como error.
        """
        response = requests.get(url = url, allow_redirects = False)
        # Usamos raise for status para que identifique el error y lance el error.
        response.raise_for_status()
        resp_info['status_code'] = response.status_code
        resp_info['message'] = response.text
        if 200 <=response.status_code < 300:
            resp_info['success'] = True
            resp_info['is_redirect'] = False
        if 300 <= response.status_code < 400:
            resp_info['success'] = False
            resp_info['is_redirect'] = True
            # La redireccion la podemos obtener del header  , campo Location.
            resp_info['redirect_url'] = response.headers['Location']
    
    # Excepciones de tipo HTTP.
    except requests.exceptions.HTTPError as e:
        resp_info['success'] = False
        resp_info['status_code'] = e.response.status_code
        resp_info['is_redirect'] = False
        #Identifico el tipo de error HTTP cliente o servidor.
        if 400 <= e.response.status_code < 500:
            resp_info['error_type'] = 'client_error'
        if 500 <= e.response.status_code:
            resp_info['error_type'] = 'server_error'
        # obtengo el mensaje de la excepcion
        resp_info['message'] = str(e)
        """
        except requests.exceptions.RequestException as e:
            resp_info['success'] = False
            resp_info['status_code'] = e.response.status_code
            resp_info['is_redirect'] = False
            #Identifico el tipo de error HTTP cliente o servidor.
            #        if 400 <= e.response.status_code < 500:
            #            resp_info['error_type'] = 'client_error'
            #        if 500 <= e.response.status_code:
            #            resp_info['error_type'] = 'server_error'
            # obtengo el mensaje de la excepcion
            resp_info['message'] = str(e)
            
        """

    except  requests.exceptions.ConnectionError as e:
        resp_info['success'] = False
        resp_info['is_redirect'] = False
        #resp_info['status_code'] = 34
        resp_info['message'] = 'connection_error'
    #Excepcion cajon desastre
    
    except Exception as e:
        #print(f"EXCEPTION {e}")
        resp_info['success'] = False
        #resp_info['status_code'] = e
        resp_info['is_redirect'] = False
        resp_info['message'] = str(e)
    finally:
        return resp_info

if __name__ == "__main__":
    # Puedes probar tu función con estas URLs:

    # Para probar un error 404 (Not Found)
    print("Probando URL con error 404:")
    result = request_with_error_handling("https://httpstatuses.maor.io/404")
    print(f"Resultado: {result}")

    # Para probar un error 500 (Server Error)
    print("\nProbando URL con error 500:")
    result = request_with_error_handling("https://httpstatuses.maor.io/500")
    print(f"Resultado: {result}")

    # Para probar una redirección 301 (Moved Permanently)
    print("\nProbando URL con redirección 301:")
    result = request_with_error_handling("https://httpstatuses.maor.io/301")
    print(f"Resultado: {result}")

    # Para probar una respuesta exitosa
    print("\nProbando URL con respuesta exitosa:")
    result = request_with_error_handling("https://httpstatuses.maor.io/200")
    print(f"Resultado: {result}")

    print("\nProbando URL test:")
    result = request_with_error_handling("https://httpstatuses.maor.io/301")
    print(f"Resultado: {result}")



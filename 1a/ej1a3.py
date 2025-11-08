"""
Enunciado:
Desarrolla un servidor web básico utilizando la biblioteca http.server de Python.
El servidor debe responder a peticiones GET y proporcionar información sobre la IP del cliente.

`GET /ip`: Devuelve la dirección IP del cliente en formato JSON.

Esta es una introducción a los servidores HTTP en Python para entender cómo:
1. Crear una aplicación web básica sin usar frameworks
2. Responder a diferentes rutas en una petición HTTP
3. Procesar encabezados de peticiones HTTP
4. Devolver respuestas en formato JSON

Tu tarea es completar la implementación de la clase MyHTTPRequestHandler.

Nota: Para obtener la IP del cliente, necesitarás examinar los encabezados de la petición HTTP.
Algunos encabezados comunes para esto son: X-Forwarded-For, X-Real-IP o directamente la dirección
del cliente mediante self.client_address.
"""

import json
from http.server import HTTPServer, BaseHTTPRequestHandler

class MyHTTPRequestHandler(BaseHTTPRequestHandler):
    """
    Manejador de peticiones HTTP personalizado
    """

    def do_GET(self):
        """
        Método que se ejecuta cuando se recibe una petición GET.

        Rutas implementadas:
        - `/ip`: Devuelve la IP del cliente en formato JSON

        Para otras rutas, devuelve un código de estado 404 (Not Found).
        """
        # Implementa aquí la lógica para responder a las peticiones GET
        # 1. Verifica la ruta solicitada (self.path)
        # 2. Si la ruta es "/ip", envía una respuesta 200 con la IP del cliente en formato JSON
        # 3. Si la ruta es cualquier otra, envía una respuesta 404

        # PISTA: Para obtener la IP del cliente puedes usar el método auxiliar _get_client_ip()
        #print(f"Ruta : {self.path}")
        if self.path == "/ip":
            #Envio el status y el header
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            #ULTRA IMPORTANTE!!! hacer un end headers xq si no considera el contenido como un hdeader. (los 3 \n del protovolo HTTP)
            self.end_headers()
            ip = self._get_client_ip()
            resp_content = {}
            resp_content["ip"] = ip
            #Transformamos el diccionario a json con json.dumps. pero lo hemos de enviar como bytes asi que lo codificamos como utf-8
            self.wfile.write(json.dumps(resp_content).encode("utf-8"))

        else:
            #Error, path no encontrado => comunicamos el 404 y el texto que lo informa.
            self.send_response(404)
            self.send_header("Content-Type", "application/json")
            #ULTRA IMPORTANTE!!! hacer un end headers xq si no considera el contenido como un hdeader. (los 3 \n del protovolo HTTP)
            self.end_headers()
            self.wfile.write(b"")
            #self.send_header("Content-Type", "text/html")
            #self.wfile.write(b"<html><body><h1>404: NOT FOUND!</h1></body></html>")


    def _get_client_ip(self):
        """
        Método auxiliar para obtener la IP del cliente desde los encabezados.
        Debes implementar la lógica para extraer la IP del cliente desde los encabezados
        de la petición o desde la dirección directa del cliente.

        Returns:
            str: La dirección IP del cliente
        """
        # Implementa aquí la lógica para extraer la IP del cliente
        # 1. Verifica si existe el encabezado 'X-Forwarded-For' (común en servidores con proxy)
        # 2. Si no existe, verifica otros encabezados comunes como 'X-Real-IP'
        # 3. Como último recurso, utiliza self.client_address[0]
        if self.headers.get("X-Forwarded-For") is not None:
            return self.headers.get("X-Forwarded-For")
        elif self.headers.get("X-Real-IP") is not None:
            return self.headers.get("X-Real-IP")
        else:
            return self.client_address[0]

#    def log_message(self, format, *args):
#        return


def create_server(host="localhost", port=8000):
    """text/html
    Crea y configura el servidor HTTP
    """
    server_address = (host, port)
    httpd = HTTPServer(server_address, MyHTTPRequestHandler)
    return httpd

def run_server(server):
    """
    Inicia el servidor HTTP
    """
    print(f"Servidor iniciado en http://{server.server_name}:{server.server_port}")
    server.serve_forever()

if __name__ == '__main__':
    server = create_server()
    run_server(server)

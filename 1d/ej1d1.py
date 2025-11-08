"""
Enunciado:
Este ejercicio introduce el uso de bibliotecas especializadas para acceder a APIs de forma
sencilla y estructurada. En concreto, utilizaremos la biblioteca pybikes que proporciona
wrappers para múltiples sistemas de bicicletas compartidas en todo el mundo.

En lugar de construir nuestro propio cliente HTTP y procesar manualmente los datos JSON,
aprenderemos a utilizar herramientas existentes que hacen este trabajo por nosotros.

Tareas:
1. Explorar los sistemas de bicicletas disponibles
2. Obtener información sobre el sistema de Barcelona (Bicing)
3. Analizar los datos de las estaciones

Esta práctica ilustra cómo las bibliotecas especializadas simplifican el acceso a APIs
y permiten concentrarse en el análisis de datos en lugar de en los detalles técnicos
de la comunicación con la API.
"""

import pybikes
import pandas as pd
import time
from typing import List, Dict, Any, Optional
import matplotlib.pyplot as plt
import sys


def listar_sistemas_disponibles() -> List[str]:
    """
    Obtiene una lista de todos los sistemas de bicicletas disponibles en pybikes.

    Returns:
        List[str]: Lista de identificadores de sistemas disponibles
    """
    # Implementa aquí la lógica para obtener y devolver la lista
    # de sistemas disponibles en pybikes
    #pass
    lista_sistemas = []
    lista_sistemas = pybikes.get_schemas()
    return lista_sistemas


def buscar_sistema_por_ciudad(ciudad: str) -> List[str]:
    """
    Busca sistemas de bicicletas que contengan el nombre de la ciudad especificada.

    Args:
        ciudad (str): Nombre de la ciudad a buscar

    Returns:
        List[str]: Lista de sistemas que coinciden con la búsqueda
    """

    """
    Ejemplo de sistema qu devuelve, hemos de iterar en cada instance para busca el meta.
    una vez tenemos meta, buscamos la city y comparamos.
    SISTEMA: {'instances': [{'tag': 'bicing', 'endpoint': 'https://www.bicing.barcelona', 'meta': {'country': 'ES', 'city': 'Barcelona', 'name': 'Bicing', 'latitude': 41.3850639, 'longitude': 2.1734035, 'company': ['Barcelona de Serveis Municipals, S.A. (BSM)', 'CESPA', 'PBSC']}}, {'tag': 'biki', 'endpoint': 'https://biki-valladolid.es/es', 'bbox': [[41.4602, -5.0492], [41.8421, -4.3764]], 'meta': {'country': 'ES', 'city': 'Valladolid', 'name': 'BIKI', 'latitude': 41.6522, 'longitude': -4.7243, 'company': ['Autobuses Urbanos de Valladolid S.A']}}], 'system': 'bicing', 'class': 'Bicing'}
    """
    # Implementa aquí la lógica para buscar y devolver sistemas
    # que coincidan con la ciudad especificada
    #pass
    lista_sistemas_en_ciudad = []
    lista_schemas = pybikes.get_schemas()
    for schema in lista_schemas:
        try:
            sistema = pybikes.get_data(schema)
            # Check que el sistema exista y que tenga el tag json instance ya que si no , no sirve de nada iterar.
            if sistema is None or sistema.get('instances', None) is None:
                continue
            for instance in sistema['instances']:
                meta = instance.get('meta',None)
                if meta is None:
                    continue
                meta_ciudad = meta.get('city',None)
                if meta_ciudad is None:
                    continue
                # En lma api viene la ciudad con la primera en mayuscula, convierto los dos strings en minuscula 
                if meta_ciudad.lower() == ciudad.lower():
                    #print(f"SISTEMA: {sistema}")
                    lista_sistemas_en_ciudad.append(schema)
                #print(f"META: {meta}\n")
            #print(f"SISTEMA: {sistema}\n")
            
            #print(f"sdasdasdasdasda {sistema}\n")
        except pybikes.PackageNotFoundError as e:
#        except Exception as e:
            # Los que den excepcion los ignoramos
            print(f"EXCEPCION {e}\n")
            continue
    #lista_sistemas_en_ciudad = pybikes.
    return lista_sistemas_en_ciudad

def obtener_info_sistema(tag: str) -> Dict[str, Any]:
    """
    Obtiene la información del sistema especificado.

    Args:
        tag (str): Identificador del sistema (por ejemplo, 'bicing')

    Returns:
        Dict[str, Any]: Metadatos del sistema o None si no existe
    """
    # Implementa aquí la lógica para obtener y devolver
    # los metadatos del sistema especificado
    #pass
    info_sistema = {}
    try:
        sistema = pybikes.get(tag)
        if sistema is None:
            return None
        info_sistema = sistema.meta
    except pybikes.exceptions.BikeShareSystemNotFound as e:
        return None
    return info_sistema


def obtener_estaciones(tag: str) -> Optional[List]:
    """
    Obtiene la lista de estaciones del sistema especificado.

    Args:
        tag (str): Identificador del sistema (por ejemplo, 'bicing')

    Returns:
        Optional[List]: Lista de objetos estación o None si hay error
    """
    # Implementa aquí la lógica para obtener y devolver
    # la lista de estaciones del sistema especificado
    lista_estaciones = []
    try:
        sistema = pybikes.get(tag)
        if sistema is None:
            return None
        #Segun la api , una vez se tiene el sistema hay que hacer un update para obtener las estaciones.
        sistema.update()
        lista_estaciones = sistema.stations
    except pybikes.exceptions.BikeShareSystemNotFound as e:
        return None
    except Exception as e:
        return None
    return lista_estaciones


def crear_dataframe_estaciones(estaciones: List) -> pd.DataFrame:
    """
    Convierte la lista de estaciones en un DataFrame de pandas.

    Args:
        estaciones (List): Lista de objetos estación

    Returns:
        pd.DataFrame: DataFrame con la información de las estaciones
    """
    # Implementa aquí la lógica para convertir la lista de estaciones
    # en un DataFrame de pandas con al menos las columnas:
    # nombre, latitud, longitud, bicicletas disponibles, espacios libres
    #pass

    lista_dict_estaciones = []
    for estacion in estaciones:
        dict_estacion = {}
        dict_estacion['name'] = estacion.name
        #position = estacion.latlng.split(',')
        dict_estacion['latitude'] = estacion.latitude
        dict_estacion['longitude'] = estacion.longitude
        dict_estacion['bikes'] = estacion.bikes
        dict_estacion['free'] =  estacion.free
        lista_dict_estaciones.append(dict_estacion)
#        print(f"ESTACION: {estacion} \n \n")
#        print(f"Dataframe: {estaciones}\n")
    df = pd.DataFrame(lista_dict_estaciones)
    return df


def visualizar_estaciones(df: pd.DataFrame) -> None:
    """
    Genera una visualización simple de la disponibilidad de bicicletas.

    Args:
        df (pd.DataFrame): DataFrame con la información de las estaciones
    """
    # Implementa aquí la lógica para crear un gráfico de barras que muestre
    # las 10 estaciones con más bicicletas disponibles
    #pass
    # Ordenamos el dataFrame por bikes de forma Descendente
    df_sorted = df.sort_values(by=['bikes'],axis= 0, ascending = False)
    # Obtenemos los 10 primeros
    df_top_ten = df_sorted.head(10)
    print(f"DASDAS\n {df_top_ten}\n")
    ax = df_top_ten.plot(kind= 'barh', title='Disponibilidad de Bicicletas', x= 'name', y = 'bikes')
    plt.show()
    #ax = df_top_ten.plot.bar(x='name', y = 'bikes', rot = 0)
    #ax.set_xlabel("name")
    #ax.set_ylabel("bikes")
    # Tenemos las figuras configuradas asi que forzamos el plot.
    #plt.show()


if __name__ == "__main__":

    print(f"ASDASDASDASDAS: {obtener_estaciones("sistema_inexistente")}\n\n")
    # Listar sistemas disponibles
    print("\nSistemas de bicicletas disponibles:")
    sistemas = listar_sistemas_disponibles()
    print(f"Total: {len(sistemas)} sistemas")
    print(f"Algunos ejemplos: {sistemas[:5]}")

    # Buscar sistemas en Barcelona
    print("\nBuscando sistemas en Barcelona:")
    sistemas_barcelona = buscar_sistema_por_ciudad("Barcelona")
    print(f"Encontrados: {len(sistemas_barcelona)}")
    for sistema in sistemas_barcelona:
        print(f"- {sistema}")

    # Si se encuentra el sistema de Barcelona (Bicing), obtener información
    if "bicing" in sistemas:
        print("\nInformación del sistema Bicing de Barcelona:")
        info = obtener_info_sistema("bicing")
        for key, value in info.items():
            print(f"{key}: {value}")

        # Obtener estaciones
        print("\nObteniendo estaciones...")
        estaciones = obtener_estaciones("bicing")
        if estaciones:
            print(f"Obtenidas {len(estaciones)} estaciones")

            # Convertir a DataFrame
            print("\nConvirtiendo a DataFrame...")
            df = crear_dataframe_estaciones(estaciones)
            print(df.head())

            # Estadísticas básicas
            print("\nEstadísticas de bicicletas disponibles:")
            print(df['bikes'].describe())

            # Visualización
            print("\nVisualizando estaciones con más bicicletas disponibles...")
            visualizar_estaciones(df)
        else:
            print("No se pudieron obtener las estaciones.")
    else:
        print("El sistema 'bicing' no está disponible en pybikes.")


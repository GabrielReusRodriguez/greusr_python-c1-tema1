"""
Enunciado:
Desarrolla una API REST utilizando Flask que permita realizar operaciones básicas sobre una lista de tareas (to-do list).
La API debe exponer los siguientes endpoints:

1. `GET /tasks`: Devuelve la lista completa de tareas.
2. `POST /tasks`: Agrega una nueva tarea. El cuerpo de la solicitud debe incluir un JSON con el campo "name".
3. `DELETE /tasks/<task_id>`: Elimina una tarea específica por su ID.

Requisitos:
- Cada tarea debe tener un ID único (entero) y un nombre (cadena de texto).
- La lista de tareas debe almacenarse en memoria (no es necesario usar una base de datos).
- Maneja errores como intentar eliminar una tarea que no existe.

Ejemplo:
Si la lista de tareas inicial está vacía:
1. Una solicitud `POST /tasks` con el cuerpo `{"name": "Comprar leche"}` debe agregar la tarea con ID 1.
2. Una solicitud `GET /tasks` debe devolver `[{"id": 1, "name": "Comprar leche"}]`.
3. Una solicitud `DELETE /tasks/1` debe eliminar la tarea con ID 1.
4. Una solicitud `GET /tasks` debe devolver `[]`.

Tu tarea es implementar esta API en Flask.
"""

from flask import Flask, jsonify, request

# Esta lista almacenará todas las tareas
tasks = []
# Este contador se usará para asignar IDs únicos
next_id = 1

def create_app():
    """
    Crea y configura la aplicación Flask
    """
    app = Flask(__name__)

    @app.route('/tasks', methods=['GET'])
    def get_tasks():
        """
        Devuelve la lista completa de tareas
        """
        # Implementa este endpoint
        pass

    @app.route('/tasks', methods=['POST'])
    def add_task():
        """
        Agrega una nueva tarea
        El cuerpo de la solicitud debe incluir un JSON con el campo "name"
        """
        # Implementa este endpoint
        pass

    @app.route('/tasks/<int:task_id>', methods=['DELETE'])
    def delete_task(task_id):
        """
        Elimina una tarea específica por su ID
        """
        # Implementa este endpoint
        pass

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
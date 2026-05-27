from flask import Flask

app = Flask(__name__)

tareas = [
    {"id": 1, "nombre": "Estudiar Python", "completada": False},
    {"id": 2, "nombre": "Hacer tarea de HTML", "completada": True}
]

@app.route("/")
def inicio():
    return tareas

app.run(debug=True)
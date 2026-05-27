from flask import Flask, request

app = Flask(__name__)

# Lista donde guardamos las tareas
tareas = [
    {"id": 1, "nombre": "Estudiar Python", "completada": False},
    {"id": 2, "nombre": "Aprender Flask", "completada": True}
]

# Página principal
@app.route("/")
def inicio():

    html = """
    <h1>📋 Sistema de Tareas</h1>

    <h2>Agregar nueva tarea</h2>

    <form action="/agregar" method="POST">
        <input type="text" name="tarea" placeholder="Escribe una tarea">
        <button type="submit">Agregar</button>
    </form>

    <hr>

    <h2>Lista de tareas</h2>
    """

    # Mostrar tareas
    for tarea in tareas:

        estado = "✅ Completada" if tarea["completada"] else "❌ Pendiente"

        html += f"""
        <div style="
            border:1px solid gray;
            padding:10px;
            margin:10px;
            border-radius:10px;
        ">
            <h3>{tarea["nombre"]}</h3>
            <p>ID: {tarea["id"]}</p>
            <p>Estado: {estado}</p>
        </div>
        """

    return html


# Ruta para agregar tareas
@app.route("/agregar", methods=["POST"])
def agregar_tarea():

    nombre_tarea = request.form["tarea"]

    nueva_tarea = {
        "id": len(tareas) + 1,
        "nombre": nombre_tarea,
        "completada": False
    }

    tareas.append(nueva_tarea)

    return f"""
    <h2>✅ Tarea agregada</h2>

    <p>{nombre_tarea}</p>

    <a href="/">Volver</a>
    """


app.run(debug=True)
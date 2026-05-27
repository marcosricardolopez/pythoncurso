from flask import Flask, request, redirect

app = Flask(__name__)

tareas = [
    {"id": 1, "nombre": "Estudiar Python", "completada": False},
    {"id": 2, "nombre": "Aprender Flask", "completada": True}
]

@app.route("/")
def inicio():
    html = """
    <h1>📋 Sistema de Tareas</h1>

    <form action="/agregar" method="POST">
        <input type="text" name="tarea" placeholder="Escribe una tarea">
        <button type="submit">Agregar</button>
    </form>

    <hr>
    <h2>Lista de tareas</h2>
    """

    for tarea in tareas:
        estado = "✅ Completada" if tarea["completada"] else "❌ Pendiente"
        texto_boton = "Marcar pendiente" if tarea["completada"] else "Marcar completada"

        html += f"""
        <div style="border:1px solid gray; padding:10px; margin:10px; border-radius:10px;">
            <h3>{tarea["nombre"]}</h3>
            <p>ID: {tarea["id"]}</p>
            <p>Estado: {estado}</p>

            <form action="/cambiar/{tarea["id"]}" method="POST">
                <button type="submit">{texto_boton}</button>
            </form>
        </div>
        """

    return html


@app.route("/agregar", methods=["POST"])
def agregar_tarea():
    nombre_tarea = request.form["tarea"]

    nueva_tarea = {
        "id": len(tareas) + 1,
        "nombre": nombre_tarea,
        "completada": False
    }

    tareas.append(nueva_tarea)

    return redirect("/")


@app.route("/cambiar/<int:id_tarea>", methods=["POST"])
def cambiar_estado(id_tarea):
    for tarea in tareas:
        if tarea["id"] == id_tarea:
            tarea["completada"] = not tarea["completada"]

    return redirect("/")


app.run(debug=True)
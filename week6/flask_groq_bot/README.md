# Bot AI con Flask + Groq

Proyecto sencillo para crear un chatbot web usando Flask y Groq.

## 1. Crear API Key de Groq

Crea tu API key en Groq Console y guárdala.

## 2. Instalar dependencias

Abre PowerShell en la carpeta del proyecto y ejecuta:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## 3. Configurar tu API key

Copia el archivo `.env.example` y renómbralo a `.env`.

Luego edita `.env`:

```env
GROQ_API_KEY=tu_api_key_real_aqui
GROQ_MODEL=llama-3.1-8b-instant
```

## 4. Ejecutar Flask

```powershell
python app.py
```

Abre tu navegador en:

```text
http://127.0.0.1:5000
```

## Notas

- No subas tu archivo `.env` a GitHub.
- El modelo `llama-3.1-8b-instant` es rápido y ligero para pruebas.
- Puedes cambiar el modelo en el archivo `.env`.

from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

app = FastAPI(title="REST Countries Web App")

templates = Jinja2Templates(directory="templates")

BASE_URL = "https://restcountries.com/v3.1/name/"


def obtener_pais(nombre_pais: str):
    url = f"{BASE_URL}{nombre_pais}"

    response = requests.get(url, timeout=10, verify=False)
    response.raise_for_status()

    data = response.json()
    pais = data[0]

    nombre = pais.get("name", {}).get("common", "No disponible")
    nombre_oficial = pais.get("name", {}).get("official", "No disponible")
    capital = pais.get("capital", ["No disponible"])[0]
    region = pais.get("region", "No disponible")
    subregion = pais.get("subregion", "No disponible")
    poblacion = pais.get("population", 0)
    bandera = pais.get("flags", {}).get("png", "")
    mapa = pais.get("maps", {}).get("googleMaps", "")

    monedas = pais.get("currencies", {})
    moneda_lista = []

    for codigo, info in monedas.items():
        moneda_lista.append(f"{info.get('name')} ({codigo})")

    idiomas = pais.get("languages", {})
    idioma_lista = list(idiomas.values())

    return {
        "nombre": nombre,
        "nombre_oficial": nombre_oficial,
        "capital": capital,
        "region": region,
        "subregion": subregion,
        "poblacion": f"{poblacion:,}",
        "bandera": bandera,
        "mapa": mapa,
        "monedas": moneda_lista,
        "idiomas": idioma_lista
    }


@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(
        request,
        "index.html",
        {
            "pais": None,
            "error": None
        }
    )


@app.post("/buscar", response_class=HTMLResponse)
def buscar_pais(request: Request, nombre_pais: str = Form(...)):
    try:
        pais = obtener_pais(nombre_pais)

        return templates.TemplateResponse(
            request,
            "index.html",
            {
                "pais": pais,
                "error": None
            }
        )

    except requests.exceptions.RequestException:
        return templates.TemplateResponse(
            request,
            "index.html",
            {
                "pais": None,
                "error": "No se pudo encontrar el país o hubo un error con la API."
            }
        )

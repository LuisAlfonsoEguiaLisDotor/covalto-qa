import requests
import time

url = "https://rickandmortyapi.com/api/character"

# Tiempo de respuesta API
inicio = time.time()
respuesta = requests.get(url)
fin = time.time()

tiempo = (fin - inicio) * 1000

# Status Code
status = respuesta.status_code

datos = respuesta.json()
personajes = datos["results"]

vivos = 0
muertos = 0
tipos_correctos = True

for p in personajes:
    
    # Validacion vivos y muertos
    if p["status"] == "Alive":
        vivos = vivos + 1
    elif p["status"] == "Dead":
        muertos = muertos + 1
        
    # Validación de tipos de datos
    if type(p["id"]) != int:
        tipos_correctos = False
    if type(p["name"]) != str:
        tipos_correctos = False
    if type(p["status"]) != str:
        tipos_correctos = False

if tipos_correctos == True:
    resultado_tipos = "OK\nid: Int\nName: String\nStatus: String"
else:
    resultado_tipos = "Error en los tipos de datos"

print("Tiempo de respuesta:", round(tiempo, 2), "ms")
print("Status code:", status)
print("Vivos:", vivos)
print("Muertos:", muertos)
print("Tipo de datos:", resultado_tipos)
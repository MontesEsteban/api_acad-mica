import json
import urllib.request
import urllib.error
url = "http://127.0.0.1:8000/courses"
datos = {"name": "Redes", "credits": 0, "active": True}
peticion = urllib.request.Request(url, data=json.dumps(datos).encode(), headers={"Content-Type": "application/json"}, method="POST")
try:
    respuesta = urllib.request.urlopen(peticion)
    print("Estado:", respuesta.status)
except urllib.error.HTTPError as error:
    print("Estado:", error.code)
    print(error.read().decode())

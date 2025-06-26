from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

#--------------------------------------------------------------
@app.get("/")
def read_root():
    return {"mensaje": "¡Hola desde FastAPI!"}

#--------------------------------------------------------------
@app.get("/saludo/{nombre}")
def saludar(nombre: str):
    return {"saludo": f"Hola, {nombre}!"}

#--------------------------------------------------------------
@app.post("/enviar/{dato}")
def recibir_dato(dato: str):
    return {"respuesta": f"Me has enviado: {dato}"}

#--------------------------------------------------------------
class Persona(BaseModel):
    nombre: str
    cedula: str

@app.post("/registrar")
def registrar_persona(persona: Persona):
    return {
        "nombre_recibido": persona.nombre,
        "cedula_recibida": persona.cedula
    }

#--------------------------------------------------------------
class Numeros(BaseModel):
    lista: List[int]  # 👈 Aquí se asegura que todos los datos sean enteros

@app.post("/analizar-numeros")
def analizar_numeros(numeros: Numeros):
    datos = numeros.lista
    if not datos:
        return {"error": "La lista está vacía"}

    mayor = max(datos)
    menor = min(datos)
    promedio = sum(datos) / len(datos)

    return {
        "mayor": mayor,
        "menor": menor,
        "promedio": round(promedio, 2)
    }

# 👇 Esto es necesario para Railway
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000)

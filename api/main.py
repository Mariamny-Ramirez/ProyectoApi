from fastapi import FastAPI      #Se importa el framework para construir la API
from pydantic import BaseModel   # validar los datos de entrada que recibe la API 
from typing import List, Dict    # Se le dice a Python qué tipo de datos se espera (listas, diccionarios)
from .logica import encontrar_estados_equivalentes  # Se importa la función de logica.py, con el algoritmo de minimización

# Crear la instancia de FastAPI
app = FastAPI()

# Definir cómo se espera que lleguen los datos a la API (modelo de entrada)
class AutomataInput(BaseModel):
    estados: int
    finales: List[int]
    alfabeto: List[str]
    transiciones: Dict[int, Dict[str, int]]

# Ruta (endpoint) de la API que recibe los datos y devuelve los equivalentes
@app.post("/minimizar") # Se define la ruta de la API
def minimizar_automata(data: AutomataInput):
    equivalentes = encontrar_estados_equivalentes(
        data.estados,
        data.finales,
        data.transiciones,
        set(data.alfabeto)
    )
    #Se devuelve la respuesta en formato JSON
    return {"equivalentes": equivalentes}

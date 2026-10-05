from fastapi import FastAPI
from routes.estudiantes import router

app = FastAPI(title="Sistema Académico - Taller de Observabilidad")
app.include_router(router)

@app.get("/")
def inicio():
    return {"mensaje": "Sistema académico activo"}

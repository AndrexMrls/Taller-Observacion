# Taller de Observabilidad – Sistema Académico

Proyecto FastAPI preparado para el análisis de observabilidad y calidad.

## Ejecución

python -m pip install -r requirements.txt

python -m uvicorn main:app --reload

Swagger:
http://127.0.0.1:8000/docs

## Endpoints

- GET /estudiantes/
- GET /estudiantes/{id_estudiante}
- POST /estudiantes/

## Propósito académico

La aplicación contiene situaciones deliberadas que deben ser investigadas mediante pruebas controladas.

NO se proporciona una lista de los problemas. El estudiante debe encontrarlos, demostrar cada hallazgo con evidencia, explicar su posible causa e impacto y proponer una mejora técnica.

No subir credenciales, tokens, claves API ni contraseñas.

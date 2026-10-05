# Taller de Observabilidad: Identificación y Mitigación de Errores en API REST

Este proyecto documenta el proceso de auditoría y corrección de una API REST para la gestión de estudiantes (Sistema Académico)[cite: 4, 5]. El objetivo principal es identificar debilidades estructurales mediante el ciclo de Observar, Probar, Documentar, Analizar y Mejorar, garantizando que el sistema sea robusto ante escenarios de estrés, fallos de infraestructura y recepción de datos inválidos[cite: 5].

## Tecnologías Utilizadas
* **Lenguaje y Framework Web:** Python con FastAPI[cite: 7].
* **Persistencia de Datos:** Base de datos relacional SQLite (`academico.db`)[cite: 7].
* **Validación de Modelos:** Pydantic[cite: 13].
* **Pruebas y Documentación:** Swagger UI (`http://127.0.0.1:8000/docs`)[cite: 6].
* **Integración Externa:** Librería `requests`[cite: 9].

## Flujo de la Arquitectura
El procesamiento de las solicitudes dentro de la aplicación sigue este flujo secuencial: 
Cliente (Swagger UI / Postman) -> Endpoint FastAPI (Rutas / Controllers) -> Lógica de negocio (Servicios y validaciones) -> Base de datos (SQLite) / API externa (Requests) -> Respuesta (JSON / Código de estado HTTP)[cite: 7].

## Vulnerabilidades Identificadas y Mitigadas
La auditoría reveló cinco fallos críticos que comprometían la calidad y seguridad de la aplicación:

* **Falta de Timeout en API Externa (Hallazgo 01):** La comunicación con el servicio `jsonplaceholder.typicode.com` mediante `requests.get()` no contaba con un tiempo máximo de espera[cite: 9]. Esto exponía a los hilos de ejecución del servidor a quedarse esperando indefinidamente (DoS) en caso de latencia[cite: 10]. 
* **Fallo Crítico de Infraestructura (Hallazgo 02):** La aplicación devolvía un Error Interno (500) por la inexistencia de la tabla principal en la base de datos[cite: 10, 11]. Se corrigió garantizando la creación de la estructura con la instrucción `CREATE TABLE IF NOT EXISTS`[cite: 12].
* **Carencia de Validación Lógica (Hallazgo 3):** El sistema colapsaba (Error 500 en lugar de 422) al recibir datos de entrada inválidos, como nombres vacíos o semestres negativos[cite: 12]. La mejora consistió en utilizar la restricción `Field` de Pydantic[cite: 13].
* **Falsos Positivos HTTP (Hallazgo 4):** Al consultar el ID de un estudiante inexistente, la API retornaba un código de éxito (200 OK) en lugar de reportar el fallo[cite: 14, 15]. Se solucionó levantando explícitamente una excepción `HTTPException` con código 404[cite: 15].
* **Degradación de Rendimiento (Hallazgo 05):** El endpoint de consulta masiva saturaba la memoria RAM al utilizar la instrucción `SELECT *` y el método `.fetchall()` sin emplear parámetros de paginación[cite: 16, 17]. Se recomendó utilizar cláusulas `LIMIT` y `OFFSET`[cite: 17].

## Importancia de la Observabilidad
El análisis demostró que una apariencia de éxito frente al usuario puede ocultar cuellos de botella y fallos lógicos[cite: 18]. Al analizar las trazas de error (Tracebacks) y aplicar correctamente los códigos de estado HTTP, se facilita el mantenimiento preventivo y se evita el bloqueo total del sistema ante fallos externos[cite: 18, 21].

## Autor
* **Andrés Felipe Morales Pretel**
* **Programa:** Ingeniería de Sistemas
* **Institución:** Corporación Universitaria Remington
* **Repositorio:** [https://github.com/AndrexMrls/Taller-Observacion.git](https://github.com/AndrexMrls/Taller-Observacion.git)

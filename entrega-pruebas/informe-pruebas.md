Informe de pruebas — API Académica

Fecha: 29 de octubre de 2026

Tecnologías: FastAPI, SQLModel y SQLite

Servidor: http://127.0.0.1:8000

Herramienta: Swagger UI (/docs)

1\. Pruebas realizadas



Caso	Endpoint	Resultado esperado	Estado

P01	POST /courses	Crear curso: 201	Pendiente

P02	GET /courses	Listar cursos: 200	Pendiente

P03	GET /courses/{course\_id}	Consultar curso existente: 200	Pendiente

P04	PUT /courses/{course\_id}	Actualizar curso: 200, mismo ID	Aprobado

P05	DELETE /courses/{course\_id}	Eliminar curso: 200	Pendiente

P06	POST /students	Crear estudiante: 201	Aprobado

P07	GET /students	Listar estudiantes: 200	Aprobado

P08	GET /students/{student\_id}	Consultar estudiante: 200	Aprobado

P09	GET /students/99999	Estudiante inexistente: 404	Aprobado

P10	POST /students	Semestre 11: 422	Aprobado

P11	GET /students/abc	ID inválido: 422	Aprobado

P12	Persistencia	Datos conservados tras reiniciar Uvicorn	Aprobado

Nota: Los estados deben reflejar las pruebas realmente ejecutadas. Cambia «Pendiente» por «Aprobado» únicamente después de comprobar cada caso.



2\. Persistencia

Se detuvo y reinició Uvicorn. Se consultaron nuevamente los estudiantes y cursos para comprobar que los registros permanecen en SQLite.



3\. Arquitectura

models/: modelos de las tablas.

schemas/: validación de entrada y salida.

services/: lógica de negocio y persistencia.

routers/: endpoints HTTP.

database/: conexión y sesiones SQLite.

main.py: configuración de FastAPI y registro de routers.

4\. Evidencias

Guardar las capturas reales de Swagger en entrega-pruebas/evidencias/, mostrando el endpoint, los datos enviados, el código HTTP y la respuesta obtenida.



5\. Conclusión

La API incorpora operaciones CRUD para Courses y operaciones de creación y consulta para Students. Las pruebas documentadas permiten verificar validaciones, manejo de errores y persistencia de los datos.


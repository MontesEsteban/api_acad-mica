API Académica

API REST educativa desarrollada con FastAPI, SQLModel, Pydantic y SQLite. Permite gestionar cursos académicos y registrar y consultar estudiantes, con validación de datos y respuestas HTTP apropiadas.

Funcionalidades
Crear, listar, consultar, actualizar y eliminar cursos.
Registrar estudiantes, listar todos los estudiantes y consultar uno por su identificador.
Validar los datos de entrada mediante esquemas Pydantic.
Utilizar SQLite para almacenar los registros.
Documentar y probar los endpoints mediante Swagger.
Responder con códigos HTTP según el resultado de cada operación.
Tecnologías
Herramienta	Uso
Python 3.12	Lenguaje de programación
FastAPI	Desarrollo de la API REST
Uvicorn	Servidor de desarrollo
SQLModel	Modelos y acceso a la base de datos
Pydantic	Validación de datos
SQLite	Persistencia de registros

Las dependencias y sus versiones se encuentran en requirements.txt.

Instalación y ejecución

Abre PowerShell en la carpeta raíz del proyecto, donde se encuentra main.py.

1. Crear y activar el entorno virtual

En Windows PowerShell:

powershell
python -m venv venv
.\venv\Scripts\Activate.ps1


Si el entorno virtual ya existe, solo tienes que activarlo.

2. Instalar las dependencias
powershell
python -m pip install -r requirements.txt

3. Iniciar la API
powershell
python -m uvicorn main:app --reload --host 127.0.0.1 --port 8000


La opción --reload permite recargar la aplicación cuando se modifican los archivos durante el desarrollo. Para detener el servidor, presiona Ctrl + C.

4. Abrir Swagger

Con el servidor activo, visita:

Documentación interactiva: http://127.0.0.1:8000/docs
Esquema OpenAPI: http://127.0.0.1:8000/openapi.json

Desde Swagger puedes seleccionar un endpoint, pulsar Try it out, introducir los datos y ejecutar la petición.

Endpoints de cursos
Método	Ruta	Operación	Respuesta esperada
POST	/courses	Crear un curso	201 Created
GET	/courses	Listar cursos	200 OK
GET	/courses/{course_id}	Consultar un curso por ID	200 OK
PUT	/courses/{course_id}	Actualizar un curso existente	200 OK
DELETE	/courses/{course_id}	Eliminar un curso existente	200 OK
Endpoints de estudiantes
Método	Ruta	Operación	Respuesta esperada
POST	/students	Registrar un estudiante	201 Created
GET	/students	Listar estudiantes	200 OK
GET	/students/{student_id}	Consultar un estudiante por ID	200 OK
Validación y errores HTTP
404 Not Found: el curso o estudiante solicitado no existe.
422 Unprocessable Entity: los datos enviados no cumplen las validaciones del esquema.
500 Internal Server Error: error inesperado del servidor que debe investigarse.
Reglas de entrada de cursos
Campo	Regla
name	Entre 3 y 80 caracteres
credits	Entero entre 1 y 6
active	Booleano; valor predeterminado true

Los nombres de los cursos no son únicos en la versión actual. Es posible registrar dos cursos con el mismo nombre. Impedirlo requeriría establecer una regla adicional y coordinar la validación del servicio con una restricción en la base de datos.

Las reglas de validación de estudiantes dependen del esquema definido en schemas/student.py.

Ejemplo: crear un curso

Petición a POST /courses:

json
{
  "name": "Programación I",
  "credits": 3,
  "active": true
}


Ejemplo de respuesta:

json
{
  "id": 1,
  "name": "Programación I",
  "credits": 3,
  "active": true
}


El ID es ilustrativo: lo genera la base de datos. Utiliza el ID recibido en las consultas, actualizaciones y eliminaciones posteriores.

Estructura del proyecto
text
api_acad-mica/
├── main.py
├── database/
│   └── database.py
├── models/
│   ├── course.py
│   └── student.py
├── schemas/
│   ├── course.py
│   └── student.py
├── routers/
│   ├── courses.py
│   └── students.py
├── services/
│   ├── course_service.py
│   └── student_service.py
├── entrega-pruebas/
│   ├── informe-pruebas.md
│   └── evidencias/
├── requirements.txt
├── docs.md
└── README.md

Persistencia de datos

La aplicación utiliza SQLite. Las tablas se preparan al iniciar la aplicación mediante el ciclo de vida de FastAPI.

Para evitar confusiones con los archivos de base de datos, ejecuta Uvicorn desde la raíz del proyecto y verifica la configuración de conexión en database/database.py.

Pruebas y evidencias

Las pruebas de la API pueden realizarse desde Swagger o mediante solicitudes HTTP. La carpeta entrega-pruebas/ contiene el informe y las evidencias de verificación del proyecto.

Entre las comprobaciones realizadas se incluyen:

Creación y consulta de cursos.
Actualización y eliminación de cursos.
Consulta de estudiantes.
Validación de créditos fuera del rango permitido.
Respuesta 404 al consultar un recurso inexistente.

Los resultados y las capturas deben corresponder a las pruebas efectivamente ejecutadas.

Flujo de una petición

Cliente HTTP → router de FastAPI → validación Pydantic → servicio → sesión SQLModel → SQLite → respuesta HTTP.

Consulta docs.md para ampliar la explicación del proyecto y sus componentes.
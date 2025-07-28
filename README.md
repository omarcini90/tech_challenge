# Tech Challenge
Desafío tecnológico para reclutamiento

## Propósito

Desarrollo de chatbot que mantiene su postura firme con base en un tema ingresado por el usuario, sin importar que tan logico o irracional sea la postura. La respuesta entrega un historico de los ultimos 5 menesajes de ambas partes para poder darle continuidad a la conversación. 

## Estructura del proyecto


```
tech_challenge/
├── api/
│   ├── main.py                # Punto de entrada FastAPI
│   ├── requirements.txt       # Dependencias Python
│   ├── router/                # Rutas de la API
│   ├── business_logic/        # Lógica de negocio
│   ├── models/                # Modelos de datos
│   ├── schemas/               # Esquemas Pydantic
│   ├── utils/                 # Utilidades y helpers
│   └── ...
├── tests/                     # Pruebas automatizadas
├── Dockerfile                 # Imagen de la API
├── docker-compose.yml         # Orquestación de servicios
├── Makefile                   # Comandos de automatización
├── .env                       # Variables de entorno
└── README.md                  # Documentación
```

## Ejemplo de archivo .env

```
MONGO_URI=mongodb://mongo:27017
MONGO_DB_NAME=tech_challenge
OPENAI_API_KEY=tu_clave_openai
OPENAI_MODEL=gpt-3.5-turbo
```

## Contribuir

Instrucciones para contribuir, abrir issues o enviar pull requests.

## Preguntas frecuentes (FAQ)

- **¿Qué hago si Docker no inicia?**
  - Revisa que Docker Desktop esté corriendo o ejecuta `sudo systemctl start docker` en Linux.
- **¿Cómo cambio la configuración de la base de datos?**
  - Modifica el archivo `.env` y reinicia los servicios.

## Requisitos previos

- Python 3.10+ (recomendado 3.11 o superior) para poder probar de forma local
- pip (gestor de paquetes de Python)
- Docker y Docker Compose (para levantar servicios en contenedores)

### Instalación de requisitos

1. **Python y pip:**
   - macOS: `brew install python`
   - Ubuntu: `sudo apt-get install python3 python3-pip`
2. **Docker y Docker Compose:**
   - macOS: [Descargar Docker Desktop](https://www.docker.com/products/docker-desktop/)
   - Ubuntu: [Guía oficial](https://docs.docker.com/engine/install/ubuntu/)

## Uso del Makefile

El proyecto incluye un `Makefile` para facilitar las tareas comunes:

- `make help`: Muestra todos los comandos disponibles.
- `make install`: Instala los requisitos de Python definidos en `api/requirements.txt`.
- `make test`: Ejecuta los tests del proyecto usando pytest.
- `make run`: Levanta el servicio principal y dependencias (como la base de datos) usando Docker Compose.
- `make down`: Detiene los servicios levantados por Docker Compose.
- `make clean`: Elimina todos los contenedores y volúmenes de Docker relacionados.

### Ejemplo de uso

```sh
make install   # Instala dependencias Python
make test      # Ejecuta los tests
make run       # Levanta la app y la base de datos en Docker
make down      # Detiene los servicios
make clean     # Limpia contenedores y volúmenes
```

## Variables de entorno

Debes configurar las siguientes variables de entorno para el correcto funcionamiento del servicio (puedes usar un archivo `.env`):

- `MONGO_URI`: URI de conexión a MongoDB (ejemplo: `mongodb://mongo:27017`)
- `OPENAI_API_KEY`: Clave de API para el servicio de OpenAI (si aplica)


## Documentación interactiva

Puedes visualizar la documentación de la API generada automáticamente por FastAPI en:


Puedes visualizar la documentación de la API generada automáticamente por FastAPI en:

- Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- Redoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

## Documentación de los servicios

### API principal

- `GET /conversation/{conversation_id}`: Obtiene todos los mensajes de una conversación específica.


#### Ejemplo de request para `/chat`

```json
{
  "conversation_id": "abc123",
  "message": "Hola"
}
```

#### Ejemplo de response

```json
{
  "conversation_id": "abc123",
  "message": [
    {
      "rol": "user",
      "message": "Hola"
    },
    {
      "rol": "assistant",
      "message": "¡Hola! ¿En qué puedo ayudarte?"
    }
  ]
}
```

### Servicios relacionados

- **MongoDB**: Base de datos para almacenar las conversaciones y mensajes.
- **OpenAI**: Servicio externo para generar respuestas automáticas (si está configurado).


## Pruebas

Las pruebas se ejecutan dentro de los contenedores Docker usando el Makefile. No es necesario instalar dependencias localmente ni ejecutar comandos fuera de Docker.

- Para ejecutar los tests, usa:

```sh
make test
```

Esto construirá la imagen si es necesario y correrá los tests en el entorno Docker, asegurando que todo funcione igual que en producción.

---
Para dudas o problemas, consulta el código fuente o abre un issue.

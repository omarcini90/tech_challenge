# tech_challenge
Desafío tecnológico para reclutamiento

## Requisitos previos

- Python 3.10+ (recomendado 3.11 o superior)
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

- `MONGO_URI`: URI de conexión a MongoDB (ejemplo: `mongodb://localhost:27017`)
- `OPENAI_API_KEY`: Clave de API para el servicio de OpenAI (si aplica)


## Documentación interactiva

Puedes visualizar la documentación de la API generada automáticamente por FastAPI en:

- Swagger UI: [http://localhost:8000/docs](http://localhost:8000/docs)
- Redoc: [http://localhost:8000/redoc](http://localhost:8000/redoc)

## Documentación de los servicios

### API principal

El servicio expone endpoints para gestionar conversaciones y mensajes de chat. Los principales endpoints son:

- `POST /chat`: Envía un mensaje y recibe una respuesta del asistente.
- `GET /conversation/{conversation_id}`: Obtiene todos los mensajes de una conversación específica.

#### Ejemplo de request para `/chat`

```json
{
  "conversation_id": "abc123",
  "prompt": "Hola"
}
```

#### Ejemplo de response

```json
{
  "conversation_id": "abc123",
  "response": "¡Hola! ¿En qué puedo ayudarte?"
}
```

### Servicios relacionados

- **MongoDB**: Base de datos para almacenar las conversaciones y mensajes.
- **OpenAI**: Servicio externo para generar respuestas automáticas (si está configurado).

## Pruebas

Las pruebas están en la carpeta `tests/`. Se ejecutan con `make test` o manualmente con:

```sh
PYTHONPATH=. pytest
```

---
Para dudas o problemas, consulta el código fuente o abre un issue.

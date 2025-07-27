import os
from types import SimpleNamespace
from dotenv import load_dotenv

# Cargar las variables de entorno desde el archivo .env
load_dotenv()
 
#Configuración de variables de entorno.
settings = {
    "MONGO_URI": os.getenv("MONGO_URI"),
    "MONGO_DB_NAME": os.getenv("MONGO_DB_NAME"),
    "OPENAI_API_KEY": os.getenv("OPENAI_API_KEY"),
    "OPENAI_MODEL": os.getenv("OPENAI_MODEL", "gpt-3.5-turbo"),
    "GEMINI_API_KEY": os.getenv("GEMINI_API_KEY"),
    "GEMINI_MODEL": os.getenv("GEMINI_MODEL", "gemini-1.5-flash")
}

settings = SimpleNamespace(**settings)
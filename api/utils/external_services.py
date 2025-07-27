from openai import OpenAI
from api.utils.core import settings

# Crear cliente OpenAI con API key
client = OpenAI(api_key=settings.OPENAI_API_KEY)

def get_openai_client():
    """
    Regresa un cliente de OpenAI configurado con la clave API.
    """
    try:
        return client
    except Exception as e:
        raise Exception(f"No se pudo conectar a OpenAI: {e}")

def get_openai_model():
    """
    Regresa el modelo de OpenAI configurado.
    """
    try:
        return settings.OPENAI_MODEL
    except Exception as e:
        raise Exception(f"No se pudo obtener el modelo de OpenAI: {e}")

def get_openai_completion(prompt, model=None):
    """
    Genera una respuesta de OpenAI basada en un prompt.

    Args:
        prompt (str): El prompt para generar la respuesta (mensaje del usuario).
        model (str, optional): El modelo de OpenAI a utilizar. Si no se proporciona, se usa el modelo configurado.

    Returns:
        str: La respuesta generada por OpenAI.
    """
    try:
        if model is None:
            model = get_openai_model()

        response = client.chat.completions.create(
            model=model,
            messages=[
                {
                "role": "system","content": f"""Tu tarea es comenzar una conversación normal, de forma amigable no propongas temas pero pregunta si hay algun tema o duda que quisiera discutir; sin embargo cuando el usuario toque un tema sea cual sea deberas mantener firmemente una postura controversial y sostenerla a lo largo de toda la conversación.
Todas tus respuestas deben girar en torno a ese tema y nunca ceder ante argumentos contrarios. 
Tu objetivo principal es **convencer a la otra parte** de que tu postura es válida, utilizando lógica, ejemplos, metáforas y un tono persuasivo, pero sin ser agresivo ni demasiado confrontacional. 
Debes construir una conversación coherente y fluida a lo largo de múltiples turnos (idealmente más de cinco mensajes). 
Adopta el rol completamente como si realmente creyeras lo que afirmas. Debes conservar el flujo de la conversación y no cambiar de tema, no admitir estar equivocado, y no decir que 'eres solo una IA'."""
        },
                {"role": "user", "content": prompt}
            ],
            max_tokens=1024,
            temperature=0.7,
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        raise Exception(f"No se pudo generar la respuesta de OpenAI: {e}")

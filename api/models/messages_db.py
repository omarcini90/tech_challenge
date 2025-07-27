import uuid
import datetime
from api.utils.config import get_mongo_client, insert_document, find_documents, update_document



def insert_message(message,conversation_id=None,rol="user"):
    """
    Inserta un mensaje en la colección de MongoDB.
    Si conversation_id es None, se genera uno nuevo.
    Args:
        message (str): El contenido del mensaje.
        conversation_id (str, optional): El ID de la conversación. Si es None, se genera uno nuevo.
    Returns:
        str: El ID del documento insertado.
    """
    client = get_mongo_client()
    db = client['tech_challenge']
    collection = db['messages']
    
    document = {
        "conversation_id": conversation_id,
        "message": message,
        "rol": rol
    }
    if not conversation_id:
        document["conversation_id"] = str(uuid.uuid4())
    document["timestamp"] = datetime.datetime.now()
    result=insert_document('messages', document)
    if result:
        return {"conversation_id": document["conversation_id"]}
    else:
        result = {"conversation_id": None}
    return result

def get_messages(conversation_id):
    """
    Regresa los mensajes de una conversación específica.
    Args:
        conversation_id (str): El ID de la conversación.
    Returns:
        dict: Un diccionario que contiene el ID de la conversación y una lista de mensajes.
        Si no se encuentran mensajes, regresa None.
    """
    query = {"conversation_id": conversation_id}
    documents = find_documents('messages', query)
    
    if not documents:
        return None
    
    messages = []
    #limitar a los ultimos 5 mensajes de ambos roles (user, assistant)
    num_messages = 0
    user=False
    assistant=False
    #Ordenar los mensajes por timestamp del mas reciente al mas antiguo
    documents.sort(key=lambda x: x.get("timestamp", datetime.datetime.now()), reverse=True)
    for doc in documents:
        messages.append({
            "rol": doc.get("rol", "user"),
            "message": doc.get("message", ""),
            "timestamp": doc.get("timestamp", datetime.datetime.now()).isoformat()
        })
        # detectar si ya agrego mensaje de ambos roles
        if doc.get("rol") == "assistant":
            assistant=True
        if doc.get("rol") == "user":
            user=True
        if user and assistant:
            num_messages += 1
            user=False
            assistant=False
        if num_messages >= 5:
            break
    return {
        "conversation_id": conversation_id,
        "messages": messages
    }
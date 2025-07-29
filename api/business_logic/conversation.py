from api.models.messages_db import insert_message, get_messages
from api.utils.external_services import get_openai_completion
from api.schemas.messages import MessageRequest, MessageResponse, MessageResponseItem
from fastapi import HTTPException,status


class ConversationLogic():
    """
    Clase que maneja la lógica de negocio relacionada con las conversaciones.
    
    """
    def __init__(self):
        """
        Inicializa la clase ConversationLogic.
        """
        pass
    
    def get_response_from_openai(self, conversation_id: str, conversation_history: list) -> str:
        """
        Obtiene una respuesta de OpenAI para un prompt dado.
        conversation_history debe ser una lista de mensajes tipo [{"rol": ..., "message": ...}]
        """
        # Solo pasar la lista de mensajes a get_openai_completion
        response = get_openai_completion(conversation_history)
        if not response:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error al obtener respuesta de OpenAI")
        if conversation_id is None:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Conversation ID cannot be None")
        insert_message(response, conversation_id, rol="assistant")
        return response

    def create_message(self,message_request: MessageRequest) -> MessageResponse:
        """
        Crea un mensaje y lo inserta en la base de datos.
        """
        try:
            conversation_data = get_messages(message_request.conversation_id)
            message_id = insert_message(message_request.message, message_request.conversation_id, rol="user")
            if not message_id or "conversation_id" not in message_id:
                raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error inserting message")
            if message_request.conversation_id is None:
                conversation_id = message_id["conversation_id"]
            else:
                conversation_id = message_request.conversation_id
            # Extraer solo la lista de mensajes
            if conversation_data and "messages" in conversation_data:
                conversation_history = conversation_data["messages"]
            else:
                conversation_history = [{"rol": "user", "message": message_request.message}]
            self.get_response_from_openai(conversation_id, conversation_history)
            # Obtener los mensajes de la conversación
            messages= get_messages(conversation_id)
            if not messages:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Conversation not found")
            #iterar sobre los mensajes y crear una lista de MessageResponseItem
            message_items = [
                MessageResponseItem(rol=msg["rol"], message=msg["message"]) for msg in messages["messages"]
            ]
            return MessageResponse(
                conversation_id=messages["conversation_id"],
                message=message_items
            )

        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

    def get_conversation_messages(self, conversation_id: str) -> MessageResponse:
        """
        Obtiene los mensajes de una conversación específica.
        """
        messages = get_messages(conversation_id)
        if not messages:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Conversation not found")
        
        message_items = [
            MessageResponseItem(rol=msg["rol"], message=msg["message"]) for msg in messages["messages"]
        ]
        return MessageResponse(
            conversation_id=messages["conversation_id"],
            message=message_items
        )

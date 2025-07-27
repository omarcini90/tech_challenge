from api.business_logic.conversation import ConversationLogic
from api.schemas.messages import MessageRequest, MessageResponse
from fastapi import APIRouter, HTTPException, status

router = APIRouter()
conversation_logic = ConversationLogic()



@router.post("/chat", response_model=MessageResponse, status_code=status.HTTP_201_CREATED)
async def chat(message_request: MessageRequest):
    """
    Endpoint para crear un mensaje y obtener una respuesta de OpenAI.
    
    Args:
        message_request (MessageRequest): El esquema de solicitud del mensaje.
    
    Returns:
        MessageResponse: La respuesta del mensaje con la conversación y los mensajes.
    """
    try:
        return conversation_logic.create_message(message_request)
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

@router.get("/chat/{conversation_id}", response_model=MessageResponse)
async def get_conversation(conversation_id: str):
    """
    Endpoint para obtener los mensajes de una conversación específica.
    
    Args:
        conversation_id (str): El ID de la conversación.
    
    Returns:
        MessageResponse: La respuesta del mensaje con la conversación y los mensajes.
    """
    try:
        return conversation_logic.get_conversation_messages(conversation_id)
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
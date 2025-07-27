from pydantic import BaseModel, Field
from typing import Optional, List

# En este archivo se definen los esquemas de mensajes para la API. 
# Para validación de datos y documentación automática.


#Se define el esquema de solicitud del mensaje donde la conversación es opcional y el mensaje es obligatorio.
class MessageRequest(BaseModel):
    conversation_id: Optional[str] = Field(
        default=None,
        description="The ID of the conversation to which the message belongs."
    )
    message: str = Field(
        ...,
        description="The content of the message to be sent."
    )
# Se define el esquema de respuesta del mensaje donde se incluye el rol del remitente y el contenido del mensaje.
class MessageResponseItem(BaseModel):
    rol: str = Field(
        ...,
        description="The role of the message sender (e.g., 'user', 'assistant')."
    )
    message: str = Field(
        ...,
        description="The content of the message."
    )

# Se define el esquema de respuesta del mensaje que incluye el ID de la conversación y una lista de mensajes.
# Este esquema se utiliza para estructurar la respuesta de la API al cliente.
class MessageResponse(BaseModel):
    conversation_id: str = Field(
        ...,
        description="The ID of the conversation to which the message belongs."
    )
    message: List[MessageResponseItem] = Field(
        ...,
        description="A list of messages in the conversation."
    )
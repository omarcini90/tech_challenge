import pytest
from api.schemas.messages import MessageResponse
from api.business_logic.conversation import ConversationLogic

@pytest.fixture
def conversation_logic():
    return ConversationLogic()

def test_get_conversation_messages_found(monkeypatch, conversation_logic):
    # Simula la respuesta de get_messages
    def fake_get_messages(conversation_id):
        return {
            "conversation_id": conversation_id,
            "messages": [
                {"rol": "user", "message": "Hola"},
                {"rol": "assistant", "message": "¡Hola! ¿En qué puedo ayudarte?"}
            ]
        }
    monkeypatch.setattr("api.business_logic.conversation.get_messages", fake_get_messages)

    response = conversation_logic.get_conversation_messages("abc123")
    assert isinstance(response, MessageResponse)
    assert response.conversation_id == "abc123"
    assert len(response.message) == 2
    assert response.message[0].rol == "user"
    assert response.message[1].rol == "assistant"

def test_get_conversation_messages_not_found(monkeypatch, conversation_logic):
    def fake_get_messages(conversation_id):
        return None
    monkeypatch.setattr("api.business_logic.conversation.get_messages", fake_get_messages)

    with pytest.raises(Exception) as excinfo:
        conversation_logic.get_conversation_messages("noexiste")
    assert "Conversation not found" in str(excinfo.value)

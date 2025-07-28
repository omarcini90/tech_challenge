import pytest
from fastapi.testclient import TestClient
from fastapi import HTTPException
from api.main import app
from api.business_logic.conversation import ConversationLogic

client = TestClient(app)


# 🔹 Helper para validar estructura de respuesta
def assert_chat_response(data, conversation_id, user_message, assistant_message="¡Hola! ¿En qué puedo ayudarte?"):
    assert data["conversation_id"] == conversation_id
    assert isinstance(data["message"], list)
    assert len(data["message"]) == 2
    assert data["message"][0]["rol"] == "user"
    assert data["message"][0]["message"] == user_message
    assert data["message"][1]["rol"] == "assistant"
    assert data["message"][1]["message"] == assistant_message


# ✅ Test para POST /chat
@pytest.mark.parametrize("conversation_id,message", [
    ("abc123", "Hola"),
    ("xyz789", "¿Qué tal?")
])
def test_post_chat_creates_message(monkeypatch, conversation_id, message):
    def fake_create_message(self, message_request):
        return {
            "conversation_id": message_request.conversation_id or "abc123",
            "message": [
                {"rol": "user", "message": message_request.message},
                {"rol": "assistant", "message": "¡Hola! ¿En qué puedo ayudarte?"}
            ]
        }

    monkeypatch.setattr(ConversationLogic, "create_message", fake_create_message)

    payload = {"conversation_id": conversation_id, "message": message}
    response = client.post("/chat", json=payload)

    assert response.status_code == 201
    data = response.json()
    assert_chat_response(data, conversation_id, message)


# ✅ Test para GET /chat/{conversation_id}
def test_get_chat_conversation(monkeypatch):
    def fake_get_conversation_messages(self, conversation_id):
        return {
            "conversation_id": conversation_id,
            "message": [
                {"rol": "user", "message": "Hola"},
                {"rol": "assistant", "message": "¡Hola! ¿En qué puedo ayudarte?"}
            ]
        }

    monkeypatch.setattr(ConversationLogic, "get_conversation_messages", fake_get_conversation_messages)

    response = client.get("/chat/abc123")
    assert response.status_code == 200
    data = response.json()
    assert_chat_response(data, "abc123", "Hola")


# ✅ Test para errores en POST /chat
@pytest.mark.parametrize("payload,expected_status", [
    ({}, 422),  # Falta todo
    ({"conversation_id": "abc123"}, 422),  # Falta message
    ({"message": "Hola"}, 201)  # Se permite sin conversation_id
])
def test_post_chat_validation(payload, expected_status, monkeypatch):
    def fake_create_message(self, message_request):
        return {
            "conversation_id": message_request.conversation_id or "abc123",
            "message": [
                {"rol": "user", "message": message_request.message},
                {"rol": "assistant", "message": "¡Hola! ¿En qué puedo ayudarte?"}
            ]
        }

    monkeypatch.setattr(ConversationLogic, "create_message", fake_create_message)

    response = client.post("/chat", json=payload)
    assert response.status_code == expected_status


# ✅ Test para error en GET /chat cuando no existe conversación
def test_get_chat_not_found(monkeypatch):
    def fake_get_conversation_messages(self, conversation_id):
        raise HTTPException(status_code=404, detail="Conversation not found")

    monkeypatch.setattr(ConversationLogic, "get_conversation_messages", fake_get_conversation_messages)

    response = client.get("/chat/invalid-id")
    assert response.status_code == 404
    assert response.json()["detail"] == "Conversation not found"

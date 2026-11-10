import pytest

from unittest.mock import patch
from llm_client import analyse_requirement
from ollama import ResponseError

def test_ollama_connection_error():

    with patch("llm_client.chat") as mock_chat:

        mock_chat.side_effect = ConnectionError(
            "Ollama server unavailable"
        )

        with pytest.raises(ConnectionError):
            analyse_requirement(
                "You are a Business Analyst.",
                "Create one user story."
            )

def test_ollama_model_not_found():

    with patch("llm_client.chat") as mock_chat:

        mock_chat.side_effect = ResponseError(
            "Model not found",
            status_code=404
        )

        with pytest.raises(ResponseError) as error:
            analyse_requirement(
                "You are a Business Analyst.",
                "Create one user story."
            )

        assert error.value.status_code == 404

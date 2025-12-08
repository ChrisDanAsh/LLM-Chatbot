"""Model initialization for the agent."""

from langchain.chat_models import init_chat_model
from .config import settings


def get_model():
    # Initialize and return the chat model.
    model = init_chat_model(settings.CHAT_MODEL)

    return model

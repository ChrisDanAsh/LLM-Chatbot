"""Configuration settings for the LLM Chatbot."""

import os
from dotenv import load_dotenv

# Load variables from .env file
load_dotenv()


# Centralized configuration loader for environment variables.
# Provides a single place to access all required API keys and settings.
class Settings:
    # API keys
    LANGSMITH_TRACING: str = os.getenv("LANGSMITH_TRACING", "false")
    LANGSMITH_API_KEY: str = os.getenv("LANGSMITH_API_KEY")
    GOOGLE_API_KEY: str = os.getenv("GOOGLE_API_KEY")

    # Vectorstore settings
    DOC_PATH: str = "data/TT_Visa_FAQ.pdf"
    VECTORSTORE_DIR: str = "data/embeddings"

    # Model settings
    EMBEDDING_MODEL: str = "sentence-transformers/all-mpnet-base-v2"
    CHAT_MODEL: str = "google_genai:gemini-2.5-flash-lite"


settings = Settings()

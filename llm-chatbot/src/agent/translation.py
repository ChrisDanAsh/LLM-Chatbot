"""Translation functions for the agent using the chosen chat model."""

from .model import get_model

# Get shared model instance
model = get_model()


def detect_language(text: str) -> str:
    """Returns language code like 'en', 'es', 'de', 'fr', 'ko', ..."""
    prompt = f"""
    Detect the language of the following text and return only the language code (ISO-639-1):
    ---
    {text}
    """
    result = model.invoke(prompt)
    return result.content


def translate_to_english(text: str) -> str:
    prompt = f"""
    Translate the following text into English. Do not add commentary.
    ---
    {text}
    """
    return model.invoke(prompt).content


def translate_from_english(text: str, target_lang: str) -> str:
    prompt = f"""
    Translate the following English text into {target_lang}.
    Do not add commentary.
    ---
    {text}
    """
    return model.invoke(prompt).content

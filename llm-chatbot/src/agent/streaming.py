"""Streaming interface for multilingual agent responses."""

from agent.agent_builder import get_agent
from agent.translation import (
    detect_language,
    translate_to_english,
    translate_from_english,
)


def multilingual_agent_stream(query: str) -> str:
    """
    Handles language detection, translation, streaming agent output,
    and translation of the final answer back to the user's language.
    """

    # 1. Detect the user's input language
    user_lang = detect_language(query)

    # 2. Translate query to English if needed
    english_query = translate_to_english(query) if user_lang != "en" else query

    # 3. Stream the agent's English response
    agent = get_agent()
    english_fragments = []

    for step in agent.stream(
        {"messages": [{"role": "user", "content": english_query}]},
        stream_mode="values",
    ):
        # Ensure valid streamed content
        if "messages" in step and step["messages"]:
            msg = step["messages"][-1]
            # Only capture AI/assistant messages, not tool outputs
            if (
                hasattr(msg, "content")
                and isinstance(msg.content, str)
                and hasattr(msg, "type")
                and msg.type == "ai"  # Filter for AI responses only
            ):
                english_fragments.append(msg.content)

    english_answer = "".join(english_fragments).strip()

    # 4. If original user language was English, return directly
    if user_lang == "en":
        return english_answer

    # 5. Translate final answer from English back to user's language
    final_answer = translate_from_english(english_answer, user_lang).strip()

    return final_answer

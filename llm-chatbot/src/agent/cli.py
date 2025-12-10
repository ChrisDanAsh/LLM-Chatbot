"""Simple CLI application for testing the multilingual agent locally."""

from agent.streaming import multilingual_agent_stream
from agent.vectorstore import initialize_vectorstore


def run_cli():
    print("Welcome to the Multilingual TT Visa FAQ Chatbot")
    print("Initializing...\n")

    # Initialize vectorstore at startup
    initialize_vectorstore()
    print("Initialization complete. You can start chatting now.")
    print("\nType 'exit' or 'quit' to stop.\n")

    while True:
        user_input = input("You: ").strip()

        if user_input.lower() in {"exit", "quit"}:
            print("Goodbye!")
            break

        # Streaming output returned as a generator
        for chunk in multilingual_agent_stream(user_input):
            print(chunk, end="", flush=True)

        print("\n")  # Formatting

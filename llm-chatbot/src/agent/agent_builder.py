"Module to create the agent with tools."

from langchain.agents import create_agent

from .model import get_model
from .tools import retrieve_context


def get_agent():
    """
    Constructs and returns the agent with tool capabilities.
    The agent uses the shared model and the retrieval tool.
    """

    # 1. Load model
    model = get_model()

    # 2. Define the tools available to the agent
    tools = [retrieve_context]

    # 3. System instructions for how the agent should behave
    system_prompt = (
        "You are a helpful FAQ assistant for Trinidad and Tobago eVisa services. "
        "You have access to a tool that retrieves information from the official FAQ documentation. "
        "Use this tool when necessary to answer user questions accurately. "
        "\n"
        "IMPORTANT INSTRUCTIONS:\n"
        "- Extract ONLY the most relevant information from the retrieved context.\n"
        "- Provide a SHORT, direct answer (2-3 sentences maximum).\n"
        "- DO NOT repeat or include unnecessary details from the source documents.\n"
        "- DO NOT include document metadata, dates, or filenames.\n"
        "- If the answer requires a list, format it as bullet points.\n"
        "- Be concise and to the point."
    )

    # 4. Create and return the tool-enabled agent
    agent = create_agent(
        model=model,
        tools=tools,
        system_prompt=system_prompt,
    )

    return agent

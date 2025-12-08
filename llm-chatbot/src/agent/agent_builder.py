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
        "You have access to a tool that retrieves context from a blog post. "
        "Use this tool when necessary to help answer user queries accurately."
    )

    # 4. Create and return the tool-enabled agent
    agent = create_agent(
        model=model,
        tools=tools,
        system_prompt=system_prompt,
    )

    return agent

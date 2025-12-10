import pytest
from agent import __version__


# Version test
def test_version():
    """Test that version is set correctly."""
    assert __version__ == "0.1.0"


# CLI tests
def test_main_runs():
    """Test that the CLI entry point can be imported without error."""
    from agent.cli import run_cli

    # Just test that import works; don't actually run CLI
    # (running would block waiting for input)
    assert callable(run_cli)


# Configuration tests
def test_config_settings_exist():
    """Test that all required config settings are present."""
    from agent.config import settings

    assert hasattr(settings, "DOC_PATH")
    assert hasattr(settings, "VECTORSTORE_DIR")
    assert hasattr(settings, "EMBEDDING_MODEL")
    assert hasattr(settings, "CHAT_MODEL")


# Vectorstore tests (mark as slow since they load models)
@pytest.mark.slow
def test_vectorstore_initialization():
    """Test that vectorstore can be initialized."""
    from agent.vectorstore import initialize_vectorstore, get_vectorstore

    initialize_vectorstore()
    vectorstore = get_vectorstore()
    assert vectorstore is not None


# Model tests
@pytest.mark.slow
def test_model_initialization():
    """Test that the model can be initialized."""
    from agent.model import get_model

    model = get_model()
    assert model is not None


# Tools tests
@pytest.mark.slow
def test_retrieve_context_tool():
    """Test that retrieve_context tool works."""
    from agent.tools import retrieve_context
    from agent.vectorstore import initialize_vectorstore

    initialize_vectorstore()
    result = retrieve_context.invoke({"query": "visa requirements"})

    assert isinstance(result, str)
    assert len(result) > 0


# Integration test
@pytest.mark.slow
@pytest.mark.integration
def test_end_to_end_query():
    """Integration test: full query through the system."""
    from agent.vectorstore import initialize_vectorstore
    from agent.streaming import multilingual_agent_stream

    initialize_vectorstore()
    response = multilingual_agent_stream("Who can apply?")

    assert isinstance(response, str)
    assert len(response) > 10

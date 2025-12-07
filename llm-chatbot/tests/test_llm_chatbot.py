from llm_chatbot import __version__


def test_version():
    """Test that version is set correctly."""
    assert __version__ == "0.1.0"


def test_main_runs():
    """Test that main() can be called without error."""
    from llm_chatbot.__main__ import main

    # This will print to stdout; in real tests, capture output
    main()

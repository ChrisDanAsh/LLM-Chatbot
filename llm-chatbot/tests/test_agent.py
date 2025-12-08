from agent import __version__


def test_version():
    """Test that version is set correctly."""
    assert __version__ == "0.1.0"


def test_main_runs():
    """Test that the CLI entry point can be imported without error."""
    from agent.cli import run_cli

    # Just test that import works; don't actually run CLI
    # (running would block waiting for input)
    assert callable(run_cli)

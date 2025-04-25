"""Test Snap App."""

import curso_fastapi_template_backend


def test_import() -> None:
    """Test that the app can be imported."""
    assert isinstance(curso_fastapi_template_backend.__name__, str)

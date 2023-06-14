"""Testing functionality for the Loqio Charging Station device."""
from pathlib import Path


def _fixture_path(filename: str) -> Path:
    return Path(__file__).parent / "fixtures" / filename


def load_fixtures(filename: str) -> str:
    """Load a fixture."""
    return _fixture_path(filename).read_text(encoding="utf-8")

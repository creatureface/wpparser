from pathlib import Path

import pytest

FIXTURES_DIR = Path(__file__).parent / "fixtures"


@pytest.fixture
def sample_export():
    return str(FIXTURES_DIR / "blog.wordpress.2014-09-26.xml")

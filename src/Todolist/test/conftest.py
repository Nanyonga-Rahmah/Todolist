"""Configure test fixtures."""

import pytest
from _pytest.assertion import truncate
from faker import Faker

fake = Faker()

# Increase the long string truncation limit when running pytest in
# verbose mode; cf. https://stackoverflow.com/a/60321834.
truncate.DEFAULT_MAX_LINES = 999999
truncate.DEFAULT_MAX_CHARS = 999999


@pytest.fixture
def todo_data() -> dict:
    """Provide sample data for a Todo item."""
    return {
        "title": f"{fake.sentence(nb_words=3)}",
        "description": f"{fake.paragraph(nb_sentences=2)}",
        "completed": fake.boolean(),
    }

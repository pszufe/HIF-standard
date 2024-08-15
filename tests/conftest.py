import json

import pytest

schema_location = "schemas/hif_schema_v0.1.0.json"


@pytest.fixture
def schema():
    return json.load(open(schema_location, "r"))


@pytest.fixture
def empty_file():
    return json.load(open("tests/test_files/empty.json", "r"))

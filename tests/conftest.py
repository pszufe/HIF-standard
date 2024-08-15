import json

import pytest
import requests

schema_location = "https://raw.githubusercontent.com/pszufe/HIF_validators/main/schemas/hif_schema_v0.1.0.json"
json_dir = "tests/test_files"


@pytest.fixture
def schema():
    r = requests.get(schema_location)

    if r.ok:
        return r.json()


@pytest.fixture
def empty_file():
    return json.load(open(f"{json_dir}/empty.json", "r"))

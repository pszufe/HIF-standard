"""
in order to load each of the files needed for the tests
"""
#pylint:disable = missing-function-docstring,unspecified-encoding
import json

import pytest
import fastjsonschema

SCHEMA = "schemas/hif_schema_v0.1.0.json"
JSON_DIR = "tests/test_files"


@pytest.fixture
def validator():
    return fastjsonschema.compile(json.load(open(SCHEMA)))

@pytest.fixture
def empty():
    return json.load(open(f"{JSON_DIR}/empty.json", "r"))

@pytest.fixture
def single_node():
    return json.load(open(f"{JSON_DIR}/single_node.json", "r"))

@pytest.fixture
def single_edge():
    return json.load(open(f"{JSON_DIR}/single_edge.json", "r"))

@pytest.fixture
def single_incidence():
    return json.load(open(f"{JSON_DIR}/single_incidence.json", "r"))

@pytest.fixture
def directed_incidence():
    return json.load(open(f"{JSON_DIR}/directed_incidence.json", "r"))

@pytest.fixture
def bad_top_level_field():
    return json.load(open(f"{JSON_DIR}/bad_top_level_field.json", "r"))


@pytest.fixture
def bad_network_type():
    return json.load(open(f"{JSON_DIR}/bad_network_type.json", "r"))


@pytest.fixture
def bad_node_without_id():
    return json.load(open(f"{JSON_DIR}/bad_node_without_id.json", "r"))


@pytest.fixture
def metadata_as_list():
    return json.load(open(f"{JSON_DIR}/metadata_as_list.json", "r"))


@pytest.fixture
def empty_hypergraph():
    return json.load(open(f"{JSON_DIR}/empty_hypergraph.json", "r"))

import json

import fastjsonschema
import pytest
import requests

schema = "schemas/hif_schema_v0.1.0.json"
json_dir = "tests/test_files"


@pytest.fixture
def validator():
    return fastjsonschema.compile(json.load(open(schema)))


@pytest.fixture
def empty():
    return json.load(open(f"{json_dir}/empty.json", "r"))


@pytest.fixture
def single_node():
    return json.load(open(f"{json_dir}/single_node.json", "r"))


@pytest.fixture
def single_edge():
    return json.load(open(f"{json_dir}/single_edge.json", "r"))


@pytest.fixture
def single_incidence():
    return json.load(open(f"{json_dir}/single_incidence.json", "r"))


@pytest.fixture
def bad_top_level_field():
    return json.load(open(f"{json_dir}/bad_top_level_field.json", "r"))


@pytest.fixture
def bad_network_type():
    return json.load(open(f"{json_dir}/bad_network_type.json", "r"))


@pytest.fixture
def bad_node_without_id():
    return json.load(open(f"{json_dir}/bad_node_without_id.json", "r"))


@pytest.fixture
def metadata_as_list():
    return json.load(open(f"{json_dir}/metadata_as_list.json", "r"))


@pytest.fixture
def empty_hypergraph():
    return json.load(open(f"{json_dir}/empty_hypergraph.json", "r"))

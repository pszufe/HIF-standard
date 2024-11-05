import json

import fastjsonschema
import pytest

schema = "schemas/hif_schema_v0.1.0.json"
bad_json_dir = "tests/test_files/HIF-non-compliant"
good_json_dir = "tests/test_files/HIF-compliant"


# validator
@pytest.fixture
def validator():
    return fastjsonschema.compile(json.load(open(schema)))


### Examples which should break ###
# test empty fields
@pytest.fixture
def empty():
    return json.load(open(f"{bad_json_dir}/empty.json", "r"))


# test top-level
@pytest.fixture
def bad_top_level_field():
    return json.load(open(f"{bad_json_dir}/bad_top_level_field.json", "r"))


@pytest.fixture
def bad_network_type():
    return json.load(open(f"{bad_json_dir}/bad_network_type.json", "r"))


# test metadata
@pytest.fixture
def metadata_as_list():
    return json.load(open(f"{bad_json_dir}/metadata_as_list.json", "r"))


# test nodes
@pytest.fixture
def bad_node_without_id():
    return json.load(open(f"{bad_json_dir}/bad_node_without_id.json", "r"))


@pytest.fixture
def bad_node_field():
    return json.load(open(f"{bad_json_dir}/bad_node_field.json", "r"))


# test edges
@pytest.fixture
def bad_edge_without_id():
    return json.load(open(f"{bad_json_dir}/bad_edge_without_id.json", "r"))


@pytest.fixture
def bad_edge_field():
    return json.load(open(f"{bad_json_dir}/bad_edge_field.json", "r"))


# test incidences
@pytest.fixture
def bad_incidence_field():
    return json.load(open(f"{bad_json_dir}/bad_incidence_field.json", "r"))


@pytest.fixture
def single_incidence_with_weight_as_string():
    return json.load(
        open(f"{bad_json_dir}/single_incidence_with_weight_as_string.json", "r")
    )


### Examples which should work
# empty
@pytest.fixture
def empty_hypergraph():
    return json.load(open(f"{good_json_dir}/empty_hypergraph.json", "r"))


# test nodes
@pytest.fixture
def single_node():
    return json.load(open(f"{good_json_dir}/single_node.json", "r"))


@pytest.fixture
def single_node_with_attrs():
    return json.load(open(f"{good_json_dir}/single_node_with_attrs.json", "r"))

@pytest.fixture
def single_node_with_additional_properties():
    return json.load(open(f"{good_json_dir}/single_node_with_additional_properties.json", "r"))

# test edges
@pytest.fixture
def single_edge():
    return json.load(open(f"{good_json_dir}/single_edge.json", "r"))


@pytest.fixture
def single_edge_with_attrs():
    return json.load(open(f"{good_json_dir}/single_edge_with_attrs.json", "r"))

@pytest.fixture
def single_edge_with_additional_properties():
    return json.load(open(f"{good_json_dir}/single_edge_with_additional_properties.json", "r"))

# test incidences
@pytest.fixture
def single_incidence():
    return json.load(open(f"{good_json_dir}/single_incidence.json", "r"))


@pytest.fixture
def single_incidence_with_weights():
    return json.load(open(f"{good_json_dir}/single_incidence_with_weights.json", "r"))


@pytest.fixture
def single_incidence_with_attrs():
    return json.load(open(f"{good_json_dir}/single_incidence_with_attrs.json", "r"))

@pytest.fixture
def single_incidence_with_additional_properties():
    return json.load(open(f"{good_json_dir}/single_incidence_with_additional_properties.json", "r"))

@pytest.fixture
def good_metadata():
    return json.load(open(f"{good_json_dir}/good_metadata.json"))

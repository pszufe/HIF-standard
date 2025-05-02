import json

import fastjsonschema
import pytest

schema = "schemas/schema.json"
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

@pytest.fixture
def metadata_with_nested_attributes():
    return json.load(open(f"{good_json_dir}/metadata_with_nested_attributes.json", "r"))

@pytest.fixture
def metadata_with_deeply_nested_attributes():
    return json.load(open(f"{good_json_dir}/metadata_with_deeply_nested_attributes.json", "r"))


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

@pytest.fixture
def empty_arrays():
    return json.load(open(f"{good_json_dir}/empty_arrays.json", "r"))

# test nodes
@pytest.fixture
def single_node():
    return json.load(open(f"{good_json_dir}/single_node.json", "r"))


@pytest.fixture
def single_node_with_attrs():
    return json.load(open(f"{good_json_dir}/single_node_with_attrs.json", "r"))


# test edges
@pytest.fixture
def single_edge():
    return json.load(open(f"{good_json_dir}/single_edge.json", "r"))


@pytest.fixture
def single_edge_with_attrs():
    return json.load(open(f"{good_json_dir}/single_edge_with_attrs.json", "r"))


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
def single_incidence_with_direction_not_in_enum():
    return json.load(open(f"{bad_json_dir}/single_incidence_with_direction_not_in_enum.json", "r"))

@pytest.fixture
def missing_required_field_incidence():
    return json.load(open(f"{bad_json_dir}/missing_required_field_incidence.json", "r"))

@pytest.fixture
def bad_node_float():
    return json.load(open(f"{bad_json_dir}/bad_node_float.json", "r"))

### Tests for duplicated items

@pytest.fixture
def duplicated_nodes_edges():
    return json.load(open(f"{good_json_dir}/duplicated_nodes_edges.json", "r"))


### Tests for directionality

import pytest

@pytest.fixture
def valid_direction_head():
    """Fixture for a valid incidence with direction 'head'."""
    return json.load(open(f"{good_json_dir}/valid_incidence_head.json", "r"))

@pytest.fixture
def valid_direction_tail():
    """Fixture for a valid incidence with direction 'tail'."""
    return json.load(open(f"{good_json_dir}/valid_incidence_tail.json", "r"))

@pytest.fixture
def missing_direction():
    """Fixture for a valid incidence without the direction field."""

    # This should be a valid incidence unless the schema is updated to enforce the direction field
    return json.load(open(f"{good_json_dir}/missing_direction.json", "r"))

@pytest.fixture
def invalid_direction_value():
    """Fixture for an invalid direction value."""
    return json.load(open(f"{bad_json_dir}/invalid_direction_value.json", "r"))

@pytest.fixture
def missing_required_fields_with_direction():
    """Fixture for incidences with direction but missing required fields."""
    return json.load(open(f"{bad_json_dir}/missing_required_fields_with_direction.json", "r"))

@pytest.fixture
def extra_fields_with_direction():
    """Fixture for incidences with extra fields."""
    return json.load(open(f"{bad_json_dir}/extra_fields_with_direction.json", "r"))

### Tests which check HIF non-compliant files to make sure the schema catches them ###
import pytest


# test empty
def test_empty(validator, empty):
    with pytest.raises(ValueError):
        validator(empty)


# test top-level fields
def test_bad_top_level_field(validator, bad_top_level_field):
    with pytest.raises(ValueError):
        validator(bad_top_level_field)


def test_bad_network_type(validator, bad_network_type):
    with pytest.raises(ValueError):
        validator(bad_network_type)


# test metadata
def test_metadata_as_list(validator, metadata_as_list):
    with pytest.raises(ValueError):
        validator(metadata_as_list)


# test nodes
def test_bad_node_without_id(validator, bad_node_without_id):
    with pytest.raises(ValueError):
        validator(bad_node_without_id)


def test_bad_node_field(validator, bad_node_field):
    with pytest.raises(ValueError):
        validator(bad_node_field)


# test edge
def test_bad_edge_without_id(validator, bad_edge_without_id):
    with pytest.raises(ValueError):
        validator(bad_edge_without_id)


def test_bad_edge_field(validator, bad_edge_field):
    with pytest.raises(ValueError):
        validator(bad_edge_field)


# test incidences
def test_bad_incidence_field(validator, bad_incidence_field):
    with pytest.raises(ValueError):
        validator(bad_incidence_field)


def test_single_incidence_with_weight_as_string(
    validator, single_incidence_with_weight_as_string
):
    with pytest.raises(ValueError):
        validator(single_incidence_with_weight_as_string)

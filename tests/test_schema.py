import pytest

### Tests which check bad formats ###


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


# test incidences
def test_bad_incidence_field(validator, bad_incidence_field):
    with pytest.raises(ValueError):
        validator(bad_incidence_field)


def test_single_incidence_with_weight_as_string(
    validator, single_incidence_with_weight_as_string
):
    with pytest.raises(ValueError):
        validator(single_incidence_with_weight_as_string)


### Tests which check valid formats


# test empty
def test_empty_hypergraph(validator, empty_hypergraph):
    validator(empty_hypergraph)


# test metadata


# test nodes
def test_single_node(validator, single_node):
    validator(single_node)


def test_single_node_with_attrs(validator, single_node_with_attrs):
    validator(single_node_with_attrs)


# test edges
def test_single_edge(validator, single_edge):
    validator(single_edge)


def test_single_edge_with_attrs(validator, single_edge_with_attrs):
    validator(single_edge_with_attrs)


# test incidences
def test_single_incidence(validator, single_incidence):
    validator(single_incidence)


def test_single_incidence_with_weights(validator, single_incidence_with_weights):
    validator(single_incidence_with_weights)


def test_single_incidence_with_attrs(validator, single_incidence_with_attrs):
    validator(single_incidence_with_attrs)

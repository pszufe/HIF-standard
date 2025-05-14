### Tests which check HIF-compliant files formats to make sure the schema validates them ###


# test empty
def test_empty_hypergraph(validator, empty_hypergraph):
    validator(empty_hypergraph)


def test_empty_arrays(validator, empty_arrays):
    validator(empty_arrays)


# test metadata
def test_nested_attributes_validation(validator, metadata_with_nested_attributes):
    validator(metadata_with_nested_attributes)


def metadata_with_deeply_nested_attributes(validator, deeply_nested_metadata):
    validator(deeply_nested_metadata)


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


# test duplicated
def test_duplicated_nodes_edges(validator, duplicated_nodes_edges):
    """Test with repeated nodes, edges, and incidences."""
    validator(duplicated_nodes_edges)  # Expect to pass unless uniqueness is enforced


# test direction


def test_valid_direction_head(validator, valid_direction_head):
    """Test a valid incidence with direction 'head'."""
    validator(valid_direction_head)


def test_valid_direction_tail(validator, valid_direction_tail):
    """Test a valid incidence with direction 'tail'."""
    validator(valid_direction_tail)


def test_missing_direction(validator, missing_direction):
    """Test a valid incidence without the direction field."""
    validator(missing_direction)

### Tests which check HIF-compliant files formats to make sure the schema validates them ###


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

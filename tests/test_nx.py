import networkx as nx
from scripts.nx import from_hif


def test_empty_hypergraph(empty_hypergraph):
    result = from_hif(empty_hypergraph)
    expected = nx.Graph()
    assert nx.utils.graphs_equal(result, expected)

def test_single_node(single_node):
    result = from_hif(single_node)
    expected = nx.Graph()
    expected.add_node(42, bipartite=0, weight=0)
    assert nx.utils.graphs_equal(result, expected)

def test_single_edge(single_edge):
    result = from_hif(single_edge)
    expected = nx.Graph()
    expected.add_node(3, bipartite=1, weight=0)
    assert nx.utils.graphs_equal(result, expected)

def test_single_incidence(single_incidence):
    result = from_hif(single_incidence)
    expected = nx.Graph()
    expected.add_edge("abcd", 42, weight=0)
    assert nx.utils.graphs_equal(result, expected)

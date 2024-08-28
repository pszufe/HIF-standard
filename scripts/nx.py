"""
convert to a networkx Graph
"""
from typing import Union
import networkx as nx

def from_hif(data) -> Union[nx.Graph,nx.DiGraph]:
    """
    convert to a networkx Graph
    """
    is_directed = data.get("network-type","undirected") == "directed"
    if is_directed:
        g = nx.DiGraph()
    else:
        g = nx.Graph()
    for n in data.get("nodes", []):
        g.add_node(n["node"], bipartite=0, weight=n.get("weight", 0))
    for e in data.get("edges", []):
        g.add_node(e["edge"], bipartite=1, weight=e.get("weight", 0))
    for i in data["incidences"]:
        if is_directed:
            # TODO the default is ambiguous and requires discussion
            if i.get("direction","head") == "head":
                g.add_edge(i["edge"],i["node"], weight=i.get("weight", 0))
            else:
                g.add_edge(i["node"], i["edge"], weight=i.get("weight", 0))
        else:
            g.add_edge(i["node"], i["edge"], weight=i.get("weight", 0))
    return g

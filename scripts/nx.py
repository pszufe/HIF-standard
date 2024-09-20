import networkx as nx


def from_hif(data) -> nx.Graph:
    g = nx.Graph()
    for n in data.get("nodes", []):
        g.add_node(n["node"], bipartite=0, weight=n.get("weight", 0))
    for e in data.get("edges", []):
        g.add_node(e["edge"], bipartite=1, weight=e.get("weight", 0))
    for i in data["incidences"]:
        g.add_edge(i["node"], i["edge"], weight=i.get("weight", 0))
    return g

import json
import sys
from collections import defaultdict

# network parameters
filename = sys.argv[1]

with open(filename) as file:
    # load JSON file
    data = json.loads(file.read())

# check that keys do not deviate from the standard field names
fields = {"network-type", "metadata", "nodes", "edges", "incidences"}
if not set(data).issubset(fields):
    raise Exception(f"Acceptable field names are: {", ".join(fields)}\nand the field names are {", ".join(set(data))}")

# incidences are required
if "incidences" not in data:
    raise Exception(f"The file must contain an field for incidences.")

# check network type
network_types = {"asc", "undirected", "directed"}
if "network-type" in data:
    if data["network-type"] not in network_types:
        raise Exception(
            f"Unsupported network type. Valid types are: {", ".join(network_types)}"
        )

# check network metadata
if "metadata" in data:
    if not isinstance(data["metadata"], dict):
        raise Exception(f"The metadata must be dict-like.")

# check node attributes
if "nodes" in data:
    for i, record in enumerate(data["nodes"]):
        if len(record) != 2:
            raise Exception(
                f"Each node record must have two entries: an ID and the dictionary of corresponding attributes."
            )
        if not isinstance(record[1], dict):
            raise Exception(f"The node attributes must be dict-like.")

# check edge attributes
if "edges" in data:
    for i, record in enumerate(data["edges"]):
        if len(record) != 2:
            raise Exception(
                f"Each edge record must have two entries: an ID and the dictionary of corresponding attributes."
            )
        if not isinstance(record[1], dict):
            raise Exception(f"The edge attributes must be dict-like.")

for i, record in enumerate(data["edges"]):
    if len(record) != 3:
        raise Exception(
            f"Each incidence record must have three entries: an edge ID, a node ID, and the dictionary of corresponding attributes."
        )
    if not isinstance(record[2], dict):
        raise Exception(f"The incidence attributes must be dict-like.")

# in the case of directed hypergraphs, each incidence must
# have the "direction" attribute
if "network-type" in data and data["network-type"] == "directed":
    for i, record in enumerate(data["edges"]):
        if "direction" not in record[2]:
            raise Exception(
                f"Each incidence record must have have the 'direction' attribute for directed hypergraphs."
            )

# in the case of simplicial complexes, make sure that the edges are maximal
if "network-type" in data and data["network-type"] == "asc":
    edgedict = defaultdict(set)
    for record in data["incidences"]:
        e = record[0]
        n = record[1]
        edgedict[e].add(n)
    for e1, edge1 in edgedict.items():
        for e2, edge2 in edgedict.items():
            if e1 != e2 and edge1.issubset(edge2):
                raise Exception(
                    f"Only maximal faces should be stored for simplicial complexes."
                )

print("File conforms to HIF standard.")

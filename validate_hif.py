import json
import sys
from collections import defaultdict

# 0 - OK, 1 - bad JSON
status = 0

# network parameters
filename = sys.argv[1]

if len(sys.argv) > 2 and sys.argv[2] == "--silent":
    verbose = False
else:
    verbose = True


with open(filename) as file:
    # load JSON file
    data = json.loads(file.read())

# check that keys do not deviate from the standard field names
# DESCRIPTIONS OF THE FIELDS
# "network-type": a string indicating what type of network the dataset is.
#     Valid choices currently include:
#     - "undirected" (undirected hypergraph with potential multiedges)
#     - "asc" (simplicial complex where only the maximal faces are stored)
#     - "directed" (directed hypergraph with potential multiedges)
# "metadata": any dataset-level attributes (e.g., name, author, etc.) which must be dict-like
# "nodes": a list of 2-entries, where the first entry of a record is the node ID
#     and the second entry is dict-like and stores the associated attributes.
# "edges": a list of 2-entries, where the first entry of a record is the edge ID
#     and the second entry is dict-like and stores the associated attributes.
# "incidences": a list of 3-entries, where the first entry of a record is the edge ID,
#     the second entry is the node ID, and the third entry is dict-like and
#     stores the associated attributes.
#     **Note that this is the only required field.

fields = {"network-type", "metadata", "nodes", "edges", "incidences"}
if not set(data).issubset(fields):
    status = 1
    if verbose:
        field_names = ", ".join(fields)
        new_field_names = ", ".join(set(data))
        print(
            f"Acceptable field names are: {field_names}\nand the field names are {new_field_names}"
        )

# incidences are required
if "incidences" not in data:
    status = 1
    if verbose:
        print(f"The file must contain an field for incidences.")

# check network type
network_types = {"asc", "undirected", "directed"}
if "network-type" in data:
    if data["network-type"] not in network_types:
        status = 1

        if verbose:
            network_types = ", ".join(network_types)
            print(
                f"Unsupported network type. Valid types are: {network_types}"
            )

# check network metadata
if "metadata" in data:
    if not isinstance(data["metadata"], dict):
        status = 1
        if verbose:
            print(f"The metadata must be dict-like.")

# check node attributes
if "nodes" in data:
    for i, record in enumerate(data["nodes"]):
        if len(record) != 2:
            status = 1
            if verbose:
                print(
                    f"Each node record must have two entries: an ID and the dictionary of corresponding attributes."
                )
        if not isinstance(record[1], dict):
            status = 1
            if verbose:
                print(f"The node attributes must be dict-like.")

# check edge attributes
if "edges" in data:
    for i, record in enumerate(data["edges"]):
        if len(record) != 2:
            status = 1
            if verbose:
                print(
                    f"Each edge record must have two entries: an ID and the dictionary of corresponding attributes."
                )
        if not isinstance(record[1], dict):
            status = 1
            if verbose:
                print(f"The edge attributes must be dict-like.")

if "incidences" in data:
    for i, record in enumerate(data["incidences"]):
        if len(record) != 3:
            status = 1
            if verbose:
                print(
                    f"Each incidence record must have three entries: an edge ID, a node ID, and the dictionary of corresponding attributes."
                )
        if not isinstance(record[2], dict):
            status = 1
            if verbose:
                print(f"The incidence attributes must be dict-like.")

# in the case of directed hypergraphs, each incidence must
# have the "direction" attribute
if (
    "network-type" in data
    and data["network-type"] == "directed"
    and "incidences" in data
):
    for i, record in enumerate(data["incidences"]):
        if "direction" not in record[2]:
            status = 1
            if verbose:
                print(
                    f"Each incidence record must have have the 'direction' attribute for directed hypergraphs."
                )

# in the case of simplicial complexes, make sure that the edges are maximal
if "network-type" in data and data["network-type"] == "asc" and "incidences" in data:
    edgedict = defaultdict(set)
    for record in data["incidences"]:
        e = record[0]
        n = record[1]
        edgedict[e].add(n)
    for e1, edge1 in edgedict.items():
        for e2, edge2 in edgedict.items():
            if e1 != e2 and edge1.issubset(edge2):
                status = 1
                if verbose:
                    print(
                        f"Only maximal faces should be stored for simplicial complexes."
                    )

print(f"Exit status {status}.")

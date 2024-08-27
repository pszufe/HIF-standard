"""
this script provides a function `validate_hif`
which returns a dictionary specifying whether every part of the HIF specification is followed.
"""

import json
from collections import defaultdict
from typing import Dict
from warnings import warn

def validate_network_type(data, verbose : bool):
    if (
        "network-type" in data
        and data["network-type"] == "directed"
        and "incidences" in data
    ):
        for _i, record in enumerate(data["incidences"]):
            if "direction" not in record[2]:
                status = 1
                if verbose:
                    print(
                        "".join(["Each incidence record must have have",
                                 "the 'direction' attribute for directed hypergraphs."])
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
                    if verbose:
                        print(
                            "Only maximal faces should be stored for simplicial complexes."
                    )

#pylint:disable=too-many-branches,too-many-statements
def validate_hif(path) -> Dict[str,int]:
    """
    a dictionary specifying whether every part of the HIF specification is followed
    for the file with the given path
    """
    #pylint:disable=unspecified-encoding
    with open(path) as file:
        # load JSON file
        data = json.loads(file.read())

    # dictionary to store statuses
    info = {}

    # check that keys do not deviate from the standard field names
    info["valid-field-names"] = 0
    fields = {"network-type", "metadata", "nodes", "edges", "incidences"}
    if not set(data).issubset(fields):
        fields = ", ".join(fields)
        data = ", ".join(set(data))
        warn(
            f"Acceptable field names are: {fields}\nand the field names are {data}"
        )
        info["valid-field-names"] = 1

    # incidences are required; check that they exist
    info["incidences-exist"] = 0

    if "incidences" not in data:
        warn("The file must contain an field for incidences.")
        info["incidences-exist"] = 1

    # check network type
    info["valid-network-type"] = 0

    network_types = {"asc", "undirected", "directed"}
    if "network-type" in data:
        if data["network-type"] not in network_types:
            network_types = ", ".join(network_types)
            warn(
                f"Unsupported network type. Valid types are: {network_types}"
            )
            info["valid-network-type"] = 1

    # check network metadata
    info["metadata-dict"] = 0

    if "metadata" in data:
        if not isinstance(data["metadata"], dict):
            warn("The metadata must be dict-like.")
            info["metadata-dict"] = 1

    # check node attributes
    info["node-record-length"] = 0
    info["node-attr-dict"] = 0

    if "nodes" in data:
        for _i, record in enumerate(data["nodes"]):
            if len(record) != 2:
                warn(
                    " ".join(["Each node record must have two entries:",
                              "an ID and the dictionary of corresponding attributes."])
                )
                info["node-record-length"] = 1

            if not isinstance(record[1], dict):
                warn("The node attributes must be dict-like.")
                info["node-attr-dict"] = 1

    # check edge attributes
    info["edge-record-length"] = 0
    info["edge-attr-dict"] = 0

    if "edges" in data:
        for _i, record in enumerate(data["edges"]):
            if len(record) != 2:
                warn(
                    " ".join(["Each edge record must have two entries:",
                              "an ID and the dictionary of corresponding attributes."])
                )
                info["edge-record-length"] = 1

            if not isinstance(record[1], dict):
                warn("The edge attributes must be dict-like.")
                info["edge-attr-dict"] = 1

    if "incidences" in data:
        info["incidence-record-length"] = 0
        info["incidence-attr-dict"] = 0

        for _i, record in enumerate(data["incidences"]):
            if len(record) != 3:
                warn(
                    " ".join(["Each incidence record must have three entries:",
                              "an edge ID, a node ID,",
                              "and the dictionary of corresponding attributes."])
                )
                info["incidence-record-length"] = 1

            if not isinstance(record[2], dict):
                warn("The incidence attributes must be dict-like.")
                info["incidence-attr-dict"] = 1

    # in the case of directed hypergraphs, each incidence must
    # have the "direction" attribute
    if "network-type" in data and data["network-type"] == "directed":
        data["direction-exists-for-directed"] = 0
        for _i, record in enumerate(data["edges"]):
            if "direction" not in record[2]:
                warn(
                    " ".join(["Each incidence record must have have",
                             "the 'direction' attribute for directed hypergraphs."])
                )
                data["direction-exists-for-directed"] = 1

    # in the case of simplicial complexes, make sure that the edges are maximal
    if "network-type" in data and data["network-type"] == "asc":
        data["maximal-edges-for-asc"] = 0
        edgedict = defaultdict(set)
        for record in data["incidences"]:
            e = record[0]
            n = record[1]
            edgedict[e].add(n)
        for e1, edge1 in edgedict.items():
            for e2, edge2 in edgedict.items():
                if e1 != e2 and edge1.issubset(edge2):
                    warn(
                        "Only maximal faces should be stored for simplicial complexes."
                    )
                    data["maximal-edges-for-asc"] = 1

    return info

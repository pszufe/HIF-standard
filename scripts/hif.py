"""
this script provides a function `validate_hif`
which returns a dictionary specifying whether every part of the HIF specification is followed.
"""

from __future__ import annotations
import json
from collections import defaultdict
from os import PathLike
from typing import List, Literal, Optional, TypeAlias,TypedDict, Union
from warnings import warn

SpecificationPart : TypeAlias = str
StatusCode : TypeAlias = Union[Literal[0],Literal[1]]

class SpecificationMet(TypedDict):
    """
    every part of the HIF specification
    has a status code
    """
    valid_field_names: StatusCode
    incidences_exist: StatusCode
    validate_network_type: StatusCode
    metadata_dict: StatusCode
    node_record_length: StatusCode
    node_attr_dict: StatusCode
    edge_record_length: StatusCode
    edge_attr_dict: StatusCode
    incidence_record_length: StatusCode
    incidence_attr_dict : StatusCode

def all_good() -> SpecificationMet:
    """
    all the good status codes
    """
    return SpecificationMet({"valid_field_names":0,
                        "incidences_exist":0,
                        "validate_network_type":0,
                        "metadata_dict":0,
                        "node_record_length":0,
                        "node_attr_dict":0,
                        "edge_record_length":0,
                        "edge_attr_dict":0,
                        "incidence_record_length":0,
                        "incidence_attr_dict":0})

SPECIFICATION_MET_PARTS = len(all_good())

def which_bad(info: SpecificationMet) -> List[str]:
    """
    which part of the specification have bad status codes
    """
    return [k for k, v in info.items() if v != 0]

#pylint:disable=too-many-branches,too-many-statements,too-many-locals
def validate_hif(path : Union[str,PathLike],*,data: Optional[dict] = None) -> SpecificationMet:
    """
    a dictionary specifying whether every part of the HIF specification is followed
    for the file with the given path
    alternatively, can just provide the loaded data directly and the path will be ignored
    """

    #pylint:disable=unspecified-encoding
    if data is None:
        with open(path) as file:
            # load JSON file
            data = json.loads(file.read())

    # dictionary to store statuses
    info_class = all_good()

    # check that keys do not deviate from the standard field names
    info_class["valid_field_names"] = 0
    fields = {"network-type", "metadata", "nodes", "edges", "incidences"}
    if not set(data).issubset(fields):
        fields_warn = ", ".join(fields)
        data_warn = ", ".join(set(data))
        warn(
            f"Acceptable field names are: {fields_warn}\nand the field names are {data_warn}"
        )
        info_class["valid_field_names"] = 1

    # incidences are required; check that they exist
    info_class["incidences_exist"] = 0
    if "incidences" not in data:
        warn("The file must contain an field for incidences.")
        info_class["incidences_exist"] = 1

    # check network type
    info_class["validate_network_type"] = 0
    network_types = {"asc", "undirected", "directed"}
    if "network-type" in data:
        if data["network-type"] not in network_types:
            network_types_warn = ", ".join(network_types)
            warn(
                f"Unsupported network type. Valid types are: {network_types_warn}"
            )
            info_class["validate_network_type"] = 1

    # check network metadata
    info_class["metadata_dict"] = 0
    if "metadata" in data:
        if not isinstance(data["metadata"], dict):
            warn("The metadata must be dict-like.")
            info_class["metadata_dict"] = 1

    # check node attributes
    info_class["node_record_length"] = 0
    info_class["node_attr_dict"] = 0
    if "nodes" in data:
        for _i, record in enumerate(data["nodes"]):
            if len(record) != 2:
                warn(
                    " ".join(["Each node record must have two entries:",
                              "an ID and the dictionary of corresponding attributes."])
                )
                info_class["node_record_length"] = 1

            if len(record)>1 and not isinstance(record[1], dict):
                warn("The node attributes must be dict-like.")
                info_class["node_attr_dict"] = 1

    # check edge attributes
    info_class["edge_record_length"] = 0
    info_class["edge_attr_dict"] = 0
    if "edges" in data:
        for _i, record in enumerate(data["edges"]):
            if len(record) != 2:
                warn(
                    " ".join(["Each edge record must have two entries:",
                              "an ID and the dictionary of corresponding attributes."])
                )
                info_class["edge_record_length"] = 1

            if len(record) > 1 and not isinstance(record[1], dict):
                warn("The edge attributes must be dict-like.")
                info_class["edge_attr_dict"] = 1

    if "incidences" in data:
        info_class["incidence_record_length"] = 0
        info_class["incidence_attr_dict"] = 0

        for _i, record in enumerate(data["incidences"]):
            if len(record) != 3:
                warn(
                    " ".join(["Each incidence record must have three entries:",
                              "an edge ID, a node ID,",
                              "and the dictionary of corresponding attributes."])
                )
                info_class["incidence_record_length"] = 1

            if len(record)>2 and not isinstance(record[2], dict):
                warn("The incidence attributes must be dict-like.")
                info_class["incidence_attr_dict"] = 1

    # in the case of directed hypergraphs, each incidence must
    # have the "direction" attribute
    if "network-type" in data and data["network-type"] == "directed":
        data["direction-exists-for-directed"] = 0
        for _i, record in enumerate(data["edges"]):
            if len(record)<2 or "direction" not in record[2]:
                warn(
                    " ".join(["Each incidence record must have have",
                             "the 'direction' attribute for directed hypergraphs."])
                )
                data["direction-exists-for-directed"] = 1
    return info_class

def validate_network_type(data, verbose : bool):
    """
    Custom validations for network types
    """
    if (
        "network-type" in data
        and data["network-type"] == "directed"
        and "incidences" in data
    ):
        for _i, record in enumerate(data["incidences"]):
            if "direction" not in record[2]:
                _status = 1
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

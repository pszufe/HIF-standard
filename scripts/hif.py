from collections import defaultdict


def validate_network_type(data, verbose):
    """
    Custom validations for network types
    """
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
                    if verbose:
                        print(
                            f"Only maximal faces should be stored for simplicial complexes."
                    )

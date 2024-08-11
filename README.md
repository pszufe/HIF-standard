## A set of Hypergraph Exchange Format (HIF) specification & validators
(Work-in-progress)

Hypergraph Exchange Format (HIF) is a forthcoming standardard for data exchange of the existing hypergaph libraries. 

Initial assumptions about the core of the HIF data format:
```
"network-type": "hypergraph",
"metadata": {"name": "test"},
"incidences":[[2, 1, {"weight": "test", etc.}]],
"nodes":[[1, {"name": "test"}]],
"edges":[[2, {"timestamp": "2024-06-16"}]],
```
- All fields are optional except for "incidences". If there are no attributes associated with each incidence, it is an empty dictionary.
- The first two fields of each incidence record are edge, node IDs.
- If a hypergraph is, for instance, directed, the edge direction will be contained in the attribute dictionary.
- Isolated nodes and empty edges by entries in "nodes" and "edges" which are not present in the incidences.

### Table of contents for this folder

This repository is organized into three folders:
* `examples`: This folder contains examples of higher-order datasets in the HIF standard. For details of its contents, see the [README](/examples/EXAMPLES.md).
* `schemas`: This folder contains all schemas used for specifying the HIF standard. For details of its contents, see the [README](/schemas/SCHEMAS.md).
* `scripts`: This folder contains scripts for checking that datasets match the HIF standard. For details of its contents, see the [README](/scripts/SCRIPTS.md).

- *HIF_schemas.ipynb*:
- *validate_hif.py*: This Python command line executable checks whether a JSON file matches the HIF standard. All errors print to the command line. More details on running this are in the [next section](#validate-files-against-the-hif-standard).
	

### Validate files against the HIF standard
*validate_hif.py* is an executable that checks whether a file follows the HIF standard. It can be run as follows:
```python
python validate_hif.py <filename> [OPTIONS]
```
The only option is `--silent`, which suppresses all detailed warnings. Regardless, the script prints a 0 if the JSON file passes the HIF standard and 1 otherwise.

### Hypergraph tools and packages represented

The authors, co-authors or contributors of the following software libraries are represented:
- [HypergraphX](https://github.com/HGX-Team/hypergraphx) (Python)
- [HyperNetX](https://github.com/pnnl/HyperNetX) (Python)
- [XGI](https://github.com/xgi-org/xgi) (Python)
- [SimpleHypergraphs.jl](https://github.com/pszufe/SimpleHypergraphs.jl) (Julia)

### Contributors
This project is an ongoing colaborative work of the following people (alphabetical order):
- [Audun Myers](https://www.audunmyers.com/) (Pacific Northwest National Laboratory) 
- [Brenda Praggastis](https://www.pnnl.gov/people/brenda-praggastis)  (Pacific Northwest National Laboratory)
- [Caterina Debacco](https://www.cdebacco.com/) (Max Planck Institute for Intelligent Systems)
- [Cliff Joslyn](https://www.pnnl.gov/people/cliff-joslyn) (Pacific Northwest National Laboratory)
- [Francesco Lotito](https://scholar.google.it/citations?user=_r_zQAwAAAAJ&hl=en) (University of Trento)
- [Martín Coll](https://about.me/mcoll)  (University of Buenos Aires)
- [Nicholas Landry](https://nwlandry.com/) (University of Virginia) 
- [Przemyslaw Szufel](https://szufel.pl/) (SGH Warsaw School of Economics)


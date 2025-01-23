<p align="center">
  <img src="HIF_logo.svg" alt="Logo" width="400">
</p>

## The Hypergraph Interchange Format (HIF) standard
(Work-in-progress)

The Hypergraph Interchange Format (HIF) is a forthcoming standard for higher-order network data to facilitate seamless data exchange between existing higher-order network libraries. 

### Table of contents for this folder

This repository is organized into the following folders:
* `examples`: This folder contains examples of higher-order datasets in the HIF standard. For details of its contents, see the [README](/examples/EXAMPLES.md).
* `requirements`: This folder contains a list of all dependencies used in this project.
* `schemas`: This folder contains all schemas used for specifying the HIF standard. For details of what has changed with each version, see the [CHANGELOG](/schemas/CHANGLEOG.md).
* `src`: This folder contains addition functionality for checking against the HIF specification.
* `tests`: This folder contains all of the unit tests used for validating that the schema is correct.
* `tutorials`: This folder contains tutorials detailing how each library uses the HIF standard and how the HIF standard allows seamless integration between libraries. For details of its contents, see the [README](/tutorials/TUTORIALS.md).

Initial assumptions about the core of the HIF standard:
```
{
"network-type": "undirected", # will indicate if directed or an asc
"metadata": {"name": "test"}, # library specific metadata to store with object
"incidences":[{"edge":edge_id, "node":node_id,...},...], # incidences are lists of records of edge node pairs along with the edge dependent node properties
"nodes":[{"node":node_id,...},...] # nodes and edges are lists of records
"edges":[{"edge":edge_id,...},...],
}
```
- All fields are optional except for "incidences". 
- Keywords are indicated in the schema, these include:
    - incidences
    - nodes
    - edges
    - weight
    - network-type
    - **network types** : undirected, directed, asc
    - direction
    - **direction keywords** : head, tail
- If a hypergraph is, for instance, directed, the edge direction will be contained in the incidences record with keyword "direction".
- Isolated nodes and empty edges are entries in "nodes" and "edges" which are not present in the incidences.
- This schema explicitely describes all items in the schema using json objects and typing. This is a verbose presentation making it faster to instantiate than list-based schemas requiring a parser.

- *validate_hif.py*: This Python command line executable checks whether a JSON file matches the HIF standard. All errors print to the command line. More details on running this are in the [next section](#validate-files-against-the-hif-standard).
	

### Validate files against the HIF standard
*validate_hif.py* is an executable that checks whether a file follows the HIF standard. It can be run as follows:
```python
python validate_hif.py <filename> [OPTIONS]
```
The only option is `--silent`, which suppresses all detailed warnings. Regardless, the script prints a 0 if the JSON file passes the HIF standard and 1 otherwise.

### Validate files using HIF standard with fastjsonschema in python module
```python
import fastjsonschema
import json
import requests

schema = requests.get("https://raw.githubusercontent.com/pszufe/HIF-standard/main/schemas/hif_schema_v0.1.0.json").json()
validator = fastjsonschema.compile(schema)
hiftext = json.load(open(filename,'r'))
validator(hiftext)
```

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
- [Cliff Joslyn](https://www.pnnl.gov/people/cliff-joslyn) (Pacific Northwest National Laboratory)
- [Francesco Lotito](https://scholar.google.it/citations?user=_r_zQAwAAAAJ&hl=en) (University of Trento)
- [Martín Coll](https://about.me/mcoll)  (University of Buenos Aires)
- [Nicholas Landry](https://nwlandry.com/) (University of Virginia) 
- [Przemyslaw Szufel](https://szufel.pl/) (SGH Warsaw School of Economics)

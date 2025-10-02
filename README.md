<p align="center">
  <img src="logo/logo.svg" alt="Logo" width="300">
</p>

[![DOI](https://zenodo.org/badge/829894825.svg)](https://doi.org/10.5281/zenodo.15802759)

# The Hypergraph Interchange Format (HIF) standard

The Hypergraph Interchange Format (HIF) is a standard for higher-order network data to facilitate seamless data exchange between higher-order network libraries. 

## Repository structure

This repository is organized into the following folders:

* `figures`: This folder contains all the figures used in the preprint corresponding to this project.
* `logo`: This folder contains the HIF logo in several different formats.
* `requirements`: This folder contains a list of all dependencies used in this project.
* `schemas`: This folder contains all schemas used for specifying the HIF standard. For details of what has changed with each version, see the [CHANGELOG](/schemas/CHANGELOG.md).
* `tests`: This folder contains all of the unit tests used for validating the schema against known compliant and non-compliant datasets.
* `tutorials`: This folder contains tutorials detailing how each library uses the HIF standard and how the HIF standard allows seamless integration between libraries. For details of its contents, see the [README](/tutorials/TUTORIALS.md).

## HIF Standard

### Structure
The HIF standard specifies the following JSON file structure:

* `"network-type"` (optional): `"asc"`, `"directed"`, or `"undirected"`
* `"metadata"` (optional): A dictionary-like set of network-level attributes
* `"incidences"` (required): A list of records, where each record is an incidence. Each incidence is a dictionary-like oject which may contain the following fields:
  * `"node"` (required): the node ID
  * `"edge"` (required): the edge ID
  * `"weight"` (optional): the incidence weight as an integer or floating point number
  * `"direction"` (optional): `"head"` or `"tail"` if the hyperedge is a directed hyperedge
  * `"attrs"` (optional): a dictionary-like object of all the miscellaneous incidence properties
* `"nodes"` (optional): A list of records, where each record is an node entry. Each entry is a dictionary-like object which may contain the following fields:
  * `"node"` (required): the node ID
  * `"attrs"` (optional): a dictionary-like object of all the miscellaneous nodal properties
* `"edges"` (optional): A list of records, where each record is an edge entry. Each entry is a dictionary-like object which may contain the following fields:
  * `"edge"` (required): the edge ID
  * `"attrs"` (optional): a dictionary-like object of all the miscellaneous edge properties

### Notes
* All fields are optional except for "incidences". 
* If a hypergraph is directed, the edge direction will be contained in the incidences record with keyword "direction".
* Isolated nodes and empty edges can be specified with entries in "nodes" and "edges" which are not present in the incidences.
* This schema explicitly describes all items in the schema using JSON objects and typing. This is a verbose presentation making it faster to instantiate than list-based schemas requiring a parser.

## Validate files against HIF standard

### Python
```python
import fastjsonschema
import json
import requests

url = "https://raw.githubusercontent.com/pszufe/HIF-standard/main/schemas/hif_schema.json"
schema = requests.get(url).json()
validator = fastjsonschema.compile(schema)
hiftext = json.load(open(filename,'r'))
try:
  validator(hiftext)
  print("HIF-Compliant JSON.")
except Exception as e:
   print(f"Invalid JSON: {e}")
```

### R
```R
library(jsonvalidate)
library(jsonlite)

url = "https://raw.githubusercontent.com/pszufe/HIF-standard/main/schemas/hif_schema.json"

schema <- paste(readLines(url, warn = FALSE))
validator <- json_validator(schema)
if (validator(filepath)) {
    print("HIF-Compliant JSON.")
} else {
    print("Invalid JSON.")
}
```

### Julia
```julia
using HTTP
using JSON3
using JSONSchema

url = "https://raw.githubusercontent.com/pszufe/HIF-standard/main/schemas/hif_schema.json"

schema = String(HTTP.get(url).body)
validator = Schema(schema)
hiftext = JSON3.read(filepath)
result = JSONSchema.validate(validator, hiftext)
println(
    result === nothing ?
    "HIF-Compliant JSON." :
    "Invalid JSON: " * "$result"
)
```

## Hypergraph tools and packages represented

The authors, co-authors, or contributors of the following software libraries are represented:
* [HypergraphX](https://github.com/HGX-Team/hypergraphx) (Python)
* [HyperNetX](https://github.com/pnnl/HyperNetX) (Python)
* [HAT](https://github.com/Jpickard1/Hypergraph-Analysis-Toolbox) (Python) 
* [SimpleHypergraphs.jl](https://github.com/pszufe/SimpleHypergraphs.jl) (Julia)
* [XGI](https://github.com/xgi-org/xgi) (Python)

## Contributors
This project is an ongoing colaborative work of the following people (alphabetical order):
* [Martín Coll](https://github.com/colltoaction)  (University of Buenos Aires)
* [Cliff Joslyn](https://www.pnnl.gov/people/cliff-joslyn) (Pacific Northwest National Laboratory)
* [Nicholas Landry](https://nwlandry.com/) (University of Virginia)
* [Francesco Lotito](https://scholar.google.it/citations?user=_r_zQAwAAAAJ&hl=en) (University of Trento)
* [Audun Myers](https://www.audunmyers.com/) (Pacific Northwest National Laboratory) 
* [Joshua Pickard](https://github.com/Jpickard1) (University of Michigan) 
* [Brenda Praggastis](https://www.pnnl.gov/people/brenda-praggastis)  (Pacific Northwest National Laboratory)
* [Przemysław Szufel](https://szufel.pl/) (SGH Warsaw School of Economics)

## How to Cite
You can cite the Hypergraph Interchange Format paper [arXiv:2507.11520](https://arxiv.org/abs/2507.11520) by copying the following BibTeX entry:
```bibtex
@misc{coll2025hifhypergraphinterchangeformat,
      title={HIF: The hypergraph interchange format for higher-order networks}, 
      author={Martín Coll and Cliff A. Joslyn and Nicholas W. Landry and Quintino Francesco Lotito and Audun Myers and Joshua Pickard and Brenda Praggastis and Przemysław Szufel},
      year={2025},
      eprint={2507.11520},
      archivePrefix={arXiv},
      primaryClass={physics.soc-ph},
      url={https://arxiv.org/abs/2507.11520}, 
}
```

## Projects using HIF
* [A Blue Start: A large-scale pairwise and higher-order social network dataset](https://arxiv.org/abs/2505.11608)
* [Efficient Gillespie algorithms for spreading phenomena in large and heterogeneous higher-order networks](https://arxiv.org/abs/2509.20174)

<p align="center">
  <img src="HIF_logo.svg" alt="Logo" width="300">
</p>

# The Hypergraph Interchange Format (HIF) standard
(Work-in-progress)

The Hypergraph Interchange Format (HIF) is a standard for higher-order network data to facilitate seamless data exchange between higher-order network libraries. 

## Repository structure

This repository is organized into the following folders:

* `requirements`: This folder contains a list of all dependencies used in this project.
* `schemas`: This folder contains all schemas used for specifying the HIF standard. For details of what has changed with each version, see the [CHANGELOG](/schemas/CHANGLEOG.md).
* `src`: This folder contains addition functionality for checking against the HIF specification.
* `tests`: This folder contains all of the unit tests used for validating the schema against known compliant and non-compliant datasets.
* `tutorials`: This folder contains tutorials detailing how each library uses the HIF standard and how the HIF standard allows seamless integration between libraries. For details of its contents, see the [README](/tutorials/TUTORIALS.md).

## HIF Standard

### Structure
The HIF standard specifies the following JSON file structure:

* `network-type` (optional): "asc, "directed", or "undirected""
* `metadata` (optional): A dictionary-like set of network-level attributes
* `incidences` (required): A list of records, where each record is an incidence. Each incidence is a dictionary-like oject which may contain the following fields:
  * `node` (required): the node ID
  * `edge` (required): the edge ID
  * `weight` (optional): the incidence weight
  * `direction` (optional): if the hyperedge is a directed hyperedge
  * `attrs` (optional): a dictionary-like object of all the miscellaneous incidence properties
* `nodes` (optional): A list of records, where each record is an node entry. Each entry is a dictionary-like object which may contain the following fields:
  * `node` (required): the node ID
  * `attrs` (optional): a dictionary-like object of all the miscellaneous nodal properties
* `edges` (optional): A list of records, where each record is an edge entry. Each entry is a dictionary-like object which may contain the following fields:
  * `edge` (required): the edge ID
  * `attrs` (optional): a dictionary-like object of all the miscellaneous edge properties

### Notes
* All fields are optional except for "incidences". 
* If a hypergraph is directed, the edge direction will be contained in the incidences record with keyword "direction".
* Isolated nodes and empty edges can be specified with entries in "nodes" and "edges" which are not present in the incidences.
* This schema explicitly describes all items in the schema using json objects and typing. This is a verbose presentation making it faster to instantiate than list-based schemas requiring a parser.

## Validate files against HIF standard

### Python
```python
import fastjsonschema
import json
import requests

url = "https://raw.githubusercontent.com/pszufe/HIF-standard/main/schemas/hif_schema_v0.1.0.json"
schema = requests.get(url).json()
validator = fastjsonschema.compile(schema)
hiftext = json.load(open(filename,'r'))
validator(hiftext)
```

### R
```R
library(jsonvalidate)
library(jsonlite)

url <- "https://raw.githubusercontent.com/pszufe/HIF-standard/main/schemas/hif_schema_v0.1.0.json"
schema <- paste(
    readLines(url, warn = FALSE),
    collapse = "\n"
)
validator <- json_validator(
    schema,
    engine="ajv"
)
validator(filename, verbose = TRUE)
```

### Julia
```julia
using HTTP
using JSON3
using JSONSchema

url = "https://raw.githubusercontent.com/pszufe/HIF-standard/main/schemas/hif_schema_v0.1.0.json"

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
* [SimpleHypergraphs.jl](https://github.com/pszufe/SimpleHypergraphs.jl) (Julia)
* [XGI](https://github.com/xgi-org/xgi) (Python)

## Contributors
This project is an ongoing colaborative work of the following people (alphabetical order):
* [Martín Coll](https://about.me/mcoll)  (University of Buenos Aires)
* [Cliff Joslyn](https://www.pnnl.gov/people/cliff-joslyn) (Pacific Northwest National Laboratory)
* [Nicholas Landry](https://nwlandry.com/) (University of Virginia)
* [Francesco Lotito](https://scholar.google.it/citations?user=_r_zQAwAAAAJ&hl=en) (University of Trento)
* [Audun Myers](https://www.audunmyers.com/) (Pacific Northwest National Laboratory) 
* [Brenda Praggastis](https://www.pnnl.gov/people/brenda-praggastis)  (Pacific Northwest National Laboratory)
* [Przemyslaw Szufel](https://szufel.pl/) (SGH Warsaw School of Economics)

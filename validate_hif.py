import json
import sys

import fastjsonschema

from scripts.hif import validate_network_type


if len(sys.argv) > 2 and sys.argv[2] == "--silent":
    verbose = False
else:
    verbose = True

# network parameters
filename = sys.argv[1]
schema_filename = "schemas/hif_schema_v0.1.0.json"

with open(filename) as file, open(schema_filename) as schema_file:
    # load JSON file
    validate_schema = fastjsonschema.compile(json.load(schema_file))
    data = json.load(file)
    validate_schema(data)
    validate_network_type(data, verbose)

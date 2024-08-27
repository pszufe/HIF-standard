"""
an executable that checks whether a file follows the HIF standard
"""

#pylint:disable=unspecified-encoding
import json
import sys

import fastjsonschema

from scripts.hif import validate_network_type


if len(sys.argv) > 2 and sys.argv[2] == "--silent":
    VERBOSE = False
else:
    VERBOSE = True

# network parameters
filename = sys.argv[1]
SCHEMA_FILENAME = "schemas/hif_schema_v0.1.0.json"

with open(filename,'r') as file, open(SCHEMA_FILENAME,'r') as schema_file:
    # load JSON file
    validate_schema = fastjsonschema.compile(json.load(schema_file))
    data = json.load(file)
    validate_schema(data)
    validate_network_type(data, VERBOSE)

# Description of schemas

- *hif_schema.json* - Initial JSONSchema
- *hif_schema1.json*
- *hif_schema2.json*

The schemas represent two possible approaches

1. hif_schema and hif_schema1 both accept arrays for incidences, nodes, and edges. The differ in that hif_schema1 does not require properties in the individual arrays.
2. hif_schema2 explicitely describes all items in the schema using json objects and typing. This presentation requires more storage but is faster to instantiate and interpret since parsing is no longer necessary.
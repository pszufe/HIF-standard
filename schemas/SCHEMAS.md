# Description of schemas

- *hif_schema.json* - Initial JSONSchema
- *hif_schema1.json*
- *hif_schema2.json*

The schemas represent two possible approaches

1. hif_schema and hif_schema1 both accept arrays for incidences, nodes, and edges. The differ in that hif_schema1 does not require properties in the individual arrays.
2. hif_schema2 explicitely describes all items in the schema using json objects and typing. This presentation requires more storage but is faster to instantiate and interpret since parsing is no longer necessary.

## Times

| schema           | data                          | hnx.to_hif       | hnx.from_hif     | 
|------------------|-------------------------------|------------------|------------------|
| hif_schema1.json | xgi contacts-high-school.json | 50.4 s ± 1.23    | 26.2 ms ± 516 µs |
| hif_schema2.json | xgi contacts-high-school.json | 16.5 ms ± 229 μs | 22.9 ms ± 554 µs |
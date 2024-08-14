# Description of schemas

## hif_schema_v0.1.0.json  
Initial proposal for schema for HIF json format.  
This schema explicitely describes all items in the schema using json objects and typing. This is a verbose presentation making it faster to instantiate than list based
schemas requiring a parser.

## Times - performance_testing.py
Performance estimates for generating hif format from various libraries using hif_schema_v0.1.0.json:

| library.method    | HGX-data/contacts-high-school.json |                    
|-------------------|------------------------------------|
| hnx.to_hif        |  0.01768 ns                        |  
| hnx.from_hif      |  0.02658 ns                        |  

## HIF_schemas.ipynb
Illustration of usage with fastschemajson library

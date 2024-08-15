import fastjsonschema
import pytest


def test_empty(schema, empty):
    validator = fastjsonschema.compile(schema)
    with pytest.raises(ValueError):
        validator(empty)


def test_bad_top_level_field(schema, bad_top_level_field):
    validator = fastjsonschema.compile(schema)
    with pytest.raises(ValueError):
        validator(bad_top_level_field)


def test_metadata_as_list(schema, metadata_as_list):
    validator = fastjsonschema.compile(schema)
    with pytest.raises(ValueError):
        validator(metadata_as_list)


def test_empty_hypergraph(schema, empty_hypergraph):
    validator = fastjsonschema.compile(schema)
    validator(empty_hypergraph)

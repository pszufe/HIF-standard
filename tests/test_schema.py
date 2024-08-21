import pytest


def test_empty(validator, empty):
    with pytest.raises(ValueError):
        validator(empty)


def test_bad_top_level_field(validator, bad_top_level_field):
    with pytest.raises(ValueError):
        validator(bad_top_level_field)


def test_metadata_as_list(validator, metadata_as_list):
    with pytest.raises(ValueError):
        validator(metadata_as_list)


def test_empty_hypergraph(validator, empty_hypergraph):
    validator(empty_hypergraph)

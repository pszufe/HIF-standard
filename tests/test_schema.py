import fastjsonschema
import pytest


def test_empty_file(schema, empty_file):
    validator = fastjsonschema.compile(schema)
    with pytest.raises(ValueError):
        validator(empty_file)

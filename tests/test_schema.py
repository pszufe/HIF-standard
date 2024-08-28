"""
each of the fixtures against the validator
all of which are defined in ``conftest.py``
"""

#pylint:disable = missing-function-docstring
import warnings
from fastjsonschema import JsonSchemaValueException
import pytest

from scripts.hif import SPECIFICATION_MET_PARTS, validate_hif, validate_network_type, which_bad

def test_empty(validator, empty):
    with pytest.raises(JsonSchemaValueException):
        validator(empty)
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        full_info = validate_hif("",data=empty)
    assert len(full_info) == SPECIFICATION_MET_PARTS
    assert which_bad(full_info) == ["incidences_exist"]

def test_bad_top_level_field(validator, bad_top_level_field):
    with pytest.raises(JsonSchemaValueException):
        validator(bad_top_level_field)
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        full_info = validate_hif("",data=bad_top_level_field)
    assert len(full_info) == SPECIFICATION_MET_PARTS
    assert which_bad(full_info) == ["valid_field_names"]

def test_bad_network_type(validator, bad_network_type):
    with pytest.raises(JsonSchemaValueException):
        validator(bad_network_type)
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        full_info = validate_hif("",data=bad_network_type)
    assert len(full_info) == SPECIFICATION_MET_PARTS
    assert which_bad(full_info) == ["validate_network_type"]

def test_bad_node_without_id(validator, bad_node_without_id):
    with pytest.raises(JsonSchemaValueException):
        validator(bad_node_without_id)
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        full_info = validate_hif("",data=bad_node_without_id)
    assert len(full_info) == SPECIFICATION_MET_PARTS
    assert which_bad(full_info) == ["node_record_length"]

def test_single_node(validator, single_node):
    validator(single_node)
    validate_network_type(single_node,False)
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        full_info = validate_hif("",data=single_node)
    assert len(full_info) == SPECIFICATION_MET_PARTS
    assert which_bad(full_info) == ["node_record_length"]

def test_single_edge(validator, single_edge):
    validator(single_edge)
    validate_network_type(single_edge,False)
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        full_info = validate_hif("",data=single_edge)
    assert len(full_info) == SPECIFICATION_MET_PARTS
    assert which_bad(full_info) == ["edge_record_length"]

def test_single_incidence(validator, single_incidence):
    validator(single_incidence)
    validate_network_type(single_incidence,False)
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        full_info = validate_hif("",data=single_incidence)
    assert len(full_info) == SPECIFICATION_MET_PARTS
    assert which_bad(full_info) == ["incidence_record_length"]

def test_metadata_as_list(validator, metadata_as_list):
    with pytest.raises(JsonSchemaValueException):
        validator(metadata_as_list)
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        full_info = validate_hif("",data=metadata_as_list)
    assert len(full_info) == SPECIFICATION_MET_PARTS
    assert which_bad(full_info) == ["metadata_dict"]

def test_empty_hypergraph(validator, empty_hypergraph):
    validator(empty_hypergraph)
    validate_network_type(empty_hypergraph,False)
    full_info = validate_hif("",data=empty_hypergraph)
    assert len(full_info) == SPECIFICATION_MET_PARTS
    assert len(which_bad(full_info)) == 0

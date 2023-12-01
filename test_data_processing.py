import pytest
from data_processing_function import process_data

def test_data_processing(file_obj):
    result = process_data(file_obj)
    assert result == "HELLO, WORLD!"


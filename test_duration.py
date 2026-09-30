import pytest
from duration_explore import decompose

def test_decompose_valid_small():
    assert decompose(380) == {'hours': 6, 'minutes': 20}

def test_decompose_valid_big():
    assert decompose(34533) == {'days': 23, 'hours': 23, "minutes": 33}

def test_decompose_valid_boundary():
    assert decompose(1440) == {'days': 1, 'hours': 0, 'minutes': 0}

def test_decompose_invalid_type():
    with pytest.raises(TypeError):
        decompose("380")

def test_decompose_invalid_value_negative():
    with pytest.raises(ValueError):
        decompose(-345)

def test_decompose_invalid_value_zero():
    with pytest.raises(ValueError):
        decompose(0)   
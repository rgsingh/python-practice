import pytest
from src.general import prob5


def test_position_out_of_bounds_raises_exception():
    with pytest.raises(Exception, match='zero-based position must be within bounds of input_arr') as e_info:
        prob5.valid_string_in_which(6, ['a', 'abb', 'sfs', 'oo', 'de', 'sfde'])

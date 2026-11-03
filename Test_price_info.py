import price_info
import pytest

def test_total_cost_shopping():
    result = price_info.total_cost_shopping()
    assert (result == pytest.approx(46.75)) 

def test_cost_of_fruits():
    result = price_info.cost_of_fruits('apple', 10)
    assert (result == pytest.approx(12.0))
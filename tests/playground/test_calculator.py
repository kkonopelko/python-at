import pytest
from playground.calculator import Calculator


class TestCalculator:
    
    @pytest.mark.parametrize(" x, y, result", [(1, 2, 0.5), (5, -1, -5)])
    def test_divide(self, x, y, result):
        assert Calculator().divide(x, y) == result
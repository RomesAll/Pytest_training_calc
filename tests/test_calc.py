from src.main import Calculator
import pytest

class TestCalc:

    @pytest.mark.parametrize("x, y, res", [(1, 91, 92),(2, 21, 23),(492, 222, 714),(53, 0, 53), (32.1, 2.1245, 34.224)])
    def test_addition(self, x, y, res):
        assert Calculator.addition(x, y) == res

    @pytest.mark.parametrize("x, y, res", [(32, "9", 41), (92.1235, 1.22, 93.34)])
    def test_addition_errors(self, x, y, res):
        with pytest.raises((TypeError, AssertionError)):
            assert Calculator.addition(x, y) == res

    @pytest.mark.parametrize("x, y, res", [(1,91,-90),(2,21,-19),(492,222,270),(53,0,53)])
    def test_subtraction(self, x, y, res):
        assert Calculator.subtraction(x, y) == res

    @pytest.mark.parametrize("x, y, res", [(1,91,'-90'),(2,"21",-19)])
    def test_subtraction_errors(self, x, y, res):
        with pytest.raises((TypeError, AssertionError)):
            assert Calculator.subtraction(x, y) == res
    
    @pytest.mark.parametrize("x, y, res", [(3,4,12),(9,9,81),(325,124,40300),(53,0,0)])
    def test_multiplication(self, x, y, res):
        assert Calculator.multiplication(x, y) == res

    @pytest.mark.parametrize("x, y, res", [(3, "4", 12), (1.3242, 1.111, 2.435)])
    def test_multiplication_errors(self, x, y, res):
        with pytest.raises((TypeError, AssertionError)):
            assert Calculator.subtraction(x, y) == res
    
    @pytest.mark.parametrize("x, y, res", [(81,9,9),(2,21,0.095),(492,222,2.216),(53,1,53)])
    def test_division(self, x, y, res):
        assert Calculator.division(x, y) == res

    @pytest.mark.parametrize("x, y, res", [("81",9,9),(1, 0, 0)])
    def test_division(self, x, y, res):
        with pytest.raises((TypeError, AssertionError, ZeroDivisionError)):
            assert Calculator.division(x, y) == res
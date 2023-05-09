import pytest

from app.calc import Calculator

class TestCalc:
    def setup(self):
        self.calc = Calculator
    def test_multiply(self):
        assert self.calc.multiply(self, 2, 2) == 4
    def test_division(self):
        assert self.calc.division(self, 8, 2) == 4
    def test_adding(self):
        assert self.calc.adding(self, 3, 3) == 6
    def test_subtraction(self):
        assert self.calc.subtraction(self, 3, 2) == 1

    def teardown(self):
        print(' ')

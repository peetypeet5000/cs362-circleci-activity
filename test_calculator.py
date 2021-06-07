import calculator


class TestCalc:
    def test_addition(self):
        assert calculator.add(1, 1) == 2
        assert calculator.add(-1, 1) == 0
        assert calculator.add(2.5, 1.25) == 3.75

    def test_subtraction(self):
        assert calculator.sub(1, 1) == 0
        assert calculator.sub(5, -5) == 10
        assert calculator.sub(10.5, 5.5) == 5

    def test_multiplication(self):
        assert calculator.mult(1, 10) == 10
        assert calculator.mult(-5, 5) == -25
        assert calculator.mult(.5, .5) == .25

    def test_devision(self):
        assert calculator.div(10, 1) == 10
        assert calculator.div(15, 5) == 3
        assert calculator.div(-10, 2) == -5

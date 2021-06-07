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

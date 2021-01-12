import unittest
from Functions_for_Unittests_two import fibonacci_memo, GridTraveler_new


class FunctionsTwoTests(unittest.TestCase):
    def test_fibonacci(self):
        self.assertEqual(fibonacci_memo(100), 354224848179261915075)

    def test_gridtraveler(self):
        self.assertEqual(GridTraveler_new(15, 15), 40116600)


if __name__ == "__main__":
    unittest.main()
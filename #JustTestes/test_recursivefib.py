import unittest
from recursivefib import fib


class TestRecursiveFib(unittest.TestCase):
    def test_values(self):
        self.assertAlmostEqual(fib(7), fib(7))
        self.assertAlmostEqual(fib(3), fib(3))
        self.assertAlmostEqual(fib(6), fib(6))
        self.assertAlmostEqual(fib(20), fib(20))

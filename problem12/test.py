import unittest
import triangle


class TestTriangle(unittest.TestCase):
    def test_calc_triangle(self):
        """ Triangle numbers are sum of successive numbers
        1: 1
        2: (1+2): 3
        3: (1+2+3): 6
        4: (1+2+3+4): 10
        ...
        """
        self.assertEquals(3, triangle.triangle_number(2))
        self.assertEquals(6, triangle.triangle_number(3))
        self.assertEquals(28, triangle.triangle_number(7))
        self.assertEquals(55, triangle.triangle_number(10))

    def test_factors(self):
        self.assertEquals([1, 2], triangle.factors(6))
        self.assertEquals([1, 3], triangle.factors(15))
        self.assertEquals([1, 2, 4], triangle.factors(28))

    def test_find(self):
        """ Find_first finds the first triangle number with n divisors"""
        self.assertEquals(6, triangle.find_first(3))
        self.assertEquals(6, triangle.find_first(4))
        self.assertEquals(28, triangle.find_first(5))

    def test_solution(self):
        self.assertEquals(76576500, triangle.find_first(500))

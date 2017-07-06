import unittest
import grid


class TestAdjacency(unittest.TestCase):
    def test_basic_adjacency(self):
        """ From the grid,
        08 02 22 97 38 15 00 40
        49 49 99 40 17 81 18 57
        81 49 31 73 55 79 14 29
        52 70 95 23 04 60 11 42
        22 31 16 71 51 67 63 89
        24 47 32 60 99 03 45 02
        32 98 81 28 64 23 67 10
        67 26 20 68 02 62 12 20,

        Asking for adjacency for 0,0 should result in
        [[08, 02, 22, 97], [08, 49, 31, 23], [08, 49, 81, 52]
        """
        actual = grid.get_4_adjacent_to(0, 0)
        expected = [[8, 2, 22, 97], [8, 49, 31, 23], [8, 49, 81, 52]]
        self.assertItemsEqual(actual, expected)

        actual = grid.get_4_adjacent_to(1, 1)
        expected = [[49, 99, 40, 17], [49, 49, 70, 31], [49, 31, 23, 51]]
        self.assertItemsEqual(actual, expected)

        actual = grid.get_4_adjacent_to(4, 3)
        expected = [[04, 60, 11, 42],
                    [04, 51, 99, 64],
                    [38, 17, 55, 04],
                    [70, 95, 23, 04],
                    [2, 99, 73, 4],
                    [4, 67, 45, 10],
                    [4, 79, 18, 40],
                    [98, 32, 71, 04]]
        self.assertItemsEqual(actual, expected)

        actual = grid.get_4_adjacent_to(3, 3)
        expected = [[23, 04, 60, 11],
                    [23, 71, 60, 28],
                    [52, 70, 95, 23],
                    [97, 40, 73, 23],
                    [8, 49, 31, 23],
                    [23, 51, 03, 67],
                    [23, 55, 81, 0],
                    [32, 47, 16, 23]]
        self.assertItemsEqual(actual, expected)

    def test_product(self):
        self.assertEquals(24, grid.product([1, 2, 3, 4]))
        self.assertEquals(120, grid.product([2, 3, 4, 5]))

    def test_solution(self):
        self.assertEquals(70600674, grid.get_largest_4_adjacent_product())

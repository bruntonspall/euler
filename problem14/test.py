import unittest
import collatz


class CollatzTest(unittest.TestCase):
    def test_collatz(self):
        self.assertEquals(5, collatz.collatz(10))
        self.assertEquals(16, collatz.collatz(5))
        self.assertEquals(8, collatz.collatz(16))
        self.assertEquals(4, collatz.collatz(8))
        self.assertEquals(2, collatz.collatz(4))
        self.assertEquals(1, collatz.collatz(2))

    def test_chain_length(self):
        self.assertEquals(4, collatz.chain_length(8))
        self.assertEquals({1: 1, 2: 2, 4: 3, 8: 4}, collatz.chain_cache)
        self.assertEquals(10, collatz.chain_length(13))
        self.assertEquals({1: 1, 2: 2, 4: 3, 5: 6, 8: 4, 10: 7, 13: 10, 16: 5, 20: 8, 40: 9}, collatz.chain_cache)
        self.assertEquals(8, collatz.chain_length(20))
        self.assertEquals({1: 1, 2: 2, 4: 3, 5: 6, 8: 4, 10: 7, 13: 10, 16: 5, 20: 8, 40: 9}, collatz.chain_cache)

    def test_solution(self):
        self.assertEquals(0, collatz.longest_chain_under(1000000))

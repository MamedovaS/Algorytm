import unittest

from Lab1 import Lab1


class TestLab1(unittest.TestCase):

    def setUp(self):
        self.lab1 = Lab1()

    def test_find_indexer(self):

        nums2 = [4, 2]
        target2 = 7
        result2 = self.lab1.find_indexer(nums2, target2)
        self.assertEqual(result2, -1)

        nums3 = []
        target3 = 5
        result3 = self.lab1.find_indexer(nums3, target3)
        self.assertEqual(result3, -1)


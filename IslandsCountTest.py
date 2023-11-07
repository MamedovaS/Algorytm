import unittest

from IslandCountTask import islands_count


class TestNumIslands(unittest.TestCase):
    def test_empty_land(self):
        grid = []
        self.assertEqual(islands_count(grid), 0)

    def test_single_island(self):
        grid = [
            ["1", "1", "0", "0", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "1", "0", "0"],
            ["0", "0", "0", "1", "1"]
        ]
        self.assertEqual(islands_count(grid), 1)

    def test_multiple_islands(self):
        grid = [
            ["1", "1", "0", "0", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "0", "0", "0"],
            ["0", "0", "0", "1", "1"],
            ["0", "0", "0", "1", "1"]
        ]
        self.assertEqual(islands_count(grid), 2)


if __name__ == '__main__':
    unittest.main()

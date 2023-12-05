import unittest

def count_pairs(N, pairs):
    count = 0
    for i in range(N):
        for j in range(i + 1, N):
            if pairs[i][0] != pairs[j][0] and pairs[i][0] != pairs[j][1] and pairs[i][1] != pairs[j][0] and pairs[i][
                1] != pairs[j][1]:
                count += 1
    return count


class TestCountPairs(unittest.TestCase):
    def test_count_pairs_example1(self):
        N = 3
        pairs = [[1, 2], [2, 4], [3, 5]]
        self.assertEqual(count_pairs(N, pairs), 2)

    def test_count_pairs_example2(self):
        N = 5
        pairs = [[1, 2], [2, 4], [1, 3], [3, 5], [8, 10]]
        self.assertEqual(count_pairs(N, pairs), 7)

    def test_count_pairs_custom_input(self):
        N = 4
        pairs = [[1, 2], [2, 3], [3, 4], [4, 5]]
        self.assertEqual(count_pairs(N, pairs), 3)

    def test_count_pairs_no_pairs(self):
        N = 3
        pairs = [[1, 3], [2, 4], [5, 6]]
        self.assertEqual(count_pairs(N, pairs), 3)

    def test_count_pairs_single_pair(self):
        N = 2
        pairs = [[1, 2], [3, 4]]
        self.assertEqual(count_pairs(N, pairs), 1)

if __name__ == '__main__':
    unittest.main()

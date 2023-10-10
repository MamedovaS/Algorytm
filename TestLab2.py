import unittest
import Lab2


class TestSimplifyCalendar(unittest.TestCase):

    def test_simplified_calendar(self):

        input_calendar = []
        expected_result = []
        self.assertEqual(Lab2.simplify_calendar(input_calendar), expected_result)

        input_calendar = [(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]
        expected_result = [(0, 1), (3, 8), (9, 12)]
        self.assertEqual(Lab2.simplify_calendar(input_calendar), expected_result)

        input_calendar = [(10, 20), (20, 30), (20, 40)]
        expected_result = [(10, 40)]
        self.assertEqual(Lab2.simplify_calendar(input_calendar), expected_result)


if __name__ == '__main__':
    unittest.main()

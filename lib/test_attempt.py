import unittest
from attempt import MakeAttempt
from mock import MagicMock


class TestMakeAttempt(unittest.TestCase):

    def test_create_attempt(self):
        ma = MakeAttempt([1, 2, 3, 4])
        self.assertIsNotNone(ma.codes)

    def test_duplicate_colours(self):
        with self.assertRaises(ValueError) as error:
            ma = MakeAttempt([1, 2, 3])

    def test_duplicate_colours_repeat(self):
        with self.assertRaises(ValueError) as error:
            ma = MakeAttempt([1, 2, 3, 3])

    def test_colour_not_valid(self):
        with self.assertRaises(ValueError) as error:
            ma = MakeAttempt([1, 2, 3, 9])

    def test_score_pass_all_black(self):
        scode = [1, 2, 3, 4]
        ma = MakeAttempt([1, 2, 3, 4])
        score_value = ma.score(scode)
        self.assertListEqual(sorted(score_value), sorted([7, 7, 7, 7]))

    def test_score_pass_two_white_two_black(self):
        scode = [1, 2, 3, 4]
        ma = MakeAttempt([1, 2, 6, 5])
        score_value = ma.score(scode)
        self.assertListEqual(sorted(score_value), sorted([7, 7, 0, 0]))


if __name__ == '__main__':
    unittest.main()

import unittest
from secretcode import SecretCode


class TestSetSecretCode(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.sc = SecretCode()

    def test_set_secret_code(self):
        codes = self.sc.set_secret_code()
        assert len(codes) == 4

    def test_unique_colours(self):
        codes = self.sc.set_secret_code()
        assert len(set(codes)) == 4

    def test_available_colours(self):
        self.assertEqual(len(SecretCode.available_colours), 6)


if __name__ == '__main__':
    unittest.main()

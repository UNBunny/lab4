import unittest

from main import check_credentials


class TestCredentials(unittest.TestCase):
    def test_correct_credentials(self):
        self.assertTrue(check_credentials('admin', 'admin'))

    def test_incorrect_credentials(self):
        self.assertFalse(check_credentials('wrong_username', 'wrong_password'))


if __name__ == '__main__':
    unittest.main()

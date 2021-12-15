import unittest
from electr import Electr

class TestHamster(unittest.TestCase):

    def test_case_1(self):
        e = Electr()
        e.read_data("electr_in_test.txt")
        self.assertEqual(e.counting_length_of_lines(), 10.0)


if __name__ == '__main__':
    unittest.main()
import unittest
from main import *

class TestStringMethods(unittest.TestCase):

    def test_1_quille(self):
        self.assertEqual(addition(9, 16), 25)

if __name__ == '__main__':
    unittest.main()


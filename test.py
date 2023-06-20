import unittest
from main import *

class TestStringMethods(unittest.TestCase):

    def test_1_quille(self):
        self.assertEqual(calcule_lancer([3]), 3)

    def test_multiple_quilles(self):
        self.assertEqual(calcule_lancer([3, 5]), 2)

    def test_multiple_lancers(self):
        self.assertEqual(calcule_multiple_lancers([[6], [2, 5], [4, 7, 9]]), 11)

    def test_est_gagnant(self):
        self.assertEqual(est_gagnant([[12], [12], [12], [12], [1, 7]]), True)

    def test_multiple_lancers_overflow(self):
        self.assertEqual(calcule_multiple_lancers([[12], [12], [12], [12], [1, 2, 3]]), 25)
    
    def test_multiple_lancers_overflow2(self):
        self.assertEqual(calcule_multiple_lancers([[12], [12], [12], [12], [1, 2, 3], [3]]), 28)

    def test_non_elimine_plus_de_3(self):
        self.assertEqual(est_elimine([[3, 10], [], [], [4], [], [6, 8]]), False)
    
    def test_est_elimine(self):
        self.assertEqual(est_elimine([[3, 10], [], [], [], [6, 8]]), True)

if __name__ == '__main__':
    unittest.main()


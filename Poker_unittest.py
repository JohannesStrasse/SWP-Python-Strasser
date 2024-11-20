import unittest
from Poker import pair, two_pair, three_of_a_kind, flush

class TestPokerMethods(unittest.TestCase):

    def test_pair(self):
        self.assertTrue(pair([('2', 'Herz'), ('2', 'Karo'), ('3', 'Pik'), ('4', 'Kreuz'), ('5', 'Herz')]))
        self.assertFalse(pair([('2', 'Herz'), ('3', 'Karo'), ('4', 'Pik'), ('5', 'Kreuz'), ('6', 'Herz')]))

    def test_two_pair(self):
        self.assertTrue(two_pair([('2', 'Herz'), ('2', 'Karo'), ('3', 'Pik'), ('3', 'Kreuz'), ('5', 'Herz')]))
        self.assertFalse(two_pair([('2', 'Herz'), ('3', 'Karo'), ('4', 'Pik'), ('5', 'Kreuz'), ('6', 'Herz')]))

    def test_three_of_a_kind(self):
        self.assertTrue(three_of_a_kind([('2', 'Herz'), ('2', 'Karo'), ('2', 'Pik'), ('4', 'Kreuz'), ('5', 'Herz')]))
        self.assertFalse(three_of_a_kind([('2', 'Herz'), ('3', 'Karo'), ('4', 'Pik'), ('5', 'Kreuz'), ('6', 'Herz')]))

    def test_flush(self):
        self.assertTrue(flush([('2', 'Herz'), ('3', 'Herz'), ('4', 'Herz'), ('5', 'Herz'), ('6', 'Herz')]))
        self.assertFalse(flush([('2', 'Herz'), ('3', 'Karo'), ('4', 'Herz'), ('5', 'Herz'), ('6', 'Herz')]))

if __name__ == '__main__':
    unittest.main()

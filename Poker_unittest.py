import unittest
import Poker

class TestPokerMethods(unittest.TestCase):

    def test_pair(self):
        karten = [('2', 'Herz'), ('2', 'Karo'), ('3', 'Pik'), ('4', 'Kreuz'), ('5', 'Herz')]
        self.assertTrue(Poker.pair(karten))

    def test_two_pair(self):
        karten = [('2', 'Herz'), ('2', 'Karo'), ('3', 'Pik'), ('3', 'Kreuz'), ('5', 'Herz')]
        self.assertTrue(Poker.two_pair(karten))

    def test_three_of_a_kind(self):
        karten = [('2', 'Herz'), ('2', 'Karo'), ('2', 'Pik'), ('4', 'Kreuz'), ('5', 'Herz')]
        self.assertTrue(Poker.three_of_a_kind(karten))

    def test_quads(self):
        karten = [('2', 'Herz'), ('2', 'Karo'), ('2', 'Pik'), ('2', 'Kreuz'), ('5', 'Herz')]
        self.assertTrue(Poker.quads(karten))

    def test_flush(self):
        karten = [('2', 'Herz'), ('3', 'Herz'), ('4', 'Herz'), ('5', 'Herz'), ('6', 'Herz')]
        self.assertTrue(Poker.flush(karten))

    def test_straight(self):
        karten = [('2', 'Herz'), ('3', 'Karo'), ('4', 'Pik'), ('5', 'Kreuz'), ('6', 'Herz')]
        self.assertTrue(Poker.straight(karten))

    def test_full_house(self):
        karten = [('2', 'Herz'), ('2', 'Karo'), ('3', 'Pik'), ('3', 'Kreuz'), ('3', 'Herz')]
        self.assertTrue(Poker.full_house(karten))

    def test_royal_flush(self):
        karten = [('10', 'Herz'), ('J', 'Herz'), ('Q', 'Herz'), ('K', 'Herz'), ('A', 'Herz')]
        self.assertTrue(Poker.royal_flush(karten))

if __name__ == "__main__":
    unittest.main()

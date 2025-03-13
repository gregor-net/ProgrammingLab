from unittest import TestCase
from somma import somma

class TestSomma(TestCase):
    def test_somma(self):
        self.assertEqual(somma(1,1), 2)
        self.assertEqual(somma(1.5,2.5), 4)

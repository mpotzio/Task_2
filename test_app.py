
from app import convert_usd_to_eur, convert_eur_to_usd

import unittest
from app import convert_usd_to_eur

class TestApp(unittest.TestCase):
    def test_convert(self):
        self.assertEqual(convert_usd_to_eur(10), 9.0)

if __name__ == '__main__':
    unittest.main()


import unittest
import hexip


class TestHexIP(unittest.TestCase):

    def test_valid(self):
        ipstr = "192.168.24.203"
        expected = "C0A818CB"
        self.assertEqual(hexip.ip4_to_hex(ipstr), expected)

    def test_valid_ranges(self):
        ipstr = "255.255.255.255"
        expected = "FFFFFFFF"
        self.assertEqual(hexip.ip4_to_hex(ipstr), expected)
        ipstr = "0.0.0.0"
        expected = "00000000"
        self.assertEqual(hexip.ip4_to_hex(ipstr), expected)

    def test_char_values(self):
        ipstr = "192.ape.24.203"
        with self.assertRaises(ValueError):
            hexip.ip4_to_hex(ipstr)

    def test_negative_values(self):
        ipstr = "192.-12.24.203"
        with self.assertRaises(AttributeError):
            hexip.ip4_to_hex(ipstr)

    def test_invalid_range_max(self):
        ipstr = "255.255.255.256"
        with self.assertRaises(AttributeError):
            hexip.ip4_to_hex(ipstr)

if __name__ == "__main__":
    unittest.main()

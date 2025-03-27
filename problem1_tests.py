import unittest
from problem1_code import determine_primes

class TestDeterminePrimes(unittest.TestCase):
    def test_primes_with_11(self):
        # Expect primes for 11 and exactly 2 traversals over the initial list
        result = determine_primes(11)
        expected = ([2, 3, 5, 7, 11], 2)
        self.assertEqual(result, expected)

    def test_primes_with_22(self):
        # Expect primes for 22 and exactly 2 traversals over the initial list
        result = determine_primes(22)
        expected = ([2, 3, 5, 7, 11, 13, 17, 19], 2)
        self.assertEqual(result, expected)

    def test_invalid_input(self):
        # Passing a non-integer should raise an Exception
        with self.assertRaises(Exception):
            determine_primes("11")

if __name__ == '__main__':
    unittest.main()
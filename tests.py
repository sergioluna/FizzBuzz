import unittest

from main import is_perfect_square, is_prime

class TestFizzBuzz(unittest.TestCase):

    def test_is_prime_from_2_to_144(self):
        prime_numbers = {
            2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43,
            47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103,
            107, 109, 113, 127, 131, 137, 139
        }

        for n in range(2, 145):
            if n in prime_numbers:
                self.assertTrue(is_prime(n))
            else:
                self.assertFalse(is_prime(n))


    def test_is_perfect_square_from_2_to_144(self):
        perfect_squares = {
            4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144
        }

        for n in range(2, 145):
            if n in perfect_squares:
                self.assertTrue(is_perfect_square(n))
            else:
                self.assertFalse(is_perfect_square(n))

if __name__ == '__main__':
    unittest.main()
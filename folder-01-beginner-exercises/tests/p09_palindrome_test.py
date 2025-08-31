import unittest
from p09_palindrome import check_palindrome

class TestPalindrome(unittest.TestCase):
    # testing numbers to see if they are palindromes
    def test_palindrome(self):
        self.assertEqual(check_palindrome(1), True)
        self.assertEqual(check_palindrome(13), False)
        self.assertTrue(check_palindrome(121), True)
        self.assertTrue(check_palindrome(1221), True)
        self.assertFalse(check_palindrome(1223), False)

if __name__ == "__main__":
    unittest.main()
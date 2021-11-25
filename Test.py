#!/usr/bin/python3
# Test case for numerical sum
import unittest

from Prog1 import Summation


class TestSum(unittest.TestCase):
    def test_list_int(self):
        """
        Test case to find minimum in a list
        """
        data = [1,2,3,4]
        result = Summation(data)
        self.assertEqual(result, 10)


if __name__ == '__main__':
    unittest.main()

#!/usr/bin/env python3
"""
TestAccessNestedMap module
"""

import unittest
from parameterized import parameterized
import utils
# Assuming you have the utils module with
# access_nested_map function implemented


class TestAccessNestedMap(unittest.TestCase):
    """
    TestAccessNestedMap class that inherits from unittest.TestCase.
    """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected_result):
        """
        Test the access_nested_map function with different inputs.

        Args:
            nested_map (dict): The nested map to test with.
            path (tuple): The path to access the value in the nested map.
            expected_result (any): The expected result of the function.

        Returns:
            None.
        """
        self.assertEqual(utils.access_nested_map(nested_map, path),
                expected_result)

if __name__ == "__main__":
    unittest.main()

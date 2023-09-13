#!/usr/bin/env python3
"""
TestAccessNestedMap module
"""

import unittest
from parameterized import parameterized
from unittest.mock import patch, Mock
import utils
# Assuming you have the utils module with
# access_nested_map and get_json functions implemented


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

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b")),
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """
        Test the access_nested_map function for expected exceptions.

        Args:
            nested_map (dict): The nested map to test with.
            path (tuple): The path to access the value in the nested map.

        Returns:
            None.
        """
        with self.assertRaises(KeyError):
            utils.access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """
    TestGetJson class that inherits from unittest.TestCase.
    """

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    @patch('utils.requests.get')
    def test_get_json(self, test_url, test_payload, mock_get):
        """
        Test the get_json function.

        Args:
            test_url (str): The URL to test the get_json function with.
            test_payload (dict): The expected payload to be returned by
            get_json.
            mock_get (MagicMock): The patched mock for requests.get.

        Returns:
            None.
        """
        mock_response = Mock()
        mock_response.json.return_value = test_payload
        mock_get.return_value = mock_response

        result = utils.get_json(test_url)

        mock_get.assert_called_once_with(test_url)
        self.assertEqual(result, test_payload)


class TestMemoize(unittest.TestCase):
    """
    TestMemoize class that inherits from unittest.TestCase.
    """

    class TestClass:

        def a_method(self):
            return 42

        @utils.memoize
        def a_property(self):
            return self.a_method()

    @patch.object(TestClass, 'a_method')
    def test_memoize(self, mock_a_method):
        """
        Test the memoize decorator.

        Args:
            mock_a_method (MagicMock): The mocked a_method.

        Returns:
            None.
        """
        instance = self.TestClass()

        # Call the property twice
        result1 = instance.a_property
        result2 = instance.a_property

        # Ensure that a_method is called only once
        mock_a_method.assert_called_once()

        # Ensure that the results are the same
        self.assertEqual(result1, result2)


if __name__ == "__main__":
    unittest.main()

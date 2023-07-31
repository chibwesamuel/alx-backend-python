#!/usr/bin/env python3
"""
TestGithubOrgClient module
"""

import unittest
from unittest.mock import patch
from client import GithubOrgClient
from fixtures import org_payload, repos_payload, expected_repos, apache2_repos


class TestGithubOrgClient(unittest.TestCase):
    """
    TestGithubOrgClient class that inherits from unittest.TestCase.
    """

    @patch('client.GithubOrgClient.get_json', return_value=org_payload)
    @parameterized.expand([('google',), ('abc',)])
    def test_org(self, org):
        """
        Test the GithubOrgClient.org method.

        Args:
            org (str): The organization name to test with.

        Returns:
            None.
        """
        client = GithubOrgClient(org)
        self.assertEqual(client.org, org_payload)

    @patch('client.GithubOrgClient.org', return_value=org_payload)
    def test_public_repos_url(self, mock_org):
        """
        Test the GithubOrgClient._public_repos_url property.

        Args:
            mock_org (MagicMock): The mocked org property.

        Returns:
            None.
        """
        client = GithubOrgClient('test')
        expected_url = org_payload['repos_url']
        self.assertEqual(client._public_repos_url, expected_url)

    @patch('client.GithubOrgClient.get_json', return_value=repos_payload)
    @patch('client.GithubOrgClient._public_repos_url', new_callable=property)
    def test_public_repos(self, mock_repos_url, mock_get_json):
        """
        Test the GithubOrgClient.public_repos method.

        Args:
            mock_repos_url (MagicMock): The mocked _public_repos_url property.
            mock_get_json (MagicMock): The mocked get_json function.

        Returns:
            None.
        """
        client = GithubOrgClient('test')
        repos = client.public_repos()
        self.assertEqual(repos, expected_repos)
        mock_repos_url.assert_called_once()
        mock_get_json.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
    ])
    def test_has_license(self, repo, license_key, expected_result):
        """
        Test the GithubOrgClient.has_license method.

        Args:
            repo (dict): The repository object.
            license_key (str): The license key to test with.
            expected_result (bool): The expected result of the method.

        Returns:
            None.
        """
        client = GithubOrgClient('test')
        result = client.has_license(repo, license_key)
        self.assertEqual(result, expected_result)

    @parameterized_class([{'org': 'test', 'repos': apache2_repos}])
    def test_public_repos_integration(self, mock_get_json, org, repos):
        """
        Integration test for GithubOrgClient.public_repos method.

        Args:
            mock_get_json (MagicMock): The mocked get_json function.
            org (str): The organization name to test with.
            repos (list): The list of mocked repositories.

        Returns:
            None.
        """
        client = GithubOrgClient(org)
        mock_get_json.return_value = repos_payload
        self.assertEqual(client.public_repos(), repos)

    @parameterized_class([{'org': 'test', 'repos': apache2_repos}])
    def test_public_repos_with_license_integration(self, mock_get_json, org,
    repos):
        """
        Integration test for GithubOrgClient.public_repos with license
        argument.

        Args:
            mock_get_json (MagicMock): The mocked get_json function.
            org (str): The organization name to test with.
            repos (list): The list of mocked repositories.

        Returns:
            None.
        """
        client = GithubOrgClient(org)
        mock_get_json.return_value = repos_payload
        filtered_repos = client.public_repos('apache-2.0')
        self.assertEqual(filtered_repos, apache2_repos)


if __name__ == "__main__":
    unittest.main()

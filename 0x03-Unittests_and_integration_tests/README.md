# Unittests and Integration Tests

In this project, I will be writing unit tests and integration tests for various functions and methods using Python's `unittest` framework and the `parameterized` module. The main goal is to ensure that the code functions as expected, handles different inputs and scenarios effectively, and maintains a high level of code quality.

## Table of Contents

- [Tasks](#tasks)
  - [0. Parameterize a unit test](#0-parameterize-a-unit-test)
  - [1. Parameterize a unit test](#1-parameterize-a-unit-test)
  - [2. Mock HTTP calls](#2-mock-http-calls)
  - [3. Parameterize and patch](#3-parameterize-and-patch)
  - [4. Parameterize and patch as decorators](#4-parameterize-and-patch-as-decorators)
  - [5. Mocking a property](#5-mocking-a-property)
  - [6. More patching](#6-more-patching)
  - [7. Parameterize](#7-parameterize)
  - [8. Integration test: fixtures](#8-integration-test-fixtures)
  - [9. Integration tests](#9-integration-tests)

## Tasks

### 0. Parameterize a unit test

First, I will familiarize myself with the `utils.access_nested_map` function and understand its purpose. Then, I will create a `TestAccessNestedMap` class that inherits from `unittest.TestCase` and write unit tests for the function. Using `@parameterized.expand`, I will test the function with different inputs, ensuring it returns the expected results.

### 1. Parameterize a unit test

In this task, I will implement `TestAccessNestedMap.test_access_nested_map_exception` to test that the `utils.access_nested_map` function raises a `KeyError` for certain inputs. Using `@parameterized.expand`, I will test the function for specific inputs and check that the correct exception is raised with the expected message.

### 2. Mock HTTP calls

Next, I will familiarize myself with the `utils.get_json` function and define the `TestGetJson(unittest.TestCase)` class. I will write a test method `test_get_json` to check that `utils.get_json` returns the expected result. Using `unittest.mock.patch`, I will mock the `requests.get` method and ensure it returns a `Mock` object with a `json` method. Then, I will parametrize the test with different test URLs and payloads.

### 3. Parameterize and patch

In this task, I will read about memoization and familiarize myself with the `utils.memoize` decorator. I will implement the `TestMemoize(unittest.TestCase)` class with a test method `test_memoize`. Inside the method, I will define a class `TestClass` with a method and a memoized property. Using `unittest.mock.patch`, I will mock the method and test that the property is called only once using `assert_called_once`.

### 4. Parameterize and patch as decorators

Next, I will familiarize myself with the `client.GithubOrgClient` class. I will create the `TestGithubOrgClient(unittest.TestCase)` class and implement the `test_org` method. To mock `utils.get_json`, I will use `@patch` as a decorator and ensure it returns the expected fixtures. I will also parametrize the test with different org examples to pass to `GithubOrgClient`.

### 5. Mocking a property

I will implement the `test_public_repos_url` method to unit-test `GithubOrgClient._public_repos_url`. Using `patch` as a context manager, I will mock `GithubOrgClient.org` and make it return a known payload. Then, I will test that the result of `_public_repos_url` is the expected one based on the mocked payload.

### 6. More patching

In this task, I will implement `TestGithubOrgClient.test_public_repos` to unit-test `GithubOrgClient.public_repos`. Using `@patch` as a decorator, I will mock `utils.get_json` and make it return a payload of my choice. I will also use `patch` as a context manager to mock `GithubOrgClient._public_repos_url` and test that the list of repos is as expected. I will also ensure that the mocked property and `get_json` were called once.

### 7. Parameterize

I will implement `TestGithubOrgClient.test_has_license` to unit-test `GithubOrgClient.has_license`. By parametrizing the test with different repos and the expected returned values, I will check that the function behaves as expected.

### 8. Integration test: fixtures

In this task, I will create the `TestIntegrationGithubOrgClient(unittest.TestCase)` class and implement the `setUpClass` and `tearDownClass` methods. Using `@parameterized_class`, I will parameterize the class with fixtures found in `fixtures.py`. I will implement the `setUpClass` method to mock `requests.get` and return example payloads from the fixtures. Finally, I will implement the `tearDownClass` method to stop the patcher.

### 9. Integration tests

Lastly, I will implement the `test_public_repos` method to test `GithubOrgClient.public_repos`. Using the fixtures, I will check that the method returns the expected results. I will also implement `test_public_repos_with_license` to test `GithubOrgClient.public_repos` with the argument `license="apache-2.0"` and verify that the result matches the expected value from the fixtures.

---

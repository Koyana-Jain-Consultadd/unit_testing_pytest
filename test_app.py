# test_app.py (handling exceptions under test)
import unittest
from unittest.mock import patch
from app import DataFetcher
import requests
import responses

class TestDataFetcher(unittest.TestCase):
    @patch('app.requests.get')
    def test_fetch_data_from_api_success(self, mocked_get):
        # Mock a successful API response
        mocked_get.return_value.status_code = 200
        mocked_get.return_value.json.return_value = {'data': 'example'}

        data_fetcher = DataFetcher()
        result = data_fetcher.fetch_data_from_api('https://api.example.com')

        self.assertEqual(result, {'data': 'example'})

    @patch('app.requests.get')
    def test_fetch_data_from_api_failure(self, mocked_get):
        # Mock a failed API response (e.g., 404)
        mocked_get.return_value.status_code = 404
        mocked_get.return_value.json.return_value = None  # Return None for JSON data in case of failure

        data_fetcher = DataFetcher()
        result = data_fetcher.fetch_data_from_api('https://api.example.com')

        self.assertIsNone(result)

    @patch('app.requests.get')
    def test_fetch_data_from_api_exception(self, mocked_get):
        # Mock an exception (e.g., network error)
        mocked_get.side_effect = requests.exceptions.RequestException('Network Error')

        data_fetcher = DataFetcher()
        result = data_fetcher.fetch_data_from_api('https://api.example.com')

        self.assertIsNone(result)

    

    @responses.activate  # Activate responses for this test case
    def test_my_api_function(self):
        # Mock the API response
        responses.add(responses.GET, 'https://api.example.com', json={'key': 'value'}, status=200)

        # Call your function that makes the HTTP request
        response = requests.get('https://api.example.com')

        # Assertions
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'key': 'value'})


if __name__ == '__main__':
    unittest.main()

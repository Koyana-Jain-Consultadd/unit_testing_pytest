# test_weather.py
import unittest
from unittest.mock import patch
from weather import get_weather

class TestWeather(unittest.TestCase):
    @patch('weather.requests.get')
    def test_get_weather_success(self, mocked_get):
        # Mocking the response from the external API
        mocked_response = {'temperature': 25, 'conditions': 'sunny'}
        mocked_get.return_value.status_code = 200
        mocked_get.return_value.json.return_value = mocked_response
        
        # Calling the function under test
        result = get_weather('indore')
        print('---------------result from function---------------',result)
        print('---------------result from mocked response---------------',mocked_response)
        # Asserting that the function returned the expected result
        self.assertEqual(result, mocked_response)
        
        # Asserting that requests.get was called with the correct URL
        mocked_get.assert_called_once_with('https://api.weather.com/indore')
        
    @patch('weather.requests.get')
    def test_get_weather_failure(self, mocked_get):
        # Mocking the failed response from the external API
        mocked_get.return_value.status_code = 404
        
        # Calling the function under test
        result = get_weather('mumbai')
        
        # Asserting that the function returned None for failed request
        self.assertIsNone(result)
        
        # Asserting that requests.get was called with the correct URL
        mocked_get.assert_called_once_with('https://api.weather.com/mumbai')

if __name__ == '__main__':
    unittest.main()

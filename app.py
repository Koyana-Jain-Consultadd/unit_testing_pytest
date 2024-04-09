import requests

class DataFetcher:
    def fetch_data_from_api(self, url):
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise an exception for non-2xx status codes
            return response.json()
        except requests.exceptions.RequestException as e:
            # Handle network errors or server errors
            return None

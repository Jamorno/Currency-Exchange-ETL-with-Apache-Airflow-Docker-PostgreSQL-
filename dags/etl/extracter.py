import logging, requests
from dotenv import load_dotenv

load_dotenv()

class DataExtract:
    def __init__(self, api_url):
        self.api_url = api_url

    def extract_data(self):
        try:
            response = requests.get(self.api_url)
            response.raise_for_status()
            data = response.json()
            logging.info("Fetched data from API.")
            return data
        except Exception as e:
            logging.error(f"DEBUG: Failed to fetch API: {e}")
            return None
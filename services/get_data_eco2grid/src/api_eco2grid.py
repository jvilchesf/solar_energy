import requests
from typing import Dict, Any
from loguru import logger

class API_eco2grid:
    def __init__(
        self,
        api_key: str,
        limit: int,
        zone_code: str,
        start: str,
        end: str,
    ):
        self.api_key = api_key
        # Include API key and secret in the URL path
        self.base_url = f"https://eco2grid.com/green-grid-compass/co2intensity/co2/detailed/hourly"

        # Define the parameters
        self.params = {
            "apikey": self.api_key,  # Add API key as a query parameter
            "limit": limit,
            "zone_code": zone_code,
            "start": start,
            "end": end,
            "emmision_scope": "operational"
        }

    def get_data(self) -> Dict[str, Any]:
        """
        Function to get data from the api through requests
        
        Returns:
            Dict[str, Any]: The data from the api
        """
        try:

            logger.info(f"Making request to {self.base_url}")
            
            # requests data from the api
            response = requests.get(
                self.base_url, 
                params=self.params
            )
            
            # Parse response as a json dictionary
            response.raise_for_status()
            data = response.json()
            
            return data
        except Exception as e:
            logger.error(f"HTTP error occurred: {str(e)}")
            return None
        
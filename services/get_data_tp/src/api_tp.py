import requests
import xmltodict
from typing import Dict, Any
from loguru import logger
from model import tp_record
class API_TP:
    def __init__(
        self,
        api_key: str,
        base_url: str
    ):
        self.api_key = api_key
        # Include API key and secret in the URL path
        self.base_url = base_url 

        self.headers = {
            "Accept": "application/xml"  # Specify that we want XML response
        }

        self.payload = {}

    def get_data_generation_per_production_type(
        self,
        document_type: str,
        process_type: str,
        in_domain: str,
        period_start: str,
        temp_period_end: str
        ) -> list[dict]:
        """
        Function to get data from the api through requests
        
        Returns:
            Dict[str, Any]: The data from the api
        """
        try:
            
            #Set url for the request
            url = f"{self.base_url}?documentType={document_type}&processType={process_type}&in_Domain={in_domain}&periodStart={period_start}&periodEnd={temp_period_end}&securityToken={self.api_key}" 

            logger.info(f"Making request to {url}")

            # requests data from the api
            response = requests.request(
                method="GET",
                url=url, 
                headers=self.headers
            )
            
            # Parse response as a json dictionary

            # Convert XML to dictionary
            xml_data = response.text
            json_data = xmltodict.parse(xml_data)

            # Get timeserie data from the json_data
            time_series = json_data['GL_MarketDocument']['TimeSeries']

            # loop over time_series and save data in a list of dicts
            data_list = []
            for element in time_series:
                breakpoint()
                #Save data in a pydantic model class
                
            return data_list
        except Exception as e:
            logger.error(f"HTTP error occurred: {str(e)}")
            return None
        
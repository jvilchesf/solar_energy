from api_eco2grid import API_eco2grid
from config import Settings

def main(api: API):
 
    data = api.get_data()

    breakpoint()
    print(data)

    
if __name__ == "__main__":

    # Initialize the enviromental variables
    settings = Settings()

    # Initialize the API
    api = API(
        api_key=settings.api_key,
        limit=settings.limit,
        zone_code=settings.zone_code,
        start=settings.start,
        end=settings.end
    )

    main(api)

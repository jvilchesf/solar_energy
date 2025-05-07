from api_tp import API_TP
from config import Settings
from datetime import datetime, timedelta
def main(
    api: API_TP,
    document_type: str,
    process_type: str,
    in_domain: str,
    period_start: str
    ):
 
    # Set period end has today, make it dinamically based on datetime now
    #period_end = datetime.now().strftime("%Y%m%d%H%M")
    
    #test period end time
    period_end = "202501020000"

    while period_start < period_end:

        # set a temp period_end increasing period_start by 1 hour
        temp_period_end = (datetime.strptime(period_start, "%Y%m%d%H%M") + timedelta(hours=1)).strftime("%Y%m%d%H%M")

        # Get data from the api
        data = api.get_data_generation_per_production_type(
            document_type,
            process_type,
            in_domain,
            period_start,
            temp_period_end
            )

        print(data) 
        breakpoint()

        # Increment period start by 1 hour
        period_start = (datetime.strptime(period_start, "%Y%m%d%H%M") + timedelta(hours=1)).strftime("%Y%m%d%H%M")
    
if __name__ == "__main__":

    # Initialize the enviromental variables
    settings = Settings()

    # Initialize the API
    api = API_TP(
        api_key=settings.api_key,
        base_url=settings.base_url
    )

    main(
        api=api,
        document_type=settings.document_type,
        process_type=settings.process_type,
        in_domain=settings.in_domain,
        period_start=settings.period_start
    )

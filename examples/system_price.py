# This script demonstrates the use of methods from the IndicativeImbalanceSettlementApi
# to retrieve settlement system prices data from the Elexon API.


from datetime import datetime
import pandas as pd
from elexonpy.api_client import ApiClient
from elexonpy.api.indicative_imbalance_settlement_api import IndicativeImbalanceSettlementApi

# Initialize API client
api_client = ApiClient()
imbalance_settlement_api = IndicativeImbalanceSettlementApi(api_client)


# Define settlement date
settlement_date = '2024-07-02'

try:
    # Fetch system prices data from API
    response = imbalance_settlement_api.balancing_settlement_system_prices_settlement_date_get(
        settlement_date=settlement_date,
        format='json'
    )

    # Convert response to DataFrame
    df = pd.DataFrame([data.to_dict() for data in response.data])

    # Print DataFrame
    print("\n--- Settlement System Prices Data ---")
    print(df.head())

except Exception as e:
    print(f"Error fetching settlement system prices data: {str(e)}")
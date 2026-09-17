import config
import requests

def get_live_prices(coin_ids, currency ="usd"):
    endpoint = f"{config.BASE_URL}/simple/price"
    params = {
        "ids": ",".join(coin_ids), # e.g., "bitcoin,ethereum"
        "vs_currencies": currency,
        "include_24hr_change": "true",
        "include_market_cap": "true"
    }

    response = requests.get(endpoint, headers=config.headers, params=params)
    response.raise_for_status() # Raises an error for bad HTTP responses
    return response.json()


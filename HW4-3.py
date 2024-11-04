from datetime import datetime
import time
import requests
import pandas as pd

if __name__ == '__main__':
    currency_df = pd.DataFrame(columns=['Время', 'USD/EUR'])
    url = "https://api.exchangerate-api.com/v4/latest/USD"
    while True:
        response = requests.get(url).json()
        price = response["rates"]["RUB"]
        time_of_request = datetime.fromtimestamp(response["time_last_updated"]).strftime('%Y-%m-%d %H:%M:%S')
        currency_df.loc[len(currency_df)] = [time_of_request, price]
        print(currency_df)
        time.sleep(1800)
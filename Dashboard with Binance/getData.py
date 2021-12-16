# Importing libraries 
from binance.client import Client
import configparser
import pandas as pd

# Loading keys from config file
config = configparser.ConfigParser()
config.read_file(open('E:\SEM-5\G1 - DATA VISUALIZATION\J Component\Dashboard with Binance\secret.cfg'))
actual_api_key = config.get('BINANCE', 'ACTUAL_API_KEY')
actual_secret_key = config.get('BINANCE', 'ACTUAL_SECRET_KEY')

client = Client(actual_api_key, actual_secret_key)

# Getting earliest timestamp availble (on Binance)
earliest_timestamp = client._get_earliest_valid_timestamp('ETHUSDT', '1d')  # Here "ETHUSDT" is a trading pair and "1d" is time interval
print(earliest_timestamp)

# Getting historical data (candle data or kline)
candle = client.get_historical_klines("ADAUSDT", "1d", earliest_timestamp, limit=1000)

cand_df = pd.DataFrame(candle, columns=['dateTime', 'open', 'high', 'low', 'close', 'volume', 'closeTime', 'quoteAssetVolume', 'numberOfTrades', 'takerBuyBaseVol', 'takerBuyQuoteVol', 'ignore'])
cand_df.dateTime = pd.to_datetime(cand_df.dateTime, unit='ms')
cand_df.closeTime = pd.to_datetime(cand_df.closeTime, unit='ms')
cand_df.set_index('dateTime', inplace=True)
cand_df.to_csv('./Candles/ada_candle.csv')
print('Done')
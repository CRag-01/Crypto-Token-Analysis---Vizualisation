# Importing libraries 
from binance.client import Client
import configparser

# Loading keys from config file
config = configparser.ConfigParser()
config.read_file(open('E:\SEM-5\G1 - DATA VISUALIZATION\J Component\Dashboard with Binance\secret.cfg'))
test_api_key = config.get('BINANCE', 'TEST_API_KEY')
test_secret_key = config.get('BINANCE', 'TEST_SECRET_KEY')

client = Client(test_api_key, test_secret_key)

client.API_URL = 'https://testnet.binance.vision/api'  # To change endpoint URL for test account  

info = client.get_account()  # Getting account info

print(info)


# Testing with Samples

print('\nBTC: ')
balance = client.get_asset_balance(asset='BTC')
print (balance)

print('\nBNB: ')
balance = client.get_asset_balance(asset='BNB')
print (balance)

print('\nETH: ')
balance = client.get_asset_balance(asset='ETH')
print (balance)

print('\n BUSD: ')
balance = client.get_asset_balance(asset='BUSD')
print (balance)

print('\n LTC: ')
balance = client.get_asset_balance(asset='LTC')
print (balance)

print('\n TRX: ')
balance = client.get_asset_balance(asset='TRX')
print (balance)

print('\n USDT: ')
balance = client.get_asset_balance(asset='USDT')
print (balance)

print('\n XRP: ')
balance = client.get_asset_balance(asset='XRP')
print (balance)

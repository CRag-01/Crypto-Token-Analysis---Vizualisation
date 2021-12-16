# STREAMING DATA - WEB SCOKET
# Importing libraries 
from binance.client import Client
import configparser
from binance.websockets import BinanceSocketManager
from twisted.internet import reactor 
import time

# Loading keys from config file
config = configparser.ConfigParser()
config.read_file(open('E:\SEM-5\G1 - DATA VISUALIZATION\J Component\Dashboard with Binance\secret.cfg'))
actual_api_key = config.get('BINANCE', 'ACTUAL_API_KEY')
actual_secret_key = config.get('BINANCE', 'ACTUAL_SECRET_KEY')

client = Client(actual_api_key, actual_secret_key)


def streaming_data_process(msg):
    """
    Function to process the received messages
    param msg: input message
    """
    print(f"message type: {msg['e']}")
    print(f"close price: {msg['c']}")
    print(f"best ask price: {msg['a']}")
    print(f"best bid price: {msg['b']}")
    print("---------------------------")
    
# Starting the WebSocket
bm = BinanceSocketManager(client)
conn_key = bm.start_symbol_ticker_socket('ETHUSDT', streaming_data_process)
bm.start()


# SLEEP FOR SOME TIME
time.sleep(10)



# TO CLOSE THE CONNECTION
# Stopping websocket
bm.stop_socket(conn_key)

# Websockets utilise a reactor loop from the Twisted library. Using the stop method above 
# will stop the websocket connection but it won’t stop the reactor loop so your code may 
# not exit when you expect.

# When you need to exit
reactor.stop()

import json
import os
import time
from web3 import Web3

def load_config():
    with open('config.json') as f:
        return json.load(f)

def main():
    config = load_config()
    print(f"Bot starting for {config['token_name']}...")
    # Simulate bot loop
    while True:
        print("Monitoring price and liquidity...")
        time.sleep(5)  # Simulate delay

if __name__ == "__main__":
    main()

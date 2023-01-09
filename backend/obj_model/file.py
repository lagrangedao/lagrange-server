import os

from dotenv import load_dotenv


class File:
    def __init__(self, filename, file_path):
        self.filename = filename
        self.chain_name = "polygon.mainnet"
        self.wallet_address = os.getenv('wallet_address')
        self.private_key = os.getenv('private_key')
        self.rpc_endpoint = os.getenv('rpc_endpoint')

        self.file_path = file_path
        self.upload_response = None
        self.payment_tx_hash = None



if __name__ == '__main__':
    load_dotenv("../../.env")
    file = File('n012.jpg', '../dataset/n009.jpg')

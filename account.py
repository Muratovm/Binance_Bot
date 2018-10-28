#binance import
from binance.client import Client

class Account:
    def __init__(self):
        self.client = self.login()
        self.balance = 0

    def login(self):
        api_key = 'P0OHQYQUI6H3Ve8jTuOZjjkKBWGjvbn6FqN7QbiRhKbe6SAInDLKPP6bE2kcVljL'
        api_secret = '4xEA8QBlbA10kgWUjNzCfViYid0e6tT2SozZkV8nweirSzoo3DPHfM5B4ZTP7Spg'
        client = Client(api_key, api_secret)
        return client



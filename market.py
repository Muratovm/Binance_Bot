from binance.client import Client
class Market:
    def __init__(self,client):
        self.client = client
        self.prices_snapshot = {}
        
    def market_buy(self):
        balance = self.client.get_asset_balance(asset='USDT')
        amount = float(balance["free"])
        depth = self.client.get_order_book(symbol="BTCUSDT",limit=5)
        bid = float(depth["asks"][0][0])
        price = round(amount/float(bid),6)-0.000001
        print(price)
        if amount > 3:
            order = self.client.order_market_buy(symbol='BTCUSDT',quantity=price)

    def market_sell(self):
        balance = self.client.get_asset_balance(asset='BTC')
        amount = round(float(balance["free"]),6)-0.000001
        print(amount)
        if amount > 0.0002:
            order = self.client.order_market_sell(symbol='BTCUSDT',quantity=amount)

    def update_prices(self):
        self.prices_snapshot = self.client.get_all_tickers()
        return self.prices_snapshot
    
    def current_prices(self):
        return self.client.get_all_tickers()

    def current_BTC_prices(self):
        lst = []
        for price in self.client.get_all_tickers():
            if price["symbol"][-3:] == "BTC":
                lst.append(price)
        return lst
        
    
        

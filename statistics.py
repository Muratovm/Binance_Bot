import matplotlib.pyplot as plt

class Statistics:
    def __init__(self):
        self.client = login()
        self.balance = 0

def get_depth(client):
    # get market depth
    depth = client.get_order_book(symbol='BNBBTC')
    return depth

def get_prices(client):
    # get all symbol prices
    prices = client.get_all_tickers()
    return prices

def sort_by_price():
    price_list = sorted(get_prices(client), key=lambda k: float(k['price']), reverse=True)
    for item in price_list:
        print(item)
        
def get_trade_graph(client, mysymbol):
    data = client.get_klines(symbol=mysymbol, interval=Client.KLINE_INTERVAL_1MINUTE)
    time            = np.zeros(len(data))
    opening         = np.zeros(len(data))
    high            = np.zeros(len(data))
    low             = np.zeros(len(data))
    volume          = np.zeros(len(data))
    index = 0
    for thing in data:
        time[index]             = thing[0]/100000
        opening[index]          = thing[1]
        high[index]             = thing[2]
        low[index]              = thing[3]
        volume[index]           = thing[5]
        index += 1
    plt.plot(time,opening)
    plt.plot(time,high)
    plt.plot(time,low)
    plt.show()

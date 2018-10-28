
#helper classes
from account import*
from statistics import*
from strategies import*
from market import*

if __name__ == "__main__":
    account = Account()
    market = Market(account.client)
    strategies = Strategies(account.client,market)
    #while True:
    #    strategies.get_up_down("BTCUSDT")
    #strategies.naive_spike()
    
    #market.current_BTC_prices()
    
    #while(True):
    #    strategies.naive_spike(1.01)

    strategies.increase_since_recording(0,1.01)
    


    
    
    

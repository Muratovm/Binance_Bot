#binance import
from binance.client import Client
#math imports
import numpy as np
import time

class Strategies:

    def __init__(self,client,market):
        self.client = client
        self.market = market
        

    def naive_spike(self, multiplier):
        self.market.update_prices()
        time.sleep(10)
        prices = self.market.current_prices()
        for i in range(len(prices)):
            if prices[i]["symbol"][-3:] == "BTC":
                past = float(self.market.prices_snapshot[i]["price"])
                new = float(prices[i]['price'])
                if(new >= multiplier*past):
                    print(prices[i]['symbol']+": "+str(past)+"--->"+str(new))
        print("---------------------------------------------------------------------")

    def increase_since_recording(self,seconds, multiplier):
        self.market.update_prices()
        while(True):
            #time.sleep(seconds)
            n = input("press to get update")
            prices = self.market.current_prices()
            going_up = []
            going_down = []
            for i in range(len(prices)):
                if prices[i]["symbol"][-3:] == "BTC":
                    past = float(self.market.prices_snapshot[i]["price"])
                    new = float(prices[i]['price'])
                    if new >= multiplier*past:
                        going_up.append((prices[i]['symbol'],past,new,float(new/past)))
                    if new <= past/multiplier:
                        going_down.append((prices[i]['symbol'],past,new,float(new/past)))
            print("GOING UP")
            going_up.sort(key=lambda x: x[3], reverse = True)
            for entry in going_up:         
                print("\t"+entry[0]+": "+str(entry[1])+"--->"+str(entry[2])+"_"*(50-len(entry[0])
                                                                               -len(str(entry[1]))
                                                                               -len(str(entry[2])))
                      +str(round((entry[3]-1)*100,3))+"%")
            print("GOING DOWN")
            going_down.sort(key=lambda x: x[3])
            for entry in going_down:         
                print("\t"+entry[0]+": "+str(entry[1])+"--->"+str(entry[2])+"_"*(49-len(entry[0])
                                                                               -len(str(entry[1]))
                                                                               -len(str(entry[2])))
                      +str(round((entry[3]-1)*100,3))+"%")
            print("---------------------------------------------------------------------")


    def get_up_down(self, mysymbol):
        data = self.client.get_klines(symbol=mysymbol, interval=Client.KLINE_INTERVAL_1MINUTE, limit=5)
        opening         = np.zeros(len(data))
        close            = np.zeros(len(data))
        volume          = np.zeros(len(data))
        index = 0
        for thing in data:
            opening[index]          = thing[1]
            close[index]             = thing[4]
            volume[index]           = thng[5]
            index += 1

        lst = []
        previous = close[0]
        for element in close:
            if previous < element:
                lst.append("up")
            elif previous > element:
                lst.append("down")
            else:
                lst.append("same")
            previous = element

        if lst[-2] == "up" and lst[-1] == "up":
            print("up -> buy")
            self.market.market_buy()
        elif lst[-2] == "down" and lst[-1] == "down":
            print("down -> sell")
            self.market.market_sell()
        print(lst[-2])
        print(lst[-1])
        print("BTC:"+self.client.get_asset_balance(asset='BTC')["free"])
        print("USDT:"+self.client.get_asset_balance(asset='USDT')["free"])

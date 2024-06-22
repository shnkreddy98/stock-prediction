import os
import yfinance as yf

class markets():

    def __init__(self, 
                 market_names_str, 
                 market_names_val = {}, 
                 market_names_dic = {}):
        self.market_names_str = market_names_str
        self.market_names_val = market_names_val
        self.market_names_dic = market_names_dic

    def get_market_fullname(short_name):
        msft = yf.Ticker(short_name)
        return msft.info['longName']


    def create_market_dict(self, 
                           market_names_str,
                           market_names_val,
                           market_names_dic):

        for market in market_names_str:
            market_names_val.append(os.listdir(f"stock_market_data/{market}/csv"))
            market_names_dic[market] = {}

        not_found = []

        for i, market in enumerate(market_names_str):
            for company in market_names_val[i]:
                short_name = str(company.split(".")[0])
                try:
                    market_names_dic[market][short_name] = self.get_market_fullname(short_name)
                except:
                    not_found.append([market, short_name])

        return market_names_str, market_names_val, market_names_dic, not_found
    
    



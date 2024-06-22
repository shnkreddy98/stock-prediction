import pickle
import markets

if __name__ == "__main__":

    try:
        print("Is this the first run?")
        first_run = bool(input('1 for yes, 0 for no \n'))
    except:
        print('Input number wrong')

    if first_run:
        market_names_str, market_names_val, market_names_dic, not_found = markets.create_market_dict()
        with open('stock_names.pickle', 'wb') as handle:
            pickle.dump(market_names_dic, handle, protocol=pickle.HIGHEST_PROTOCOL)

    else:
        with open('filename.pickle', 'rb') as handle:
            market_names_dic = pickle.load(handle)


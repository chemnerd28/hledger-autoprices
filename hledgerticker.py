from yahoo_fin.stock_info import get_live_price
from datetime import date

def grabPrice():
    for i in tickers:
        with open("2021.prices", 'a+') as file1:
            live_price = '%.2f'%(get_live_price(i))
            file1.write ("\n" + "P ")
            file1.write (date.today().strftime('%Y-%m-%d'))
            file1.write (" " + i + " " + str(live_price))

tickers = ["GOOG","AMZN","SPY","AOR","QQQ"]

ask = input("any new tickers? Y/N")
if ask == "N":
    grabPrice()
else:
    newTicker = input("what new ticker do you want to add?")
    tickers.append(newTicker)
    grabPrice()

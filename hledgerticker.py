from yahoo_fin.stock_info import get_live_price
from datetime import date

def grabPrice():
    print("grabbing current price data for the following:", openingTickerList)
    for i in openingTickerList:
        with open("2021.prices", 'a+') as file1:
            live_price = '%.2f'%(get_live_price(i))
            file1.write ("P ")
            file1.write (date.today().strftime('%Y-%m-%d'))
            file1.write (" " + i + " " + live_price + "\n")

with open("ticker.symbols", 'r') as tickerSymbols:
    openingTickerList = []
    for line in tickerSymbols:
        openingTickerList.append(line.strip('\n'))

ask = input("Do you have any new ticker symbols to add? Y/N")

if ask == "N":
    grabPrice()
else:
    newTicker = input("what new tickers do you want to add? (Split with comma, no spaces)")
    toAddSymbols = newTicker.split(',')
    openingTickerList.extend(toAddSymbols)
    with open ("ticker.symbols", 'w') as file2:
        for item in openingTickerList:
            file2.write(item + '\n')
    grabPrice()

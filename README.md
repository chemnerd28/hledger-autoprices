# hledger-autoprices

This program is intended to use the yahoo_fin API to pull real-time stock prices into a file using hledger prices syntax which can be utilized to calculate real-time gains/losses.  This uses python, so it cannot currently be incorporated directly into the hledger program, but can be incorporated through manipulation of ledgers. To install yahoo_fin, simply type `$ pip3 install yahoo_fin` and if you don't have python3 or pip3 installed, please refer to the respective manuals.

This is currently set up to print prices in hledger syntax to a new file, named `2021.prices`. This can then be incorporated into the main ledger for analysis by including `include 2021.prices` at any point of the main ledger.  For help with hledger analysis, see the hledger documentation: https://hledger.org/investments.html

Version 0.2-beta fixes and limitations:
- Implementation of ticker.symbols to store any tickers you add. They will be stored.
- Only able to look at current price.  Historical data unavailable at this time.
- cryptocurrencies have not been tested at this point.
- If you make a mistake, currently no way of erasing that mistake in ticker.symbols or 2021.prices without just going into them in a text editor and deleting the mistake.
- Unknown how hledger handles multiple entires for a single ticker per day.

Version 0.1-alpha known limitations:
- Currently, you must manually add tickers to the ticker list in hledgerticker.py, and ticker.symbols is not used.
- The option to add tickers to the list will work one time only.  The will append to the ticker list and pull the price; however, it will not be on the list during the next run.  This will be fixed in the next release. 

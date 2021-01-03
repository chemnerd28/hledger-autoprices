# hledger-autoprices

This program is intended to use the yahoo_fin API to pull real-time stock prices into file in hledger syntax which can be utilized to calculate real-time gains/losses.  This uses python, so it cannot currently be incorporated directly into the hledger program. To install yahoo_fin, simply type '$ pip3 install yahoo_fin' and if you don't have python3 or pip3 installed, please refer to the respective manuals.

Version 0.1-alpha 
known limitations:
- Currently, you must manually add tickers to the ticker list in hledgerticker.py, and ticker.symbols is not used.
- The option to add tickers to the list will work one time only.  The will append to the ticker list and pull the price;however, it will not be on the list during the next run.  This will be fixed in the next release. 

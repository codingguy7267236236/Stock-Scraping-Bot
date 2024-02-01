import yfinance as yf
import mplfinance as mpf
 

#gets the current stock price #symbol means comapny symbol e.g. Tesla: TSLA
def get_current_price(ticker):
    ticker = yf.Ticker(ticker.upper())
    todays_data = ticker.history(period='1d')
    #returning most current close price
    return todays_data['Close'][0]

#get the candlestick data for a stock over a given time period
#e.g. 5m (5 mins) 5M (5 months) 5h (5 hours) 5D (5 days)
#period refers to the timeframe you want covered, e.g. last day
#interval refers to how often each candlestick is drawn e.g. 5mins
def getCandlestick(stock,period,interval):
    
    filename = 'stock.png'

    #getting the data from yahoo finance
    data = yf.download(tickers = stock, period = period,interval = interval)

    mc = mpf.make_marketcolors(up='tab:green',down='tab:red',wick={'up':'green','down':'red'})
    style = mpf.make_mpf_style(base_mpl_style='ggplot',marketcolors=mc)
    mpf.plot(data,type='candle',style=style,ylabel='Price{$}',volume=False,ylabel_lower='Shares\nTraded',savefig=filename)
    print('saved')
    #return the filename where the candlestick was saved
    return filename


#tsla = getCandlestick("TSLA","5h","5m")
from flask import Flask, render_template, request, jsonify
import yfinance as yf
from datetime import datetime
import plotly.graph_objects as go
import pandas as pd
from plotly.utils import PlotlyJSONEncoder
import json
import requests

## Note on the usage of AI
## AI was used to create much of the code for this application. I wanted to make something that I thought would be
## a large challenge even with help from AI. I used Claude 3.5 to implement each feature separately. I don't think
## it would be appropriate to make up documentation prompts after the fact because in reality I probably reprompted 
## Claude over 300 times over the course of the weeks. But I want to reiterate that the large majoirty of the program 
## was coded by Claude, with myself prompting it to fit my exact requirements and combining each part to make each 
## feature function as part of the overall program.

app = Flask(__name__)

# Function to format market cap (reduce length of long numbers)
def format_market_cap(market_cap):
    if market_cap >= 1e12:
        return f"${market_cap/1e12:.2f}T"
    elif market_cap >= 1e9:
        return f"${market_cap/1e9:.2f}B"
    elif market_cap >= 1e6:
        return f"${market_cap/1e6:.2f}M"
    return f"${market_cap:,.2f}"

# Function to get stock info from yfinance
def get_stock_info(ticker_symbol):
    try:
        stock = yf.Ticker(ticker_symbol)
        info = stock.info
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # Get current price or most recent closing price if market is currently closed
        current_price = info.get('regularMarketPrice')
        if current_price in [None, 'N/A']:
            current_price = info.get('previousClose', 'N/A')
            price_display = f"{current_price} (Previous Close)"
        else:
            price_display = current_price
        
        stock_data = {
            'time': current_time,
            'company': info.get('shortName', info.get('longName', 'N/A')),
            'symbol': ticker_symbol.upper(),
            'currentPrice': price_display,
            'dayRange': f"{info.get('regularMarketDayLow', 'N/A')} - {info.get('regularMarketDayHigh', 'N/A')}",
            'weekRange': f"{info.get('fiftyTwoWeekLow', 'N/A')} - {info.get('fiftyTwoWeekHigh', 'N/A')}",
            'marketCap': format_market_cap(info.get('marketCap', 0)),
            'volume': f"{info.get('regularMarketVolume', 'N/A'):,}",
            'avgVolume': f"{info.get('averageVolume', 'N/A'):,}",
            'peRatio': info.get('forwardPE', info.get('trailingPE', 'N/A')),
            'eps': info.get('trailingEps', 'N/A'),
            'beta': round(info.get('beta', 'N/A'), 2) if info.get('beta') != 'N/A' else 'N/A',
            'dividendYield': f"{info.get('dividendYield', 'N/A'):.2%}" if info.get('dividendYield') else 'N/A',
            'profitMargin': f"{info.get('profitMargins', 'N/A'):.2%}" if info.get('profitMargins') else 'N/A',
            'debtToEquity': info.get('debtToEquity', 'N/A'),
            'rsi': info.get('rsi', 'N/A'),
            'priceToBook': round(info.get('priceToBook', 'N/A'), 2) if info.get('priceToBook') != 'N/A' else 'N/A',
            'targetPrice': info.get('targetMeanPrice', 'N/A')
        }
        return stock_data, None
    except Exception as e:
        return None, str(e)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/stock', methods=['GET'])
def stock():
    ticker = request.args.get('symbol', '').upper()
    features = request.args.get('features', '').split(',')
    
    if not ticker:
        return jsonify({'error': 'No stock symbol provided'}), 400
    
    stock_data, error = get_stock_info(ticker)
    if error:
        return jsonify({'error': error}), 404
    
    company_name = stock_data['company']
    
    # Save search history to CommonStocksAndHistory.json
    with open('CommonStocksAndHistory.json', 'r+') as f:
        data = json.load(f)
        history_entry = {"symbol": ticker, "name": company_name}
        if history_entry not in data["search_history"]:
            data["search_history"].insert(0, history_entry)
            data["search_history"] = data["search_history"][:10]
        f.seek(0)
        json.dump(data, f, indent=4)
        f.truncate()
    
    if features and features[0]:
        filtered_data = {key: stock_data[key] for key in stock_data if key in features}
        filtered_data['time'] = stock_data['time']
        return jsonify(filtered_data)
    
    return jsonify(stock_data)

# Function to save persistent favorites to the same history json
@app.route('/favorites', methods=['GET', 'POST', 'DELETE'])
def handle_favorites():
    with open('CommonStocksAndHistory.json', 'r+') as f:
        data = json.load(f)
        
        if request.method == 'GET':
            return jsonify(data.get('favorites', []))
            
        elif request.method == 'POST':
            symbol = request.json.get('symbol')
            name = request.json.get('name')
            if symbol and name:
                if 'favorites' not in data:
                    data['favorites'] = []
                if {'symbol': symbol, 'name': name} not in data['favorites']:
                    data['favorites'].append({'symbol': symbol, 'name': name})
                    f.seek(0)
                    json.dump(data, f, indent=4)
                    f.truncate()
                return jsonify({'status': 'added'})
                
        elif request.method == 'DELETE':
            symbol = request.args.get('symbol')
            data['favorites'] = [f for f in data['favorites'] if f['symbol'] != symbol]
            f.seek(0)
            json.dump(data, f, indent=4)
            f.truncate()
            return jsonify({'status': 'removed'})


@app.route('/stocktwits_sentiment/<symbol>')
# Function to fetch and process StockTwits sentiment data
# This analyzes Twitter posts to gauge sentiment
### Note the stockktwits api is not functioning correctly and/or is not free
### Left the code intack in case, and to demonstrate the process 
def get_stocktwits_sentiment(symbol):
    url = f"https://api.stocktwits.com/api/2/streams/symbol/{symbol}.json"
    headers = {
        'Accept': 'application/json'
    }
    
    try:
        response = requests.get(url, headers=headers)
        data = response.json()
        
        messages = data.get('messages', [])
        sentiment_counts = {
            'bullish': sum(1 for msg in messages if msg.get('entities', {}).get('sentiment', {}).get('basic') == 'bullish'),
            'bearish': sum(1 for msg in messages if msg.get('entities', {}).get('sentiment', {}).get('basic') == 'bearish'),
            'neutral': sum(1 for msg in messages if msg.get('entities', {}).get('sentiment', {}).get('basic') == 'neutral')
        }
        
        # Only return actual sentiment data
        return jsonify(sentiment_counts)
        
    except Exception as e:
        print(f"StockTwits API Error: {str(e)}")
        return jsonify({'error': str(e)})

@app.route('/news_sentiment/<symbol>')
# Function to fetch and process news sentiment data
### Note this is working, but I did not pay for the full API so I've used the demo version that
### only shows sentiment data for certain symbols (AAPL)
def get_news_sentiment(symbol):
    url = f"https://www.alphavantage.co/query?function=NEWS_SENTIMENT&tickers={symbol}&apikey=demo"
    
    try:
        response = requests.get(url)
        data = response.json()
        
        # Process feed entries to calculate sentiment
        feed = data.get('feed', [])
        sentiments = [item.get('overall_sentiment_score', 0) for item in feed]
        
        # Calculate sentiment distribution
        bullish = sum(1 for s in sentiments if s > 0.25)
        bearish = sum(1 for s in sentiments if s < -0.25)
        neutral = sum(1 for s in sentiments if -0.25 <= s <= 0.25)
        
        total = max(len(sentiments), 1)  # Avoid division by zero
        
        sentiment_scores = {
            'bullish': round((bullish/total) * 100),
            'bearish': round((bearish/total) * 100),
            'neutral': round((neutral/total) * 100)
        }
        
        return jsonify(sentiment_scores)
    except Exception as e:
        return jsonify({'error': str(e)})

@app.route('/historical/<symbol>/<timeframe>')
# Function to fetch and display historical data (using yfinance)
# chart shows as a candlestick chart, primarily for shorter timeframes
def historical_data(symbol, timeframe):
    periods = {'1d': '1d', '1w': '5d', '1m': '1mo', '1y': '1y', '5y': '5y'}
    period = periods.get(timeframe, '1y')
    
    ticker = yf.Ticker(symbol)
    hist = ticker.history(period=period)
    
    fig = go.Figure(data=[go.Candlestick(x=hist.index,
                open=hist['Open'],
                high=hist['High'],
                low=hist['Low'],
                close=hist['Close'])])
    
    fig.update_layout(title=f'{symbol} Stock Price', xaxis_title='Date', yaxis_title='Price')
    
    return json.dumps(fig, cls=PlotlyJSONEncoder)

@app.route('/compare')
# Function to compare multiple stocks on a single chart (percent change not price change)
def compare_stocks():
    symbols = request.args.get('symbols', '').split(',')
    timeframe = request.args.get('timeframe', '1y')
    
    # Map timeframes to yfinance intervals
    intervals = {
        '1mo': '1d',    # 1-day intervals for 1 month
        '3mo': '1d',    # 1-day intervals for 3 months
        '1y': '1d',     # 1-day intervals for 1 year
        '5y': '1wk',    # 1-week intervals for 5 years
        '10y': '1mo'    # 1-month intervals for 10 years
    }
    
    fig = go.Figure()
    
    for symbol in symbols:
        ticker = yf.Ticker(symbol)
        hist = ticker.history(period=timeframe, interval=intervals.get(timeframe, '1d'))
        
        initial_price = hist['Close'].iloc[0]
        pct_change = ((hist['Close'] - initial_price) / initial_price) * 100
        
        fig.add_trace(go.Scatter(x=hist.index, y=pct_change, name=symbol))
    
    fig.update_layout(
        title='Stock Price Comparison (% Change)',
        xaxis_title='Date',
        yaxis_title='Percent Change (%)',
        yaxis=dict(tickformat='.2f')
    )
    
    return json.dumps(fig, cls=PlotlyJSONEncoder)


@app.route('/suggest')
# Function to suggest stocks based on user input
# Uses both the built in list of 100 top stocks and user search history

# In situations where the stock exists already in the top stocks list and then gets added to
# search history, it will not be suggested twice.
def suggest():
    query = request.args.get('q', '').upper()
    if len(query) < 1:
        return jsonify([])
    
    with open('CommonStocksAndHistory.json', 'r') as f:
        data = json.load(f)
        common_stocks = data["common_stocks"]
        search_history = data["search_history"]
    
    suggestions = []
    
    history_matches = [
        {'symbol': entry['symbol'], 'name': entry['name']}
        for entry in search_history
        if query in entry['symbol']
    ]
    
    common_matches = [
        {'symbol': symbol, 'name': name}
        for symbol, name in common_stocks.items()
        if query in symbol
    ]
    
    for hist_match in history_matches:
        if any(cm['symbol'] == hist_match['symbol'] for cm in common_matches):
            suggestions.append(hist_match)
        else:
            suggestions.append(hist_match)
            
    for common_match in common_matches:
        if not any(s['symbol'] == common_match['symbol'] for s in suggestions):
            suggestions.append(common_match)
    
    return jsonify(suggestions)

if __name__ == "__main__":
    app.run(debug=True)

import yfinance as yf
import pandas as pd

def load_data(tf):
    interval_map = {'5m': '5m', '15m': '15m', '1h': '60m'}
    try:
        df = yf.download("XAUUSD=X", period="7d", interval=interval_map[tf])
        df.dropna(inplace=True)
        return df
    except Exception as e:
        print(f"Error loading data: {e}")
        return None

def find_snr_levels(df):
    highs = df['High'].rolling(window=20).max()
    lows = df['Low'].rolling(window=20).min()
    return {
        'support': lows[-1],
        'resistance': highs[-1]
    }

def suggest_trade(df, snr):
    last_price = df['Close'].iloc[-1]
    long_price = snr['support'] if last_price > snr['support'] else None
    short_price = snr['resistance'] if last_price < snr['resistance'] else None
    return long_price, short_price

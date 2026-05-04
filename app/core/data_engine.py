import yfinance as yf
import pandas as pd
import pandas_ta as ta

class DataEngine:
    @staticmethod
    def fetch_data(symbol, interval='1h', period='1mo'):
        df = yf.download(symbol, period=period, interval=interval)
        if df.empty: return None
        df['RSI'] = ta.rsi(df['Close'], length=14)
        df['EMA_200'] = ta.ema(df['Close'], length=200)
        macd = ta.macd(df['Close'])
        df = pd.concat([df, macd], axis=1)
        return df
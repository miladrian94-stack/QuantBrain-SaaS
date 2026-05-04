import pandas_ta as ta

class MarketRegime:
    @staticmethod
    def detect(df):
        adx = ta.adx(df['High'], df['Low'], df['Close'])
        val = adx['ADX_14'].iloc[-1]
        if val > 25: return "Trending"
        return "Sideways"
class AIScorer:
    def calculate_score(self, df):
        score = 50
        last = df.iloc[-1]
        if last['RSI'] < 30: score += 20
        elif last['RSI'] > 70: score -= 20
        if last['Close'] > last['EMA_200']: score += 15
        else: score -= 15
        return max(0, min(100, score))
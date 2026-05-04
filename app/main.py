import time
import schedule
from core.data_engine import DataEngine
from core.market_regime import MarketRegime
from ai.scorer import AIScorer
from engine.risk_manager import RiskManager

SYMBOLS = ["BTC-USD", "ETH-USD", "GC=F", "AAPL", "2222.SR"]

def run_bot():
    engine = DataEngine()
    scorer = AIScorer()
    risk = RiskManager()
    
    print(f"🔄 Running cycle...")
    for sym in SYMBOLS:
        try:
            df = engine.fetch_data(sym)
            if df is None: continue
            
            score = scorer.calculate_score(df)
            regime = MarketRegime.detect(df)
            
            if score > 80 or score < 20:
                side = "BUY" if score > 80 else "SELL"
                r_data = risk.calculate_position(sym, df['Close'].iloc[-1], side)
                print(f"🚀 Signal: {sym} | {side} | Score: {score} | TP: {r_data['take_profit']}")
        except Exception as e:
            print(f"❌ Error on {sym}: {e}")

schedule.every(15).minutes.do(run_bot)
run_bot() # للتشغيل الفوري عند البدء
while True:
    schedule.run_pending()
    time.sleep(1)
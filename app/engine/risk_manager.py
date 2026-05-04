class RiskManager:
    def calculate_position(self, symbol, price, side):
        stop_loss = price * 0.98 if side == "BUY" else price * 1.02
        take_profit = price * 1.04 if side == "BUY" else price * 0.96
        return {
            "entry": round(price, 4), 
            "stop_loss": round(stop_loss, 4), 
            "take_profit": round(take_profit, 4)
        }
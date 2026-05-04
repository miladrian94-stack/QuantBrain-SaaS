import streamlit as st
import pandas as pd

st.set_page_config(page_title="AI-TRADER Dashboard", layout="wide")
st.title("🚀 AI-TRADER-ULTRA Dashboard")
st.sidebar.header("System Control")
st.sidebar.write("Status: 🟢 Running")

col1, col2 = st.columns(2)
col1.metric("Market Status", "Operational")
col2.metric("Active Signals", "5")

st.subheader("Recent Market Analysis")
# بيانات تجريبية للعرض
data = {
    "Symbol": ["BTC-USD", "ETH-USD", "GOLD", "AAPL", "TADAWUL:2222"],
    "AI Confidence": ["92%", "88%", "45%", "76%", "82%"],
    "Recommendation": ["Strong Buy", "Buy", "Hold", "Buy", "Strong Buy"]
}
st.table(pd.DataFrame(data))
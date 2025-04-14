# main.py
import streamlit as st
from analysis import load_data, find_snr_levels, suggest_trade
from chart import plot_chart

st.title("XAUUSD 趨勢與支撐壓力分析器")

timeframe = st.selectbox("選擇時間框架", ['5m', '15m', '1h'])
df = load_data(timeframe)

if df is not None:
    snr_levels = find_snr_levels(df)
    long_price, short_price = suggest_trade(df, snr_levels)
    fig = plot_chart(df, snr_levels, long_price, short_price)
    st.plotly_chart(fig)

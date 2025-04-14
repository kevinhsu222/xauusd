import plotly.graph_objects as go

def plot_chart(df, snr, long_price, short_price):
    fig = go.Figure()
    fig.add_trace(go.Candlestick(
        x=df.index,
        open=df['Open'],
        high=df['High'],
        low=df['Low'],
        close=df['Close'],
        name='XAUUSD'
    ))

    fig.add_hline(y=snr['support'], line=dict(color='blue', dash='dot'), name='Support')
    fig.add_hline(y=snr['resistance'], line=dict(color='orange', dash='dot'), name='Resistance')

    if long_price:
        fig.add_hline(y=long_price, line=dict(color='green', width=3), name='Long Entry')
    if short_price:
        fig.add_hline(y=short_price, line=dict(color='red', width=3), name='Short Entry')

    fig.update_layout(title='XAUUSD 技術分析圖', xaxis_title='時間', yaxis_title='價格')
    return fig

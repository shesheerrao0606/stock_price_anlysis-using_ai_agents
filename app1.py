import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import yfinance as yf

# List of common stocks
COMMON_STOCKS = {
    'NVIDIA': 'NVDA', 'APPLE': 'AAPL', 'GOOGLE': 'GOOGL', 'MICROSOFT': 'MSFT',
    'TESLA': 'TSLA', 'AMAZON': 'AMZN', 'META': 'META', 'NETFLIX': 'NFLX',
    'TCS': 'TCS.NS', 'RELIANCE': 'RELIANCE.NS', 'INFOSYS': 'INFY.NS',
    'WIPRO': 'WIPRO.NS', 'HDFC': 'HDFCBANK.NS', 'TATAMOTORS': 'TATAMOTORS.NS',
    'ICICIBANK': 'ICICIBANK.NS', 'SBIN': 'SBIN.NS'
}

st.set_page_config(page_title="Stocks Market Analysis Dashboard", page_icon="", layout="wide")

st.markdown("""
    <style>
    .main { padding: 2rem; }
    .stApp { max-width: 1400px; margin: 0 auto; }
    .card {
        background: linear-gradient(135deg, #f6f8fa 0%, #ffffff 100%);
        border-radius: 15px;
        padding: 1.5rem;
        margin: 1rem 0;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        border: 1px solid #e1e4e8;
    }
    .metric-value {
        font-size: 24px;
        font-weight: bold;
        color: #0366d6;
    }
    .metric-label {
        font-size: 14px;
        color: #586069;
        text-transform: uppercase;
    }
    .chart-container {
        background: white;
        border-radius: 15px;
        padding: 1rem;
        margin: 1rem 0;
        border: 1px solid #e1e4e8;
    }
    .recommendation {
        background-color: #f0f8ff;
        border-left: 5px solid #0366d6;
        padding: 1.5rem;
        margin: 1rem 0;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        border: 1px solid #e1e4e8;
    }
    </style>
    """, unsafe_allow_html=True)

def get_stock_data(symbol):
    try:
        stock = yf.Ticker(symbol)
        info = stock.info
        hist = stock.history(period="1y")
        news = stock.news
        return info, hist, news
    except Exception as e:
        st.error(f"Error fetching data: {str(e)}")
        return None, None, None

def create_price_chart(hist_data, symbol):
    fig = go.Figure()
    fig.add_trace(go.Candlestick(
        x=hist_data.index, open=hist_data['Open'],
        high=hist_data['High'], low=hist_data['Low'],
        close=hist_data['Close'], name='OHLC'
    ))
    fig.update_layout(
        title=f'{symbol} Price Movement',
        template='plotly_white',
        xaxis_rangeslider_visible=True,
        height=500
    )
    return fig

def main():
    st.title("Stocks Price Analysis using Machine Learning and AI Agents")
    
    stock_input = st.text_input("Enter Company Name", help="e.g., APPLE, TCS")
    
    if st.button("Analyze", use_container_width=True):
        if not stock_input:
            st.error("Please enter a stock name")
            return
        
        symbol = COMMON_STOCKS.get(stock_input.upper()) or stock_input
        
        with st.spinner("Analyzing..."):
            info, hist, news = get_stock_data(symbol)
            
            if info and hist is not None:
                # Display metrics in rows
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.markdown(f"<div class='card'><div class='metric-value'>${info.get('currentPrice', 'N/A')}</div><div class='metric-label'>Current Price</div></div>", unsafe_allow_html=True)
                with col2:
                    st.markdown(f"<div class='card'><div class='metric-value'>{info.get('forwardPE', 'N/A')}</div><div class='metric-label'>Forward P/E</div></div>", unsafe_allow_html=True)
                with col3:
                    st.markdown(f"<div class='card'><div class='metric-value'>${info.get('fiftyTwoWeekLow', 'N/A')}</div><div class='metric-label'>52-Week Low</div></div>", unsafe_allow_html=True)
                
                col4, col5, col6 = st.columns(3)
                with col4:
                    st.markdown(f"<div class='card'><div class='metric-value'>${info.get('fiftyTwoWeekHigh', 'N/A')}</div><div class='metric-label'>52-Week High</div></div>", unsafe_allow_html=True)
                with col5:
                    st.markdown(f"<div class='card'><div class='metric-value'>{info.get('marketCap', 'N/A')}</div><div class='metric-label'>Market Cap</div></div>", unsafe_allow_html=True)
                with col6:
                    st.markdown(f"<div class='card'><div class='metric-value'>{info.get('dividendYield', 'N/A')}</div><div class='metric-label'>Dividend Yield</div></div>", unsafe_allow_html=True)

                st.markdown("<div class='recommendation'>", unsafe_allow_html=True)
                recommendation = info.get('recommendationKey', 'N/A').title()
                color = "green" if recommendation in ["Strong Buy", "Buy"] else "yellow" if recommendation == "Hold" else "red"
                st.markdown(f"<div class='metric-value' style='color:{color};'>{recommendation}</div><div class='metric-label'>Recommendation</div>", unsafe_allow_html=True)
                st.markdown("</div>", unsafe_allow_html=True)

                st.markdown("<div class='chart-container'>", unsafe_allow_html=True)
                st.plotly_chart(create_price_chart(hist, symbol), use_container_width=True)
                st.markdown("</div>", unsafe_allow_html=True)
                
                # Display recent news articles
                if news:
                    st.markdown("### Recent News", unsafe_allow_html=True)
                    for article in news[:3]:
                        title = article.get('title', 'No title available')
                        link = article.get('link', '#')
                        summary = article.get('summary', 'No summary available')
                        
                        st.markdown(f"- **[{title}]({link})**: {summary}")
                
                # Display company overview
                if 'longBusinessSummary' in info:
                    st.markdown("<div class='card'>", unsafe_allow_html=True)
                    st.markdown("### Company Overview")
                    st.write(info['longBusinessSummary'])
                    st.markdown("</div>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()

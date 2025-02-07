Here's a `README.md` file for the provided code:


# Stocks Price Analysis using Machine Learning and AI Agents

A web-based application built with Streamlit to analyze stock data, provide insights, and display financial metrics using AI agents. This app integrates financial data, web search tools, and AI models to deliver a comprehensive stock market analysis.

## Features

- **Stock Price Analysis**: Fetch and visualize historical stock price data using candlestick charts.
- **AI-Powered Insights**: Utilize AI agents for financial insights and web-based queries.
- **Key Financial Metrics**: Display essential metrics like current price, forward P/E, and recommendations.
- **Company Overview**: Provide a summary of the company's business.

## Tech Stack

- **Streamlit**: Frontend framework for building interactive web apps.
- **yFinance**: Fetch financial data for stocks.
- **Plotly**: Create interactive candlestick charts.
- **Phi**: AI agent framework for web and financial analysis.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/stocks-analysis-ai-agents.git
   cd stocks-analysis-ai-agents
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up your Groq API key:
   - Open the code file.
   - Replace `GROQ_API_KEY = ""` with your Groq API key.

## Usage

1. Run the application:
   ```bash
   streamlit run app.py
   ```

2. Open the app in your browser at `http://localhost:8501`.

3. Enter a stock name (e.g., `APPLE`, `TCS`) in the input field and click "Analyze."

## Customization

- **Stock List**: Add or modify stock symbols in the `COMMON_STOCKS` dictionary.
- **Agents**: Configure AI agents in the `initialize_agents` function to fit your specific requirements.

## Screenshots

### Home Page
<img width="1710" alt="image" src="https://github.com/user-attachments/assets/2913d9ea-9a2d-4354-9c11-2fcba4b68fc6" />


### Stock Analysis
<img width="1710" alt="image" src="https://github.com/user-attachments/assets/33da7114-2e3b-4a06-9325-8b1425900613" />


## Dependencies

- `streamlit`
- `pandas`
- `plotly`
- `yfinance`
- `phi`
  - `phi.agent`
  - `phi.model.groq`
  - `phi.tools.yfinance`
  - `phi.tools.duckduckgo`
  - `phi.tools.googlesearch`



## Acknowledgments

- Powered by [Groq AI](https://www.groq.com/).
- Stock data provided by [Yahoo Finance](https://finance.yahoo.com/).
- Built with [Streamlit](https://streamlit.io/).
```

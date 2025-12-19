import yfinance as yf
from functools import lru_cache

def get_stock(symbol, period="1mo", interval="15m"):
    ticker = yf.Ticker(symbol)
    hist = ticker.history(period=period, interval=interval)

    if hist.empty:
        return None

    return {
        "symbol": symbol,
        "last_price": float(hist["Close"].iloc[-1]),
        "open": float(hist["Open"].iloc[-1]),
        "high": float(hist["High"].iloc[-1]),
        "low": float(hist["Low"].iloc[-1]),
        "volume": int(hist["Volume"].iloc[-1]),
        "history": [
            {
                "date": idx.strftime("%Y-%m-%d-%H:%M"),
                "open": float(row["Open"]),
                "high": float(row["High"]),
                "low": float(row["Low"]),
                "close": float(row["Close"]),
                "volume": int(row["Volume"]),
            }
            for idx, row in hist.iterrows()
        ]
    }

@lru_cache(maxsize=100)
def get_stock_cached(symbol, period):
    return get_stock(symbol, period)

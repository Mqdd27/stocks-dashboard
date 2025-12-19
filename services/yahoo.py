import yfinance as yf
from functools import lru_cache
from datetime import time

IDX_OPEN = time(9, 0)
IDX_CLOSE = time(15, 50)

def get_stock(symbol, period="1mo", interval="15m"):
    ticker = yf.Ticker(symbol)

    hist = ticker.history(
        period=period,
        interval=interval,
        auto_adjust=False
    )

    if hist.empty:
        return None

    # filter jam bursa IDX (hanya intraday)
    if interval.endswith("m") or interval.endswith("h"):
        hist = hist.between_time(IDX_OPEN, IDX_CLOSE)

    last = hist.iloc[-1]

    return {
        "symbol": symbol,
        "last_price": round(float(last["Close"]), 2),
        "open": round(float(last["Open"]), 2),
        "high": round(float(last["High"]), 2),
        "low": round(float(last["Low"]), 2),
        "volume": int(last["Volume"]),

        "history": [
            {
                "time": idx.strftime("%Y-%m-%d %H:%M"),
                "open": round(float(row["Open"]), 2),
                "high": round(float(row["High"]), 2),
                "low": round(float(row["Low"]), 2),
                "close": round(float(row["Close"]), 2),
                "volume": int(row["Volume"]),
            }
            for idx, row in hist.iterrows()
        ]
    }

@lru_cache(maxsize=100)
def get_stock_cached(symbol, period):
    return get_stock(symbol, period)

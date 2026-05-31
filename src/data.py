import yfinance as yf
import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"


def get_data(ticker="SPY", start="2010-01-01", end="2024-12-31"):
    csv_path = DATA_DIR / "spy_data.csv"
    
    if csv_path.exists():
        data = pd.read_csv(csv_path, index_col=0, parse_dates=True)
        return data
    
    data = yf.download(ticker, start, end)
    data.columns = data.columns.droplevel(1) # type: ignore
    data.index.name= 'date'  # type: ignore
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    data.to_csv(csv_path) # type: ignore
    return data

def get_yearly_dates(data):
    
    yearly_dates = {}
    datetime_index = pd.DatetimeIndex(data.index)

    for date in datetime_index:
        year = date.year

        if year not in yearly_dates:
            yearly_dates[year] = []


        yearly_dates[year].append(date)

    return yearly_dates



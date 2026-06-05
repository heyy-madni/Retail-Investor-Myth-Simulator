import yfinance as yf
import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
SRC_DIR = Path(__file__).resolve().parent



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


def investor_summary(df, beliefs):
    investors = list(beliefs.keys())

    inflation_factor = (1 + df["inflation_rate"] / 100).cumprod().iloc[-1]

    summary = []

    for investor in investors:
        initial = df[investor].iloc[0]
        final = df[investor].iloc[-1]

        total_return = ((final - initial) / initial) * 100

        years = len(df) - 1
        cagr = ((final / initial) ** (1 / years) - 1) * 100

        inflation_adjusted_final = final / inflation_factor

        summary.append({
            "Investor": investor,
            "Initial Value": round(initial, 2),
            "Final Value": round(final, 2),
            "Inflation Adjusted Final (2000 $)": round(inflation_adjusted_final, 2),
            "Inflation Lost $": round(final - inflation_adjusted_final, 2),
            "Total Return %": round(total_return, 2),
            "CAGR %": round(cagr, 2),
            "Belief": beliefs[investor]
        })

    summary_df = pd.DataFrame(summary)

    summary_df = (
        summary_df
        .sort_values("Final Value", ascending=False)
        .reset_index(drop=True)
    )

    summary_df.index += 1
    summary_df.index.name = "Rank"

    return summary_df



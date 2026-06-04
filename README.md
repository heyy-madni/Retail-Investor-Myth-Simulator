# Retail Investor Myth Simulator

A Python simulation that tests five common retail investor strategies against 25 years of real S&P 500 data (2000–2024) — including two major crashes, a pandemic, and a bull run. Each strategy is represented by a rule-based agent with a fixed belief. The results are displayed in an interactive Streamlit dashboard.

---

## Why I Built This

Most investing advice is either too abstract ("just hold long term") or too anecdotal ("my friend panic sold in 2008 and lost everything"). I wanted to see the actual numbers — what happens to ₹10,000 over 25 years depending on *how* you behave, not just *what* you buy.

The five archetypes cover beliefs I've genuinely heard from people: the one who never sells, the one who buys every dip, the one who chases momentum, the one who runs at the first sign of loss, and the one who just invests a fixed amount every month and ignores everything else.

---

## Agents

Each agent starts with **$10,000** and operates on a fixed rule — no learning, no adapting.

| Agent | Strategy |
|---|---|
| **DiamondSana** | Buy once on day one. Never sell. |
| **PanicPayal** | Sell everything when portfolio drops 8% from peak. Re-enter after 30-day cooldown. |
| **DipHunterDev** | Deploy 25% of remaining cash whenever price dips 5% from recent high. Never sell. |
| **HotTipHari** | Buy when last 30 days were up. Sell when they were down. Pure momentum. |
| **IndexRehan** | Invest a fixed $500 every month. No timing, no conditions. |

---

## Tech Stack

- **Python** — core simulation logic
- **yfinance** — SPY historical price data (cached locally as CSV after first fetch)
- **pandas** — data wrangling, merging inflation data, building result DataFrame
- **World Bank CPI data** — annual US inflation rates (2000–2024) for real-return adjustment
- **Streamlit** — interactive dashboard for results and summary table
- **pathlib** — portable file path handling across OS

---

## Project Structure

```
RIMS/
├── data/
│   ├── spy_data.csv          # Cached SPY price history (2000–2024)
│   └── inflation.csv         # Annual US inflation rates (World Bank)
├── src/
│   ├── main.py               # Entry point — launches Streamlit via subprocess
│   ├── data.py               # Data fetching and yearly date grouping
│   ├── agents.py             # Five investor agent classes
│   ├── simulator.py          # Runs simulation, builds result + inflation DataFrame
│   └── web_presentation.py   # Streamlit dashboard — charts, summary table, verdict
└── README.md
```

---

## How to Run

```bash
# 1. Install dependencies
pip install yfinance pandas streamlit

# 2. Run
cd src
python main.py
```

The dashboard opens in your browser. SPY data is fetched once and cached — subsequent runs load from disk.

---

## Key Design Decisions

**Disk-based caching** — `spy_data.csv` is written after the first `yfinance` call. This keeps the app fast and avoids repeated API calls during development or demo.

**Inflation adjustment** — Portfolio values are adjusted using cumulative CPI (World Bank data) to show real purchasing power, not just nominal growth. The summary table shows both final nominal value and inflation-adjusted final value.

**Yearly snapshots, daily decisions** — Agents make decisions on every trading day, but portfolio values are recorded at year-end. This gives a clean annual chart without losing intra-year behaviour.

**Separation of concerns** — Agent logic (`agents.py`), simulation loop (`simulator.py`), data layer (`data.py`), and presentation (`web_presentation.py`) are kept in separate files. Easy to swap an agent or change the presentation without touching simulation logic.

---

## What the Results Show

The simulation runs from 2000 through 2024 — starting right at the dot-com crash, then through 2008, COVID, and the 2022 rate hike drawdown.

The final summary table ranks all five investors by terminal portfolio value, with CAGR and inflation-adjusted figures alongside.

The result across every run: the agents who held through downturns significantly outperformed the one who sold on fear. PanicPayal's 30-day cooldown meant she frequently re-entered after the bottom was already behind her.

---

## Reflection

The part I found most interesting wasn't the winner — it was *how much* the timing of re-entry hurt PanicPayal. Selling on a drawdown isn't the fatal move. Waiting 30 days and buying back in after the recovery has already started is. That's a behavioural tax that doesn't show up in strategy descriptions but shows up clearly in the numbers.

IndexRehan (the DCA agent) consistently finished near the top despite zero market awareness. That result alone makes the point better than most investing articles do.

---

## Status

Simulation complete. Dashboard functional. Potential next steps: add starting year selector, allow custom agent parameters, and extend to international indices.

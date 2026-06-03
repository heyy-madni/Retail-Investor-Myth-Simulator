from simulator import df
import pandas as pd
import streamlit as st



def investor_summary(df, beliefs):
    investors = list(beliefs.keys())

    # cumulative inflation from start year to end year
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

beliefs = {
    "Sana": "Never sell. Buy once. Hold forever.",
    "Payal": "Sell everything when down 8% from peak.",
    "Dev": "Every dip is an opportunity. Never sell.",
    "Hari": "What went up last month will keep going up.",
    "Rehan": "Buy a fixed amount every month. Never stop."
}


summary_df=investor_summary(df, beliefs)


st.title('Retail-Investor-Myth-Simulator')



df_plot = df.drop(columns='inflation_rate')
st.line_chart(df_plot,x='year')

st.subheader('Investor Summary')
st.dataframe(summary_df)



winner = summary_df.iloc[0]
loser = summary_df.iloc[-1]

st.write(f"""
I simulated 5 investors, each with a different belief about the market.

**{winner['Investor']}** won with a strategy of "{winner['Belief']}" — 
ended up at ${winner['Final Value']:,.2f} with a CAGR of {winner['CAGR %']}%.

**{loser['Investor']}** came last with "{loser['Belief']}" — 
only ${loser['Final Value']:,.2f} after 25 years.

Honestly the result is pretty clear — most people who just held on did well. 
The one who kept selling when things got scary ({loser['Investor']}) barely made anything. 
Not a surprise, but seeing the actual numbers makes it hit different.
""")


st.subheader('Personal Verdict')
st.write(
    'I simulated 5 agents to mimic retail investor beliefs. '
    'most of them made money because they kept their shares for a long time. '
    'the one who had a rule to panic sell barely made anything. '
    'holding index shares for the long term is always a win — '
    'there will be dips, but just buy and hold.'
)


from simulator import df
import pandas as pd
import streamlit as st
from data import investor_summary
import plotly.express as px





st.title('Retail-Investor-Myth-Simulator')


#chart block
df_raw = df.drop(columns='inflation_rate')

melt_df=pd.melt(df_raw,['year'])
melt_df.rename(columns={'variable':'investor','value':'portfolio'},inplace=True)



#chart

st.info("""
**Time frame: 2000–2024 | Index: S&P 500**

Each investor starts with $10,000 and follows one fixed rule — no learning, no adapting.
The goal: see what happens depending on *how* you behave, not just *what* you buy.
""")

st.plotly_chart(px.line(melt_df,x='year',y='portfolio',color='investor',labels={'year':'YEAR','investor':'Investor'}))




#investor summary block
st.subheader('Investor Summary')

beliefs = {
    "Sana": "Never sell. Buy once. Hold forever.",
    "Payal": "Sell everything when down 8% from peak.",
    "Dev": "Every dip is an opportunity. Never sell.",
    "Hari": "What went up last month will keep going up.",
    "Rehan": "Buy a fixed amount every month. Never stop."
}

summary_df=investor_summary(df, beliefs)
st.dataframe(summary_df,use_container_width=True)




#winner and loser block
winner = summary_df.iloc[0]
loser = summary_df.iloc[-1]

st.info(f"""
I simulated 5 investors, each with a different belief about the market.

**{winner['Investor']}** won with a strategy of "{winner['Belief']}" — 
ended up at ${winner['Final Value']:,.2f} with a CAGR of {winner['CAGR %']}%.

**{loser['Investor']}** came last with "{loser['Belief']}" — 
only ${loser['Final Value']:,.2f} after 25 years.

Honestly the result is pretty clear — most people who just held on did well. 
The one who kept selling when things got scary ({loser['Investor']}) barely made anything. 
Not a surprise, but seeing the actual numbers makes it hit different.
""")





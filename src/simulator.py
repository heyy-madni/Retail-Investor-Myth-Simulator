# simulator.py
from data import get_data ,get_yearly_dates,DATA_DIR
import agents  
import pandas as pd

inflation_file= DATA_DIR/'inflation.csv'

def run_simulation():
    df = get_data()
    dates = get_yearly_dates(df)

    sana =agents.DiamondSana()
    dev=agents.DipHunterDev()
    hari=agents.HotTipHari()
    rehan=agents.IndexRehan()
    payal=agents.PanicPayal()


    result = {
        "Sana": {},
        "Payal": {},
        "Dev": {},
        "Hari": {},
        "Rehan": {}
    }
    for year in sorted(dates.keys()):
        for date in dates[year]:
            price = df.loc[date, "Close"] #type:ignore

            sana.decide(price)
            dev.decide(price)
            payal.decide(price)
            rehan.decide(price,date.month)

            a= df.index.get_loc(date) # type: ignore
            if a >= 30: # type: ignore
                past_date = df.index[a - 30] # type: ignore
                price_30_days_ago = df.loc[past_date, "Close"] # type: ignore
                hari.decide(price, price_30_days_ago)

        sana_portfolio  = sana.cash + (sana.shares*int(price)) # type: ignore
        dev_portfolio   = dev.cash + (dev.shares*int(price)) # type: ignore
        payal_portfolio = payal.cash + (payal.shares*int(price)) # type: ignore
        rehan_portfolio = rehan.cash + (rehan.shares*int(price)) # type: ignore
        hari_portfolio  = hari.cash + (hari.shares*int(price)) # type: ignore


        result["Sana"]  [year] = sana_portfolio
        result["Payal"] [year] = payal_portfolio
        result["Dev"]   [year] = dev_portfolio
        result["Rehan"] [year] = rehan_portfolio
        result["Hari"]  [year] = hari_portfolio


    return result

data = run_simulation()

sana  = data["Sana"]
payal = data["Payal"]
dev   = data["Dev"]
rehan = data["Rehan"]
hari  = data['Hari']

df    = pd.DataFrame(data)

df.index.name = 'year'
df = df.reset_index()

inflation_df = pd.read_csv(inflation_file)

df = df.merge(inflation_df, on='year')



# for agent_name, yearly_data in data.items():
#     print(f"\n{agent_name}:")
#     for year, value in yearly_data.items():
#         print(f"  {year}: ${value:,.2f}")



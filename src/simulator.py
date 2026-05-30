# simulator.py
from data import get_data ,get_yearly_dates,get_monthly_dates
import agents  as ags

def run_simulation():
    df = get_data()
    dates = get_yearly_dates(df)

    sana =ags.DiamondSana()
    dev=ags.DipHunterDev()
    hari=ags.HotTipHari()
    rehan=ags.IndexRehan()
    payal=ags.PanicPayal()

    agents = [sana, payal, dev, hari, rehan]

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






run_simulation()
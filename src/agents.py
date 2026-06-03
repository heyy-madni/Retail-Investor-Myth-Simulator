# agents.py

class DiamondSana:
    def __init__(self, cash=10000):
        self.cash = cash
        self.shares = 0
        self.has_bought = False
        self.belief = "Never sell. Buy once. Hold forever."
        self.on_price_bought = 0
    def decide(self, price):
        #buying
        if self.has_bought is False :
           self.on_price_bought = price.__round__(2)
           self.shares = (self.cash / price).__round__(2)
           self.cash = 0
           self.has_bought = True


class PanicPayal:
    def __init__(self, cash=10000):
        self.cash = cash
        self.shares = 0
        self.peak_value = cash
        self.waiting_days = 0
        self.belief = "Sell everything when down 8% from peak."

    def decide(self, price):
        portfolio = self.cash + (self.shares * price).__round__(2)
        if portfolio > self.peak_value:
            self.peak_value = portfolio

        if self.waiting_days > 0 :
            self.waiting_days-=1
            return 'still in cooldown'

        #selling
        if portfolio < self.peak_value * 0.92 and self.shares >0:
            self.cash = self.shares * price
            self.shares = 0
            self.waiting_days = 30
        
        #buying
        elif self.cash != 0 and self.waiting_days == 0:
            self.shares = (self.cash / price).__round__(2)
            self.cash = 0





class DipHunterDev:
    def __init__(self, cash=10000):
        self.cash = cash
        self.shares = 0
        self.recent_high = 0
        self.belief = "Every dip is an opportunity. Never sell."

    def decide(self, price):
        if price > self.recent_high:
            self.recent_high = price

        if price < self.recent_high * 0.95 and self.cash != 0:
            new_shares = self.cash * 0.25 / price
            self.cash -= new_shares * price  
            self.shares += new_shares






class HotTipHari:
    def __init__(self, cash=10000):
        self.cash = cash
        self.shares = 0
        self.belief = "What went up last month will keep going up."

    def decide(self, price, price_30_days_ago):
        momentum = price - price_30_days_ago
        
        if momentum > 0 and self.cash >0:
            new_shares = self.cash / price
            self.shares += new_shares
            self.cash = 0

        elif momentum <0 and self.shares > 0:
            self.cash  += self.shares*price
            self.shares = 0





class IndexRehan:
    def __init__(self, cash=10000, monthly_investment=500):
        self.cash = cash
        self.shares = 0
        self.monthly_investment = monthly_investment
        self.last_buy_month = None
        self.belief = "Buy a fixed amount every month. Never stop."

    def decide(self, price, current_month):
        if current_month != self.last_buy_month and   self.cash >= self.monthly_investment:
            self.shares += self.monthly_investment / price
            self.cash -= self.monthly_investment
            self.last_buy_month = current_month


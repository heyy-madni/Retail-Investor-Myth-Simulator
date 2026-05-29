# agents.py

class DiamondSana:
    def __init__(self, cash=10000):
        self.cash = cash
        self.shares = 0
        self.has_bought = False
        self.belief = "Never sell. Buy once. Hold forever."

    def decide(self, price):
        if self.has_bought is False :
            price - self.cash
        # if hasn't bought yet, buy as many shares as possible with all cash
        # otherwise do nothing
        pass

class PanicPayal:
    def __init__(self, cash=10000):
        self.cash = cash
        self.shares = 0
        self.peak_value = cash
        self.waiting_days = 0
        self.belief = "Sell everything when down 8% from peak."

    def decide(self, price):
        # calculate current portfolio value (cash + shares * price)
        # update peak if current value is higher
        # if waiting_days > 0: decrement and return (still in cooldown)
        # if portfolio dropped 8% from peak: sell all shares, set waiting_days = 30
        # if has cash and not waiting: buy as many shares as possible
        pass

class DipHunterDev:
    def __init__(self, cash=10000):
        self.cash = cash
        self.shares = 0
        self.recent_high = 0
        self.belief = "Every dip is an opportunity. Never sell."

    def decide(self, price):
        # update recent_high if price is higher
        # if price dropped 5% from recent_high and has cash:
        #     deploy 25% of current cash to buy shares
        pass

class HotTipHari:
    def __init__(self, cash=10000):
        self.cash = cash
        self.shares = 0
        self.belief = "What went up last month will keep going up."

    def decide(self, price, price_30_days_ago):
        # calculate momentum (price vs price 30 days ago)
        # if positive momentum and has cash: buy all in
        # if negative momentum and has shares: sell everything
        pass

class IndexRehan:
    def __init__(self, cash=10000, monthly_investment=500):
        self.cash = cash
        self.shares = 0
        self.monthly_investment = monthly_investment
        self.last_buy_month = None
        self.belief = "Buy a fixed amount every month. Never stop."

    def decide(self, price, current_month):
        # if current_month != last_buy_month and has enough cash:
        #     buy shares worth monthly_investment amount
        #     update last_buy_month
        pass
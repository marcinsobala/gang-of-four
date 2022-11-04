"""
Normally you'd avoid packing so many responsibilities into a class. This could be avoided
by using a strategy pattern for every step of the process, but it'd lead to a lot of strategies and
therefore a lot of boilerplate. A template pattern is a better fit here since we have a
standardized process with fixed steps.
"""

class Application:

    trading_strategy: str

    def __init__(self, trading_strategy="average"):
        self.trading_strategy = trading_strategy

    def connect(self):
        print("Connecting to Crypto Exchange")

    def get_market_data(self, coin: str) -> list[float]:
        return [10, 12, 18, 14]

    def list_average(self, l: list[float]) -> float:
        return sum(l) / len(l)

    def should_buy(self, prices: list[float]) -> bool:
        if self.trading_strategy == "minmax":
            return prices[-1] == min(prices)
        else:
            return prices[-1] < self.list_average(prices)

    def should_sell(self, prices: list[float]) -> bool:
        if self.trading_strategy == "minmax":
            return prices[-1] == max(prices)
        else:
            return prices[-1] > self.list_average(prices)

    def check_prices(self, coin: str):
        self.connect()
        prices = self.get_market_data(coin)
        should_buy = self.should_buy(prices)
        should_sell = self.should_sell(prices)
        if should_buy:
            print(f"You should buy {coin}")
        elif should_sell:
            print(f"You should sell {coin}")
        else:
            print(f"No action needed for {coin}")


app = Application("average")
app.check_prices("BTC/USD")
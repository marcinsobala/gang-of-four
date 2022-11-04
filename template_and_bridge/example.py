"""
By utilizing both Bridge & Template pattern you've now made it possible to modify
both Exchange and TradingBot independently of each other and still be able to use them together
thanks to TradingBot depending on the abstraction of an Exchange. Dependency inversion rules!
"""

from abc import ABC, abstractmethod


class Exchange(ABC):
    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def get_market_data(self, coin: str) -> list[float]:
        pass


class BinanceExchange(Exchange):
    def connect(self):
        print("Connecting to Binance Exchange")

    def get_market_data(self, coin: str) -> list[float]:
        return [10, 12, 18, 14]


class CoinbaseExchange(Exchange):
    def connect(self):
        print("Connecting to Coinbase Exchange")

    def get_market_data(self, coin: str) -> list[float]:
        return [20, 32, 27, 6]


class TradingBot(ABC):
    def __init__(self, exchange: Exchange):
        self.exchange = exchange

    @abstractmethod
    def should_buy(self, prices: list[float]) -> bool:
        pass

    @abstractmethod
    def should_sell(self, prices: list[float]) -> bool:
        pass

    def check_prices(self, coin: str):
        self.exchange.connect()
        prices = self.exchange.get_market_data(coin)
        should_buy = self.should_buy(prices)
        should_sell = self.should_sell(prices)
        if should_buy:
            print(f"You should buy {coin}")
        elif should_sell:
            print(f"You should sell {coin}")
        else:
            print(f"No action needed for {coin}")


class AverageTrader(TradingBot):
    def list_average(self, l: list[float]) -> float:
        return sum(l) / len(l)

    def should_buy(self, prices: list[float]) -> bool:
        return prices[-1] < self.list_average(prices)

    def should_sell(self, prices: list[float]) -> bool:
        return prices[-1] > self.list_average(prices)


class MinMaxTrader(TradingBot):
    def should_buy(self, prices: list[float]) -> bool:
        return prices[-1] == min(prices)

    def should_sell(self, prices: list[float]) -> bool:
        return prices[-1] == max(prices)


app = MinMaxTrader(CoinbaseExchange())
app.check_prices("BTC/USD")
class MoneyMachine:

    CURRENCY = "$"

    COIN_VALUES = {
        "четвертаков": 0.25,
        "десяток": 0.10,
        "пятерок": 0.05,
        "едениц": 0.01
    }

    def __init__(self):
        self.profit = 0
        self.money_received = 0

    def report(self):
        print(f"Деньги: {self.CURRENCY}{self.profit}")

    def process_coins(self):
        print("Введите монетки")
        for coin in self.COIN_VALUES:
            self.money_received += int(input(f"Сколько {coin}?: ")) * self.COIN_VALUES[coin]
        return self.money_received

    def make_payment(self, cost):
        self.process_coins()
        if self.money_received >= cost:
            change = round(self.money_received - cost, 2)
            print(f"{self.CURRENCY}{change} после покупки")
            self.profit += cost
            self.money_received = 0
            return True
        else:
            print("Извините у вас не хватает денег")
            self.money_received = 0
            return False
        

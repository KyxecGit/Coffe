class MenuItem:
    def __init__(self, name, water, milk, coffee, cost):
        self.name = name
        self.cost = cost
        self.ingredients = {
            "вода": water,
            "молоко": milk,
            "кофе": coffee
        }


class Menu:
    def __init__(self):
        self.menu = [
            MenuItem(name="латте", water=200, milk=150, coffee=24, cost=2.5),
            MenuItem(name="экспрессо", water=50, milk=0, coffee=18, cost=1.5),
            MenuItem(name="капучино", water=250, milk=50, coffee=24, cost=3),
        ]

    def get_items(self):
        options = ""
        for item in self.menu:
            options += f"{item.name}/"
        return options

    def find_drink(self, order_name):
        for item in self.menu:
            if item.name == order_name:
                return item
        print("Этот напиток недоступен")
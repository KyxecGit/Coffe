class CoffeeMaker:
    def __init__(self):
        self.resources = {
            "вода": 300,
            "молоко": 200,
            "кофе": 100,
        }

    def report(self):
        print(f"Вода: {self.resources['вода']}мл")
        print(f"Молоко: {self.resources['молоко']}мл")
        print(f"Кофе: {self.resources['кофе']}г")

    def is_resource_sufficient(self, drink):
        can_make = True
        for item in drink.ingredients:
            if drink.ingredients[item] > self.resources[item]:
                print(f"Извините недостаточно {item}.")
                can_make = False
        return can_make

    def make_coffee(self, order):
        for item in order.ingredients:
            self.resources[item] -= order.ingredients[item]
        print(f"Ваш {order.name} ☕️. Наслаждайтесь!")

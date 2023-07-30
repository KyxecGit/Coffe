from menu import *

def is_resource_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"​Извините у нас не хватает {item}.")
            return False
    return True


def process_coins():
    print("Введите ваши монеты")
    total = int(input("Сколько четвертинок?: ")) * 0.25
    total += int(input("Сколько десяток?: ")) * 0.1
    total += int(input("Сколько пятерок?: ")) * 0.05
    total += int(input("Сколько едениц?: ")) * 0.01
    return total


def is_transaction_successful(money_received, drink_cost):
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"{change}$ после размена")
        global profit
        profit += drink_cost
        return True
    else:
        print("Извините у вас недостаточно денег")
        return False


def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Возьмите ваш {drink_name} ☕️. Наслаждайтесь!")


is_on = True

while is_on:
    choice = input("​Что бы вы хотели? (espresso/latte/cappuccino): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])









from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
# item = MenuItem()
coffeeMaker = CoffeeMaker()
moneyMachine = MoneyMachine()

machine_on = True

while machine_on:
    choice = input(f"Make a selection: {menu.get_items()} ").lower()
    if choice == 'report':
        coffeeMaker.report()
        moneyMachine.report()
    elif choice == 'off':
        print("Turning off...")
        machine_on = False
    else:
        selected_drink = menu.find_drink(choice)

        if coffeeMaker.is_resource_sufficient(selected_drink):
            if moneyMachine.make_payment(selected_drink.cost):
                coffeeMaker.make_coffee(selected_drink)

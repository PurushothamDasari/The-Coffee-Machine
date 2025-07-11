from menu import Menu,MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# printing the report

coffee_maker=CoffeeMaker()
money_machine=MoneyMachine()
menu= Menu()
money =0

is_on = True

while is_on:
    options= menu.get_items()
    ask = input(f"What would you like? {options}").lower()
    if ask =="off":
        is_on = False
    elif ask =="report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(ask)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)
        else:
            is_on = False

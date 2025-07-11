from menu import Menu,MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
import pandas

# printing the report

coffee_maker=CoffeeMaker()
money_machine=MoneyMachine()
menu= Menu()
money =0

is_on = True

# Display input instructions.
print("\n\nINPUT INSTRUCTIONS\n1. To view menu, input=menu\n2. To view report, input=report\n3. To turn off machine, input=off\n4. To order an item, input=order name.\n")
while is_on:
    options= menu.get_items()
    ask = input(f"What would you like? {options}☕ ").lower()
    if ask =="off":
        is_on = False
    elif ask =="report":
        coffee_maker.report()
        money_machine.report()
    elif ask =="menu":
        data = pandas.read_csv('menu.txt')
        print(data)
    else:
        if menu.check_in_menu(ask):
            drink = menu.find_drink(ask)
            if coffee_maker.is_resource_sufficient(drink):
                if money_machine.make_payment(drink.cost):
                    coffee_maker.make_coffee(drink)
            else:
                is_on = False

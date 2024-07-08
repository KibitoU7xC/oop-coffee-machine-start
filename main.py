from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffe_maker=CoffeeMaker()
money_machine=MoneyMachine()
menu=Menu()

is_on=True

while is_on:
    choise=menu.get_items()
    drink=menu.find_drink(input((f"choose drink{choise}")))
    if drink=="report":
        coffe_maker.report()
        money_machine.report()
    elif drink=="off":
        is_on=False
    else:
        coffe_maker.is_resource_sufficient(drink)
        money_machine.make_payment(drink.cost)
        coffe_maker.make_coffee(drink)



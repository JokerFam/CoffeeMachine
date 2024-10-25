from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


def whatDrinkYouWant():
    print(Menu().get_items())
    userInput = str(input('What drink do you want? \n'))

    if CoffeeMaker().is_resource_sufficient(Menu().find_drink(userInput)) == True:
        if MoneyMachine().make_payment(Menu().find_drink('latte').cost) == True:
            CoffeeMaker().make_coffee(Menu().find_drink(userInput))
        else:
            MoneyMachine().make_payment(Menu().find_drink('latte').cost)
    else:
        print(CoffeeMaker().is_resource_sufficient(
            Menu().find_drink(userInput)))


def main():
    print()


if __name__ == "__main__":
    main()

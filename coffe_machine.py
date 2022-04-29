# Coffee
import main


class CoffeeMachine:
    def __init__(self):
        self.exit_status = 0

        def process_coins(coffee_type):
            money_counter = 0.0
            cost_of_coffee = main.MENU[coffee_type]['cost']
            print(f"Please insert/type coins one at a time equal to {'${:,.2f}'.format(cost_of_coffee)}")
            while money_counter < cost_of_coffee:
                print(f"Current amount entered: {'${:,.2f}'.format(money_counter)}")
                inserted_coin = input("Enter coin:")
                if inserted_coin not in main.coins:
                    print("Invalid selection. Please retype your coin.")
                else:
                    money_counter += main.coins[inserted_coin]
            if money_counter > cost_of_coffee:
                amount_returned = money_counter - cost_of_coffee
                print(f"You have inserted {'${:,.2f}'.format(amount_returned)} more than required. Here is your change!"
                      f"\n"
                      f"You have received {'${:,.2f}'.format(amount_returned)}.")
            main.money += cost_of_coffee
            print(f"Thank you! Here is your {coffee_type}. Enjoy!")

        def check_resources(coffee_type):
            print(f"You have chosen {coffee_type}")
            water = main.resources["water"]
            coffee = main.resources["coffee"]
            milk = main.resources["milk"]
            if coffee_type == "espresso":
                if water >= 50 and coffee >= 18:
                    main.resources["water"] -= 50
                    main.resources["coffee"] -= 18
                    process_coins(coffee_type)
                    return
                elif water < 50 and coffee < 18:
                    print(f"There is only {main.resources['water']}ml of water and {main.resources['coffee']}g of"
                          f" coffee remaining. Please select a different option.")
                elif water < 50:
                    print(f"There is only {main.resources['water']}ml of water remaining."
                          f" Please select a different option.")
                else:
                    print(f"There is only {main.resources['coffee']}g of coffee remaining."
                          f" Please select a different option.")
            elif coffee_type == "latte":
                if water >= 200 and coffee >= 24 and milk >= 150:
                    main.resources["water"] -= 200
                    main.resources["coffee"] -= 24
                    main.resources["milk"] -= 150
                    process_coins(coffee_type)
                    return
                elif water < 200 and coffee < 24:
                    print(f"There is only {main.resources['water']}ml of water and {main.resources['coffee']}g of"
                          f" coffee remaining. Please select a different option.")
                elif water < 200:
                    print(f"There is only {main.resources['water']}ml of water remaining."
                          f" Please select a different option.")
                elif coffee < 24:
                    print(f"There is only {main.resources['coffee']}g of coffee remaining."
                          f" Please select a different option.")
                else:
                    print(f"There is only {main.resources['milk']}ml of milk remaining."
                          f" Please select a different option.")
            elif coffee_type == "cappuccino":
                if water >= 250 and coffee >= 24 and milk >= 100:
                    main.resources["water"] -= 250
                    main.resources["coffee"] -= 24
                    main.resources["milk"] -= 100
                    process_coins(coffee_type)
                    return
                elif water < 250 and coffee < 24:
                    print(f"There is only {main.resources['water']}ml of water and {main.resources['coffee']}g of"
                          f" coffee remaining. Please select a different option.")
                elif water < 250:
                    print(f"There is only {main.resources['water']}ml of water remaining."
                          f" Please select a different option.")
                elif coffee < 24:
                    print(f"There is only {main.resources['coffee']}g of coffee remaining."
                          f" Please select a different option.")
                else:
                    print(f"There is only {main.resources['milk']}ml of milk remaining."
                          f" Please select a different option.")
            else:
                print("Invalid selection. Please try again")
                return

            print(f"Not enough resources to make {coffee_type}")

        def print_report():
            money = "test"
            print(f"""
Your current resources:
Water: {main.resources["water"]}ml 
Milk: {main.resources["milk"]}ml 
Coffee: {main.resources["coffee"]}g 
Money: {'${:,.2f}'.format(main.money)}
""")

        def check_input(entered):
            lowercase_entered = entered.lower()
            if lowercase_entered == "off":
                print("You have chosen to turn off the machine. Bye!")
                exit(0)
            elif lowercase_entered == "report":
                print_report()
            else:
                check_resources(lowercase_entered)
        self.coffee_type = input("What would you like? (espresso/latte/cappuccino):")
        check_input(self.coffee_type)


while True:
    test = CoffeeMachine()


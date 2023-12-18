from actions.remove import remove_screen
from actions.view import view_screen
from prettytable import PrettyTable
from colorama import Fore, Back, Style
import colorama
from actions.add import add_items


colorama.init()

groceries = {}
categories = [Fore.WHITE+"diary_products", "meat_products", "snacks", "grains"]

while True:
    print(Fore.YELLOW+"Welcome to shopping list tracker")
    print(Fore.YELLOW+"\nMenu:")
    print(Fore.WHITE+"1.Add\n2.Remove\n3.View")
    print(Fore.RED+"4.Exit")
    
    op = int(input(Fore.YELLOW+"Choose an option:"))

    if op == 1:
        #add screen
        add_items(groceries,categories)
    if op == 2:
        remove_screen(groceries, categories)

    if op == 3:
        view_screen(groceries)

    if op == 4:
        print("\nThank you for using shopping list tracker!")
        print()
        break

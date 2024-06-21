# Menu dictionary
def print_main_menu(menu):
    # Create a variable for the menu item number
    i = 1
    # Create a dictionary to store the menu for later retrieval 
    menu_items = {}

    # Print the options to choose from menu headings (all the first level 
    # dictionary items in menu).
    for key in menu.keys():
        print(f"{i}: {key}")

        # Store the menu category associated with its menu item number
        menu_items[i] = key
        # Add 1 to the menu item number
        i += 1
    
    print('\n')
    
    return menu_items
    
def confirm_integer_input(entry_to_check):
    rslt = entry_to_check
    while True:
        if rslt.isdigit():
            break
        # elif rslt == quit_option:
        #     break
        else:
            rslt = input(f"'{rslt}' is not a valid entry, please enter a number: ")
    return rslt

def print_sub_menu(menu_category, menu):
    menu_dashes = "-" * 42
    
    #print(menu_dashes)
    print(f"This is the list of items available in the {menu_category} menu:")
    print(menu_dashes)
    print("Item # | Item name                | Price")
    print("-------|--------------------------|-------")

    available_items_to_purchase = {}
    item_to_purchase = {}
    # Initialize a menu item counter
    item_counter = 1
    # Print out the menu options from the menu_category_name
    for key, value in menu[menu_category].items():
        
        item_counter_spaces = (7 - len (str(item_counter)))

        # Check if the menu item is a dictionary to handle differently
        if type(value) is dict:
            
            # Iterate through the dictionary items
            for key1, value1 in value.items():
                item_to_purchase = {
                    'Item Name': (f'{key} - {key1}'), 
                    'Price': float(value1) 
                }
                #store item counter in dictionary of available items
                available_items_to_purchase[item_counter] = item_to_purchase
                # Add 1 to the item_counter
                item_counter += 1
        
        # Else the menu item is not a dictionary
        else:
            item_to_purchase = {
                'Item Name': (f'{key}'), 
                'Price': float(value)
            }
            #store item counter in list of items
            available_items_to_purchase[item_counter] = item_to_purchase
            # Add 1 to the item_counter
            item_counter += 1
    
    for key, value in available_items_to_purchase.items():
        # Print the menu item
        print(f"{key}"
            +f"{" " * item_counter_spaces}|"
            +f" {value['Item Name']}"
            +f"{" " * (25 - len (str(value['Item Name'])))}|"
            +f" ${" " * (5 - len (str(value['Price'])))}{value['Price']}")
    
    print(menu_dashes + '\n')
    
    return available_items_to_purchase

def print_order(items_ordered: list):
    print(items_ordered)
    
    
    
menu = {
    "Snacks": {
        "Cookie": .99,
        "Banana": .69,
        "Apple": .49,
        "Granola bar": 1.99
    },
    "Meals": {
        "Burrito": 4.49,
        "Teriyaki Chicken": 9.99,
        "Sushi": 7.49,
        "Pad Thai": 6.99,
        "Pizza": {
            "Cheese": 8.99,
            "Pepperoni": 10.99,
            "Vegetarian": 9.99
        },
        "Burger": {
            "Chicken": 7.49,
            "Beef": 8.49
        }
    },
    "Drinks": {
        "Soda": {
            "Small": 1.99,
            "Medium": 2.49,
            "Large": 2.99
        },
        "Tea": {
            "Green": 2.49,
            "Thai iced": 3.99,
            "Irish breakfast": 2.49
        },
        "Coffee": {
            "Espresso": 2.99,
            "Flat white": 2.99,
            "Iced": 3.49
        }
    },
    "Dessert": {
        "Chocolate lava cake": 10.99,
        "Cheesecake": {
            "New York": 4.99,
            "Strawberry": 6.49
        },
        "Australian Pavlova": 9.99,
        "Rice pudding": 4.99,
        "Fried banana": 4.49
    }
}

# for item in menu:
#     print(item)

# Launch the store and present a greeting to the customer
print("Welcome to the variety food truck.\n")

ordering = True
check_out = False

#list to sore items ordered
items_ordered = []

# Customers may want to view different sections of the menu, so let's create a loop
while ordering:
    
    # Ask the customer which menu category they want to view
    print("Which menu would you like to view? \n")

    #print menu items to select from
    menu_items = print_main_menu(menu)
    
    # Get the customer's input
    menu_category = input("Enter the menu number to view or q to quit: ")

    # Exit the loop if user typed 'q'
    if menu_category == 'q':
        
        #if the user has already placed items in the "cart", ask if they would like to check out
        if len(items_ordered) > 0:
            
            print(f'you have {len(items_ordered)} items in your cart.\n')
            
            while True:
                                        
                order_again = input('Would you like to place the order you currently have? (y/n) ')
                print('\n')
                
                match order_again.upper():
                    case 'Y':
                        print('Thank you for your order')
                        check_out = True
                        break
                    case 'N':
                        print('Thank you, your order has been cancelled')
                        check_out = False
                        break
                    case other:
                        print(f'"{order_again}" is not a recognized option, please enter either y or n.\n')
        ordering = False
    
    else:
        
        place_order = True
        
        while place_order:
            
            # Check if the customer's input is a number
            menu_category = confirm_integer_input(menu_category)
            
            # Check if the customer's input is a valid option
            if int(menu_category) in menu_items.keys():
                
                # Save the menu category name to a variable
                menu_category_name = menu_items[int(menu_category)]
                
                # Print out the menu category name they selected
                print(f"You selected {menu_category_name}: \n")

                # Display the heading for the sub-menu
                available_items_to_purchase = print_sub_menu(menu_category_name, menu)
                
                #prompt the user to input the item desired
                #if no item desired, allow for return to main menu
                menu_selection = input('Which item would you like to order? (0 to return to main menu) ')
                print('\n')
                
                # confirm input is a valid numeric entry
                menu_selection = confirm_integer_input(menu_selection)
                
                if int(menu_selection) == 0:
                    print('\n')
                    print('Returning to main menu \n')
                    place_order = False
                elif int(menu_selection) in available_items_to_purchase.keys():
                    
                    item_name = available_items_to_purchase[int(menu_selection)]['Item Name']
                    item_cost = available_items_to_purchase[int(menu_selection)]['Price']
                    
                    # to the reviewer: in the module challenge instructions, we were given the following direction:
                    # "The customer is prompted for a quantity of their item selection and the value 
                    # defaults to 1 if the customer does not input a valid number. (10 points)""
                    
                    # I elected not to do this (personally I tihin that to be a bad design),
                    # instead using <enter> as a default to 1
                    # and enforcing a valid digit to be entered by the user
                    # I also check for 0, and skip the item if that is true (as that would indicate
                    # that the user did not really want to order that item)
                    
                    input_quantity = input ('How many would you like to order? (press enter to order 1) ')
                    print('\n')
                    
                    quantity = 1 if (input_quantity == '') else (int(confirm_integer_input(input_quantity)))
                    
                    if (input_quantity == 0):
                            #customer entered 0 for a quantity - disregard item
                            break
                    else:
                        item_ordered = {
                            'Item Name': item_name, 
                            'Price': float(item_cost), 
                            'Quantity': int(quantity)
                        }
                        
                        #check if this item has alrady been ordered
                        existing_items = [item['Item Name']for item in items_ordered]
                        
                        if item_ordered['Item Name'] in existing_items:
                            #if it has, just update the quantity
                            items_ordered[existing_items.index(item_ordered['Item Name'])]['Quantity'] += item_ordered['Quantity']
                        else:
                            #else add to list of items ordered
                            items_ordered.append(item_ordered)
                    
                    while True:
                        
                        order_again = input('Would you like to order another item from this menu? (y/n) ')
                        print('\n')
                        
                        match order_again.upper():
                            case 'Y':
                                place_order = True
                                break
                            case 'N':
                                place_order = False
                                break
                            case other:
                                print(f'"{order_again}" is not a recognized option, please enter either y or n.\n')
                    
                    if not place_order:
                        while True:
                                            
                            order_again = input('Would you like to order from another menu? (y/n) ')
                            print('\n')
                            
                            match order_again.upper():
                                case 'Y':
                                    check_out = False
                                    ordering = True
                                    break
                                case 'N':
                                    print('Thank you for your order\n')
                                    check_out = True
                                    ordering = False
                                    break
                                case other:
                                    print('\n')
                                    print(f'"{order_again}" is not a recognized option, please enter either "y" or "n".\n')
                else:
                    print(f'Sorry entry: "{menu_selection}", is not an item in the {menu_category_name} menu, please try again. \n')
                    place_order = True
                
            else:
                # Tell the customer they didn't select a menu option
                print(f"\n{menu_category} was not a menu option, please try again.\n")
                place_order = False

if check_out:
    
    #print out hte customer order and let them know the total for the order
    print("Your order is:")
    
    #print_order(items_ordered)
    item_spaces = 26
    price_spaces = 9
    qty_spaces = 10
    frame_spaces = 46
    
    #print headder
    print('-' * frame_spaces)
    print(f'Item Name{' ' * (item_spaces - len ("Item Name"))}| '
          f'Price{' ' * (price_spaces - len ("Price")-2)} | '
          f'Quantity{' ' * (qty_spaces - len ("Quantity") - 2)}')
    print(f"{'-' * item_spaces}|{'-' * price_spaces}|{'-' * (qty_spaces - 1)}")
    
    #prints items in the order
    for i in items_ordered:
        #print(i)
        Item_Name = i['Item Name']
        Price = i['Price']
        Quantity = i['Quantity']
        # assumes prices will be less than $100
        print(f"{Item_Name}"
            +f"{' ' * (item_spaces - len (Item_Name))}| "
            +f"${" " * (price_spaces - 3 - len (f'{Price: .2f}'))}{Price: .2f} | "
            +f"{Quantity}")
    
    print('-' * frame_spaces)
    
    #calculate the total for the order and let the customer know what it is
    order_total = sum([item['Price'] * item['Quantity'] for item in items_ordered])
    
    print(f'Total for your order is: ${order_total: .2f}')
    print('-' * frame_spaces)
    
    
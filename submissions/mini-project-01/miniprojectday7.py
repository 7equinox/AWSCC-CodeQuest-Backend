# Function to exit the program
def funct_opt_quit():
    print("Goodbye!")
    exit()


# Function to remove an item from the shopping list
def funct_opt_remove(shopping_list):
    # Check if the shopping list is empty
    if len(shopping_list) == 0:
        print("Your shopping list is empty.\n")
        return

    # Keep asking for an item to remove until a non-empty input is provided
    while True:
        str_input_remove_item = input("Enter the item you want to remove: ").strip()
        str_input_remove_item = str_input_remove_item.title()
        if str_input_remove_item == '':
            print("Invalid input. Please try again.")
        else:
            break

    # If the item is in the shopping list, remove it
    if str_input_remove_item in shopping_list:
        shopping_list.remove(str_input_remove_item)
        print(f"{str_input_remove_item} has been removed from your shopping list.\n")
    else:
        print(f"{str_input_remove_item} is not in your shopping list.\n")


# Function to view the items in the shopping list
def funct_opt_view(shopping_list):
    print("Your shopping list:")

    # Check if the shopping list is empty
    if shopping_list == []:
        print("None")

    # Print each item in the shopping list
    for item in shopping_list:
        print(item)
    print()


# Function to add an item to the shopping list
def funct_opt_add(shopping_list):
    # Keep asking for an item to add until a non-empty input is provided
    while True:
        str_input_add_item = input("Enter the item you want to add: ").strip()
        str_input_add_item = str_input_add_item.title()
        if str_input_add_item == '':
            print("Invalid input. Please try again.")
        else:
            break

    # If the item is not in the shopping list, add it
    if str_input_add_item in shopping_list:
        print(f"{str_input_add_item} is already in your shopping list.\n")
    else:
        shopping_list.append(str_input_add_item)
        print(f"{str_input_add_item} has been added to your shopping list.\n")


# Function to handle the main menu options
def funct_main_opt(shopping_list):
    # Print the main menu options
    print("""Options:
1. Add item to the shopping list
2. View shopping list
3. Remove item from the shopping list
4. Quit""")
    
    # Get the user's choice
    str_input_choice = input("Enter the number of your choice: ")
    
    # Handle the user's choice
    if str_input_choice == '1':
        funct_opt_add(shopping_list)
    elif str_input_choice == '2':
        funct_opt_view(shopping_list)
    elif str_input_choice == '3':
        funct_opt_remove(shopping_list)
    elif str_input_choice == '4':
        funct_opt_quit()
    else:
        print("Invalid input. Please try again.\n")
        
    # Call the function again to display the main menu options
    funct_main_opt(shopping_list)


# Function to initialize the shopping list and starts the program
def funct_init_list():
    shopping_list = []
    print("Shopping List\n")
    funct_main_opt(shopping_list)


if __name__ == "__main__":
    funct_init_list()

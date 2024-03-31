import json

# Define the PasswordManagerApp class
class PasswordManagerApp:
    # Initialize the class with a JSON file
    def __init__(self, json_file: str):
        # Create an empty dictionary to store the app
        self.__dict_app = {}
        self.__json_file = f"C:/Users/JE/Desktop/Program/AWSCC-CodeQuest-Backend/backend/day-28-30/practice3/menu-sample/{json_file}.json"
        # Open the JSON file and load its data into the dictionary
        with open(self.__json_file, 'r') as file:
            if file.read().strip():
                file.seek(0)
                data = json.load(file)
                if data is not None:
                    for name_of_website, login in data.items():
                        self.__dict_app[name_of_website] = login

    # Method to add a new entry to the password manager
    def add_manager(self):
        # Get user input for website, email, and password
        self.__input_website()
        self.__input_email()
        self.__input_password()
        # Add the new entry to the dictionary
        if self.__website not in self.__dict_app:
            self.__dict_app[self.__website] = []
        self.__dict_app[self.__website].append(
            {'email': self.__email, 'password': self.__password})
        # Write the updated dictionary back to the JSON file
        self.__write_file(1)

    # Method to get user input for the website name
    def __input_website(self):
        while True:
            try:
                print("=====================================================")
                name_of_website = input("Enter name of website: ").strip()
                if not name_of_website:
                    raise Exception
            except Exception:
                self.invalid_input()
                continue
            else:
                self.__website = name_of_website
                break

    # Property for the website name
    @property
    def __website(self) -> str:
        return self.__name_of_website

    # Setter for the website name
    @__website.setter
    def __website(self, website: str):
        self.__name_of_website = website

    # Method to get user input for the email address
    def __input_email(self):
        while True:
            try:
                print("=====================================================")
                email_address = input("Enter email: ").strip()
                if not email_address:
                    raise Exception
            except Exception:
                self.invalid_input()
                continue
            else:
                self.__email = email_address
                break

    # Property for the email address
    @property
    def __email(self) -> str:
        return self.__email_address

    # Setter for the email address
    @__email.setter
    def __email(self, email: str):
        self.__email_address = email

    # Method to get user input for the password
    def __input_password(self):
        while True:
            try:
                print("=====================================================")
                password = input("Enter password: ").strip()
                if not password:
                    raise Exception
            except Exception:
                self.invalid_input()
                continue
            else:
                self.__password = password
                break

    # Property for the password
    @property
    def __password(self) -> str:
        return self.__password_value

    # Setter for the password
    @__password.setter
    def __password(self, password: str):
        self.__password_value = password

    # Method to print all entries in the password manager
    def __str__(self) -> str:
        print("=====================================================")
        view_inputs = ""
        no_inputs = True
        for website, login in self.__dict_app.items():
            for data in login:
                no_inputs = False
                view_inputs += f"Website: {website}\n"
                view_inputs += f"\tEmail: {data['email']}\n"
                view_inputs += f"\tPassword: {data['password']}\n\n"    
        # If no inputs are found, print a message
        if no_inputs:
            return "No inputs found!"
        return view_inputs[:-2]

    # Method to search for a specific entry in the password manager
    def operation_manager(self, function_number=0):
        # If no inputs are found, print a message and return
        if not self.__dict_app:
            print("=====================================================")
            print("No inputs found!")
            return
        while True:
            try:
                print("=====================================================")
                name_of_website = input("Enter website: ").strip()
                if not name_of_website:
                    raise Exception
            except Exception:
                self.invalid_input()
                continue
            else:
                self.__search(name_of_website, function_number)
                break

    # Method to search for a specific website in the dictionary
    def __search(self, name_of_website: str, function_number: int):
        print("=====================================================")
        counting_number = 0
        no_website = True
        # Create a copy of the dictionary items
        items = list(self.__dict_app.items())
        for website, login in items:
            # Check if the input website is in the dictionary with case-insensitive comparison
            if website.lower() == name_of_website.lower():
                no_website = False
                print(f"Website: {website}")
                for data in login:
                    counting_number += 1
                    print(f"\t[{counting_number}] Email: {data['email']}")
                    print(f"\t    Password: {data['password']}")
                if function_number in [4, 5]:
                    self.__operation(website, function_number, counting_number)
        if no_website:
            print("Website not found!")

    # Method to delete or update a specific entry in the password manager
    def __operation(self, name_of_website: str, function_number: int, counting_number: int):
        while True:
            try:
                print("=====================================================")
                # If the function_number is 4, it means the user wants to delete an entry
                if function_number == 4:
                    num = int(input("Enter the number you want to delete: "))
                # Otherwise, the user wants to update an entry
                else:
                    num = int(input("Enter the number you want to update: "))
                if num not in range(1, counting_number + 1):
                    raise Exception
            except Exception:
                self.invalid_input()
                continue
            else:
                # If the function_number is 4, delete the entry
                if function_number == 4:
                    self.__dict_app[name_of_website].pop(num - 1)
                    # If there are no more entries for the website, remove the website from the dictionary
                    if len(self.__dict_app[name_of_website]) == 0:
                        self.__dict_app.pop(name_of_website)
                    # Write the updated dictionary back to the JSON file
                    self.__write_file(4)
                # Otherwise, update the entry
                else:
                    self.__update(name_of_website, num)
                break

    # Method to update a specific entry in the password manager
    def __update(self, name_of_website: str, num: int):
        while True:
            try:
                print("=====================================================")
                # Ask the user whether they want to update the email or the password
                input_type = int(
                    input("Enter '1' for email or '2' for password: "))
                if input_type not in [1, 2]:
                    raise Exception
            except Exception:
                self.invalid_input()
                continue
            else:
                break
        # Update the specified entry with the new input
        self.__update_input(name_of_website, num, input_type)
        # Write the updated dictionary back to the JSON file
        self.__write_file(5)

    # Method to get the new input from the user and update the specified entry
    def __update_input(self, name_of_website: str, num: int, input_type: int):
        while True:
            try:
                print("=====================================================")
                # If the input_type is 1, it means the user wants to update the email
                if input_type == 1:
                    email_address = input("Enter your new email: ").strip()
                    if not email_address:
                        raise Exception
                # Otherwise, the user wants to update the password
                else:
                    password = input("Enter your new password: ").strip()
                    if not password:
                        raise Exception
            except Exception:
                self.invalid_input()
                continue
            else:
                # If the input_type is 1, update the email of the specified entry
                if input_type == 1:
                    self.__dict_app[name_of_website][num -
                                                     1]['email'] = email_address
                # Otherwise, update the password of the specified entry
                else:
                    self.__dict_app[name_of_website][num -
                                                     1]['password'] = password
                break

    # Method to write the updated dictionary back to the JSON file
    def __write_file(self, function_number: int):
        with open(self.__json_file, 'w') as file:
            json.dump(self.__dict_app, file, indent = 4)
        print("=====================================================")
        if function_number == 1:
            print("Added successfully!")
        elif function_number == 4:
            print("Deleted successfully!")
        else:
            print("Updated successfully!")

    # Method to print an error message when the user enters an invalid input
    def invalid_input(self):
        print("=====================================================")
        print("Invalid input!")


# This function serves as the main menu for the Password Manager Application
def main_menu():
    # Create an instance of the PasswordManagerApp class
    app = PasswordManagerApp("PasswordManagerApp1")
    # Keep the application running until the user chooses to exit
    while True:
        # Print the main menu options
        print("=====================================================")
        print("             Password Manager Application            ")
        print("=====================================================")
        print("[1] Add a Password, Email, and Name of Website.")
        print("[2] View all inputs.")
        print("[3] Search for a specific input.")
        print("[4] Delete an existing input.")
        print("[5] Update a specific input.")
        print("[6] Exit.")
        print("=====================================================")
        try:
            # Get the user's choice
            choice = int(input("Enter the number of your choice: "))
            if choice not in range(1, 7):
                raise Exception
        except Exception:
            app.invalid_input()
            continue
        else:
            # Perform the appropriate action based on the user's choice
            if choice == 1:
                app.add_manager()
            elif choice == 2:
                print(app)
            elif choice == 3:
                app.operation_manager()
            elif choice == 4:
                app.operation_manager(4)
            elif choice == 5:
                app.operation_manager(5)
            else:
                # If the user chooses to exit, print a goodbye message and break the loop
                print("=====================================================")
                print("Thank you for using Password Manager Application!")
                print("=====================================================")
                break


# If this script is run directly (not imported as a module), call the main_menu function
if __name__ == "__main__":
    main_menu()

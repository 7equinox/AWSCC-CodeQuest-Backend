# Class for Password Manager App
class PasswordManagerApp:
    def __init__(self):
        self.__dict_app = {}

    # For inputting the website, email and password
    def input_manager(self):
        self.__name_of_website = input("Enter name of website: ")
        self.__email = input("Enter email: ")
        self.__password = input("Enter password: ")
        print()
        self.__add_manager(self.__name_of_website,
                           self.__email, self.__password)

    # For adding the website, email and password to the dictionary
    def __add_manager(self, name_of_website, email, password):
        self.__dict_app[name_of_website] = [email, password]

    # For displaying the website, email and password
    def __str__(self):
        all_inputs = ""
        for name_of_website, login in self.__dict_app.items():
            all_inputs += f"""Website: {name_of_website}\
                \n\tEmail: {login[0]}\
                \n\tPassword: {login[1]}\n\n"""
        return all_inputs


# Main
if __name__ == "__main__":
    app = PasswordManagerApp()
    app.input_manager()
    app.input_manager()
    app.input_manager()
    print(app)

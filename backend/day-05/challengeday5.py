import random

def funct_guess_the_day_of_the_week():
    day_list = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    computer_choice = random.choice(day_list)

    str_guest = input("Enter your guess: ")

    if (str_guest.lower()) == (computer_choice.lower()):
        print(f"You guessed it right! It's {computer_choice}!")
    elif (str_guest.lower()) != (computer_choice.lower()):
        print(f"You guessed it wrong! It's {computer_choice}!")
    else:
        print("Invalid input. Please try again.\n")
        funct_guess_the_day_of_the_week()
        
        
if __name__ == "__main__":
    print("Guess the day of the week!\n")
    funct_guess_the_day_of_the_week()
def funct_dont_interact_animals_ending():
    print("""\nYou decide not to interact with the animals and continue your journey. As you walk further, \
you discover a hidden path that leads to a peaceful and serene sanctuary. Congratulations, you have found the good ending!""")


def funct_interact_animals_ending():
    print("""\nYou approach the friendly animals, and they lead you to a hidden treasure buried in the meadow. \
Congratulations, you have found the good ending!""")


def funct_dont_enter_cave_ending():
    print("""\nYou decide not to enter the cave and continue exploring the meadow. As you wander, \
you stumble upon a hidden grove filled with beautiful flowers and rare herbs. Congratulations, you have found the good ending!""")


def funct_enter_cave_ending():
    print("""\nYou bravely enter the cave, only to find a ferocious bear guarding its territory. \
The bear attacks, and you are unable to defend yourself. Unfortunately, this is the bad ending. Better luck next time!""")


def funct_dont_pick_stone_ending():
    print("""\nYou leave the stone behind and continue your journey. \
Suddenly, you come across a wise old hermit who imparts valuable knowledge and guidance. Congratulations, you have found the good ending!""")


def funct_pick_stone_ending():
    print("""\nAs you pick up the stone, a sudden gust of wind blows through the forest. The stone begins to glow, \
and you find yourself transported to a magical realm. You have unlocked a portal to a world of wonders! \
Congratulations, you have found the good ending!""")


def funct_dont_enter_cabin_ending():
    print("""\nYou decide not to enter the cabin and continue your journey. As you explore further, \
you stumble upon a magical waterfall that grants you a wish. Congratulations, you have found the good ending!""")


def funct_enter_cabin_ending():
    print("""\nYou cautiously enter the cabin, and to your surprise, you find a treasure chest filled with gold and jewels. \
You have stumbled upon a hidden treasure! Congratulations, you have found the good ending!""")


def funct_dont_follow_stream():
    print("""\nYou decide to continue walking through the meadow, enjoying the tranquility of nature. \
Suddenly, you come across a group of friendly animals.\n""")
    
    str_input_ans7 = input("Do you want to interact with them? (Yes/No): ")
    if str_input_ans7.lower() == "yes":
        funct_interact_animals_ending()
    elif str_input_ans7.lower() == "no":
        funct_dont_interact_animals_ending()
    else:
        print("Invalid input. Please try again.")
        funct_dont_follow_stream()


def funct_follow_stream():
    print("""\nYou follow the gentle flow of the stream, enjoying the peaceful ambiance. \
As you walk along its banks, you spot a hidden cave entrance.\n""")
    
    str_input_ans6 = input("Do you want to enter the cave? (Yes/No): ")
    if str_input_ans6.lower() == "yes":
        funct_enter_cave_ending()
    elif str_input_ans6.lower() == "no":
        funct_dont_enter_cave_ending()
    else:
        print("Invalid input. Please try again.")
        funct_follow_stream()


def funct_dont_explore_deep_forest():
    print("""\nYou decide to turn back, feeling a sense of unease. \
As you retrace your steps, you notice a peculiar-looking stone on the forest floor.\n""")
    
    str_input_ans5 = input("Do you want to pick up the stone? (Yes/No): ")
    if str_input_ans5.lower() == "yes":
        funct_pick_stone_ending()
    elif str_input_ans5.lower() == "no":
        funct_dont_pick_stone_ending()
    else:
        print("Invalid input. Please try again.")
        funct_dont_explore_deep_forest()


def funct_explore_deep_forest():
    print("""\nYou summon your courage and press on, determined to uncover the secrets of the forest. \
The air grows colder, and the sounds around you become more unsettling. \
Suddenly, you stumble upon an old, abandoned cabin.\n""")
    
    str_input_ans4 = input("Do you want to enter the cabin? (Yes/No): ")
    if str_input_ans4.lower() == "yes":
        funct_enter_cabin_ending()
    elif str_input_ans4.lower() == "no":
        funct_dont_enter_cabin_ending()
    else:
        print("Invalid input. Please try again.")
        funct_explore_deep_forest()


def funct_dont_go_forest():
    print("""\nYou choose to take the path to the meadow. The warm sunlight bathes the grassy expanse, \
and you can hear the gentle chirping of birds. As you walk further, you notice a sparkling stream nearby.\n""")
    
    str_input_ans3 = input("Do you want to follow the stream? (Yes/No): ")
    if str_input_ans3.lower() == "yes":
        funct_follow_stream()
    elif str_input_ans3.lower() == "no":
        funct_dont_follow_stream()
    else:
        print("Invalid input. Please try again.")
        funct_dont_go_forest()


def funct_go_forest():
    print("""\nYou decide to venture into the forest. As you step into the dense foliage, \
you feel a chill run down your spine. The trees loom overhead, casting eerie shadows on the forest floor. \
You hear strange rustling sounds and distant whispers.\n""")
    
    str_input_ans2 = input("Will you continue exploring deeper into the forest? (Yes/No): ")
    if str_input_ans2.lower() == "yes":
        funct_explore_deep_forest()
    elif str_input_ans2.lower() == "no":
        funct_dont_explore_deep_forest()
    else:
        print("Invalid input. Please try again.")
        funct_go_forest()


def funct_adventure_start():
    print("""\nYou find yourself standing at a crossroad. There are two paths ahead of you. \
One leads to a dark and mysterious forest, \
while the other leads to a bright and sunny meadow.\n""")
    
    str_input_ans1 = input("Do you want to go to the forest? (Yes/No): ")
    if str_input_ans1.lower() == "yes":
        funct_go_forest()
    elif str_input_ans1.lower() == "no":
        funct_dont_go_forest()
    else:
        print("Invalid input. Please try again.")
        funct_adventure_start()


if __name__ == "__main__":
    print("Adventure of the !Good Ending")
    funct_adventure_start()
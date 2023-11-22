int_num = int(input("Enter a number: "))

if int_num < 0:
    print(f"{int_num} is a Negative number!")
elif int_num == 0:
    print("That number is a Zero!")
else:
    print(f"{int_num} is a Positive number!")
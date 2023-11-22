int_input_limit = int(input("Limit: "))
i = 1

print()
while (i <= int_input_limit):
    if (i % 3 == 0) and (i % 5 == 0):
        print("FizzBuzz!")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
    i += 1
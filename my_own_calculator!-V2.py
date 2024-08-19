import time

print("Hello! Welcome to my first ever calculator made in Python!")

time.sleep(2.7)

while True:
    operation = input("What operation do you wish to perform? 1 for addition, 2 for substraction, 3 for multiplication and 4 for division. ")
    if operation == "1" or operation == "2" or operation == "3" or operation == "4":
        break
    else:
        print("Please choose a valid operation.")

if operation == "1":
    print("You chose addition!")
    time.sleep(1.5)
    print("Please choose the numbers you wish to perform the addition with.")
    time.sleep(1)

    while True:
        number_1_addition = input("Number 1: ")
        if number_1_addition.isdigit():
            number_1_addition = int(number_1_addition)
            break
        else:
            print("That's not a valid option. Choose a number.")

    while True:
        number_2_addition = input("Number 2: ")
        if number_2_addition.isdigit():
            number_2_addition = int(number_2_addition)
            break
        else:
            print("That's not a valid option. Choose a number.")
    print("The result is: " + str(number_1_addition + number_2_addition))

elif operation == "2":
    print("You chose substraction!")
    time.sleep(1.5)
    print("Please choose the numbers you wish to perform the substraction with.")
    time.sleep(1)

    while True:
        number_1_substraction = input("Number 1: ")
        if number_1_substraction.isdigit():
            number_1_substraction = int(number_1_substraction)
            break
        else:
            print("That's not a valid option. Choose a number.")

    while True:
        number_2_substraction = input("Number 2: ")
        if number_2_substraction.isdigit():
            number_2_substraction = int(number_2_substraction)
            break
        else:
            print("That's not a valid option. Choose a number.")
    print("The result is: " + str(number_1_substraction - number_2_substraction))

elif operation == "3":
    print("You chose multiplication!")
    time.sleep(1.5)
    print("Please choose the numbers you wish to perform the multiplication with.")
    time.sleep(1)
    while True:
        number_1_multiplication = input("Number 1: ")
        if number_1_multiplication.isdigit():
            number_1_multiplication = int(number_1_multiplication)
            break
        else:
            print("That's not a valid option. Choose a number.")

    while True:
        number_2_multiplication = input("Number 2: ")
        if number_2_multiplication.isdigit():
            number_2_multiplication = int(number_2_multiplication)
            break
        else:
            print("That's not a valid option. Choose a number.")
    print("The result is: " + str(number_1_multiplication * number_2_multiplication))

elif operation == "4":
    print("You chose division!")
    time.sleep(1.5)
    print("Please choose the numbers you wish to perform the division with.")
    time.sleep(1)
    while True:
        number_1_division = input("Number 1: ")
        if number_1_division.isdigit():
            number_1_division = int(number_1_division)
            break
        else:
            print("That's not a valid option. Choose a number.")

    while True:
        number_2_division = input("Number 2: ")
        if number_2_division.isdigit():
            number_2_division = int(number_2_division)
            break
        else:
            print("That's not a valid option. Choose a number.")
    print("The result is: " + str(number_1_division / number_2_division))



##### This calculator is the best I can make for now! I did it with a bit of help with chatGPT, but 97% of the thinking
##### and coding was only me. I'll make a better version once I can!

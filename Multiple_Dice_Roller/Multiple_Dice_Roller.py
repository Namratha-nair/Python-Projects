import random                    #use the random module to generate a random number

print("Welcome to the Multiple Dice Roller")
n = input("Enter the number of dice you want to roll: ")
n = int(n)                       # convert it to integer datatype


def roll_dice():                 # define a function to roll the dice
    return random.randint(1, 6)  # produce a random number from 1 to 6


output = []                      # create an empty list to store the output



option = "y"                     # initially set the user preference to roll the dice as yes

if n > 0:                        # check if the number of dice value is valid
    while option == "y":
        for i in range(n):       # to generate the output for all the dice
            x = roll_dice()
            output.append(x)
        print("The output for " + str(n) + " dice:")
        print(output)            # display the output
        output = []              # reset the output to an empty list after every roll
        print("\n")
        option = input(
            "Press y to roll again or press any other key to exit: ")
        print("\n")
else:
    print("Error: Try entering a valid dice number above 0")

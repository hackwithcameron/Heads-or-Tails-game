import random

money = 100


# Write your game of chance functions here
def heads_tails(guess, bet):
    global money
    answer = random.choice(["heads", "tails"])
    print(answer)
    try:
        if money >= int(bet):
            if guess == answer:
                money += int(bet)
                print("Correct!!! you win {winnings}".format(winnings=str(bet)))
                return "You have " + str(money)
            elif guess == answer:
                money += int(bet)
                print("Correct!!! you win {winnings}".format(winnings=str(bet)))
                return "You have " + str(money)
            else:
                money -= int(bet)
                print("Sorry incorrect, please try again!")
                return "You have " + str(money)
        else:
            return "Not enough money."
    except ValueError:
        return "incorrect key"

#Call function
while money > 0:
    print(heads_tails(input("please enter guess: "), input("please enter bet: ")))

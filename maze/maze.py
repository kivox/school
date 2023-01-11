import random as r

gShields = 3


def welcomeMessage():
    print("You are lost in a maze...")
    print("I'm afraid there are monsters that are quite keen on eating you")


def takeTurn():
    input("You have come to a junction. Turn left (L) or right (R)?")
    random = r.randint(1, 10)

    print(random)

    if random == 1:
        print("You have found the exit!")
        return True
    elif random == 2:
        print("You found a shield")
        getShield(1)
        return False
    elif random == 3:
        print("You found two shields")
        getShield(2)
        return False
    elif random == 4:
        print("You found a monster")
        loseShield()
        return False
    elif random == 5:
        print("You found two monsters")
        loseShield()
        loseShield()
        return False
    elif random == 6:
        print("You found a monster")
        loseShield()
        return False
    elif random == 7:
        print("You found two monsters")
        loseShield()
        return False
    elif random == 8:
        print("You found a monster")
        loseShield()
        return False
    elif random == 9:
        print("You found two monsters")
        loseShield()
        loseShield()
        return False
    elif random == 10:
        print("You found a monster")
        loseShield()
        return False
    else:
        return False


def getShield(number):
    global gShields
    gShields = gShields + number


def loseShield():
    global gShields
    gShields = gShields - 1
    if gShields < 0:
        print("You have been overcome by hairy monsters!")
        return True
    elif gShields == 0:
        print("Uh oh! You're out of shields too...")
        return True
    else:
        print("You have " + str(gShields) + " shields left")
        return False


def main():
    welcomeMessage()
    while takeTurn() == False:
        pass
    print("Game Over")


main()

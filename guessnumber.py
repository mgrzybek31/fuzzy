import random


def generator():
    drawed = random.choice(range(1, 11))
    return drawed


def game(gen, your=0):
    while your != gen:
        your = int(input("Enter the number: "))
        if your < gen:
            print("Your number is smaller!")
        elif your > gen:
            print("Your number is greater!")
    print("You did it!")


if __name__ == "__main__":
    game(generator())

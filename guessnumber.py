import random


def guess():
    x = random.choice(range(1, 10))
    y = 0
    while x != y:
        y = int(input("Guess the number: "))
        if y < x:
            print("Your number is less!")
        elif y > x:
            print("Your number is greater!")
    print("You did it!")


if __name__ == "__main__":
    guess()
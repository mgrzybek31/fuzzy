import random


def generator(sentence=input("Enter the sentence: ")):
    sentence = sentence.split()
    length = len(sentence)
    ans = ""
    for i in range(length):
        draw = random.choice(range(0, length))
        ans += sentence[draw] + " "
        sentence.remove(sentence[draw])
        length -= 1
    print(ans)


if __name__ == "__main__":
    generator()

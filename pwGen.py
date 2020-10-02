#Python password generator

import string
import random


letters = string.ascii_letters
numbers = string.digits
punc = string.punctuation


print("welcome")
use = str(input("service the password belongs to: "))


def saveFile(word):
    print("saving...")
    data = open("password.txt", "a")
    data.write(use + ": ")
    data.write(word + "\n")
    data.close()
    print("done")


def passwordGen():
    x = f"{letters}{numbers}{punc}"
    x = list(x)
    random.shuffle(x)

    #generate random pw and convert to string
    randomPassword = random.choices(x, k=16)
    randomPassword = "".join(randomPassword)
    print(randomPassword)
    saveFile(randomPassword)

passwordGen()

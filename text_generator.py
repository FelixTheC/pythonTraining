#! /usr/env/python3

import string
import random

allLetters = [i for i in string.ascii_lowercase]
vovels = ['a','e','i','o','u']
nonVovels = list(set(allLetters)-set(vovels))

choices = []
endInput = True

while endInput:
    print("For quit please type in: 'q' ")
    choice = input("Do you want to have a vovel: 'v' a nonvovel: 'n' or a random letter: 'l' and 'w' for whitespace ")
    if choice == 'q':
        break
    else:
        choices.append(choice)


def generator(list):
    text = ''
    for i in choices:
        if i == 'v':
            text = text + random.choice(vovels)
        elif i == 'n':
            text = text + random.choice(nonVovels)
        elif i == 'l':
            text = text + random.choice(allLetters)
        elif i == 'w':
            text = text + ' '
        else:
            text = text + i
    return text


print(generator(choices))

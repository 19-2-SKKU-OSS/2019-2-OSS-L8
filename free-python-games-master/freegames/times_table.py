"""Time table game, answer the correct result of times table.
Exercises:
1. Increase the range of x, y.
2. Make a score board.
3. Make time limitation to answer.
"""

from time import *
from random import *

print("Tell me the answer!\n")

while true:
    x = randrange(1, 20)
    y = randrange(1, 20)
    correct = x * y
    print(x + "X" + y + " = ")
    user_input = input()
    if str(type(user_input)) != "<class 'int'>":
        print("Wrong input!\n")
        continue
    if correct == user_input :
        print("Correct!")
    else
        print("Wrong answer! The answer is " + correct)

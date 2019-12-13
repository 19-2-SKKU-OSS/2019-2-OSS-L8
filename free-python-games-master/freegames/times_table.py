"""Time table game, answer the correct result of times table.
Exercises:
1. Increase the range of x, y.
2. Make a score board.
3. Make time limitation to answer.
4. Implement 'Stage Clear'
"""

from time import *
from random import *

life = 5

print("Tell me the answer!\n")

# Game starts
while true:
    # Get two numbers
    x = randrange(1, 20)
    y = randrange(1, 20)
    correct = x * y #answer

    if life == 0:
        print("Loss!")
        break

    # answer the question
    print(x + "X" + y + " = ")
    user_input = input()

    # check input type
    if str(type(user_input)) != "<class 'int'>":
        print("Wrong input!\n")
        continue
    # check the answer
    if correct == user_input :
        print("Correct!")
    else
        global life--
        print("Wrong answer! The answer is " + correct)

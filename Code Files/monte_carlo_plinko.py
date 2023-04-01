# This program gets user input, runs a Monte Carlo simulation for plinko using random walk, and displays a bar plot of the results if the user selects 7 pockets

import random
import matplotlib.pyplot as plt
import numpy as np

# User input 
n = input("Enter how many pucks you want to drop:") # 10000 recommended
n = int(n)

r = input("Enter how many rows of peg you want (there are 12 rows in the physics simulation):") #12 recommended
r = int(r)

c = input("Enter how many pockets you want (there are 7 pockets in the physics simulation and \nA histogram will only be generated if you select 7):") # 7 recommended
c = int(c)

c2 = c-1

p = input("Enter which pocket you want to drop the puck above (value must be between 0 and " + str(c2) + "):") # 3 recommended
p = int(p)

# This makes sure the value entered is acceptable 
while p < 0 or p > c2:
    print("The value you entered was not between 0 and " + str(c2) + " please try again.") # 3 recommended
    p = input(
        "Enter which pocket you want to drop the puck above (value must be between 0 and " + str(c2) + "):")
    p = int(p)

board = [0] * c

# This part does the Monte Carlo simulation for plinko using random walk
for i in range(n):
    position = p
    for i in range(r):
        step = random.choice([-1, 1])
        position += step

        if position == -1:
            position = 0

        if position == c:
            position = c-1

    board[position] += 1

print(board)

if c == 7:
    # creating the dataset
    data = {'0': board[0], '1': board[1], '2': board[2],
            '3': board[3], '4': board[4], '5': board[5],
            '6': board[6]}
    numbers = list(data.keys())
    values = list(data.values())

    fig = plt.figure(figsize=(10, 5))

    # creating the bar plot
    plt.bar(numbers, values, color='maroon',
            width=0.4)

    plt.xlabel("Plinko pockets 0-6")
    plt.ylabel("No. of pucks in each pocket")
    plt.title("Number of pucks in each of the 7 pockets")
    plt.show()

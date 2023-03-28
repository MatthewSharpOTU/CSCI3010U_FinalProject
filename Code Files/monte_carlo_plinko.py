import random
import matplotlib.pyplot as plt
import numpy as np

n = input("Enter how many pucks you want to drop:")  # 10000
n = int(n)

r = input("Enter how many rows of peg you want (there are 12 rows in the physics simulation):")  #12
r = int(r)

c = input("Enter how many pockets you want (there are 7 pockets in the physics simulation and \nA histogram will only be generated if you select 7):")  # 7
c = int(c)

c2 = c-1

p = input("Enter which pocket you want to drop the puck above (value must be between 0 and " + str(c2) + "):")  # 3
p = int(p)

while p < 0 or p > c2:
    print("The value you entered was not between 0 and " + str(c2) + " please try again.")
    p = input("Enter which pocket you want to drop the puck above (value must be between 0 and " + str(c2) + "):")  # 3
    p = int(p)


board = [0] * c

for i in range(n):
    for i in range(r):
        step = random.choice([-1, 1])
        #print(step)
        p += step

        if p == -1:
            p = 0

        if p == c:
            p = c-1


    board[p]+=1

print(board)

if c == 7:
    # creating the dataset
    data = {'1': board[0], '2': board[1], '3': board[2],
            '4': board[3], '5': board[4], '6': board[5],
            '7': board[6]}
    numbers = list(data.keys())
    values = list(data.values())

    fig = plt.figure(figsize=(10, 5))

    # creating the bar plot
    plt.bar(numbers, values, color='maroon',
            width=0.4)

    plt.xlabel("Numbers 1-7")
    plt.ylabel("No. of occurrences from a sample of 100 numbers")
    plt.title("Number of times numbers 1-10 occur with uneven distribution")
    plt.show()





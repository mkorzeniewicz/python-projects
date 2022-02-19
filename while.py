import random

a = random.randint(0,8)
print(a)

countStars = 0

while a > countStars:
    print("*", end=" ")
    countStars = countStars + 1



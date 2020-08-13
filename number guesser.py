import random
x = random.randint(1, 100)


print("Welcome to Guess A Random Number")


var1 = x
n = int(input("Your Guess:"))
while True:
    if n > var1:
        print("Your guess is greater than the random number")
        if (n - var1) <= 10:
            print("You're close")
            n = int(input("Your guess: "))
        else:
            n = int(input("Your guess: "))
    elif n < var1:
        print("Your guess is lower than the random number")
        if (var1 - n) <= 10:
            print("You're close")
            n = int(input("Your guess: "))
        else:
            n = int(input("Your guess: "))
    elif n == var1:
        print(f"You guessed the number! It was {x}")
        break
    else:
        pass
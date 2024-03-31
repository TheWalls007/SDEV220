# 4.1

secret = 4
guess = int(input("Enter a number between 1 and 10: "))

while guess != secret:
    if guess > secret:
        print("Too high")
    elif guess < secret:
        print("Too low")
    guess = int(input("Enter a number between 1 and 10: "))

print("Correct")

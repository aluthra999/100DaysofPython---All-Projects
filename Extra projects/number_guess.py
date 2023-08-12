import random

EASY_LEVEL = 10
HARD_LEVEL = 5

computer_pick = random.randint(1, 100)
print(computer_pick)

# level = input("Pick a level '(e)asy' or '(h)ard': ").lower()
# if level == "e" or level == "easy":
#     print("You choose Easy level, You got 10 turns to guess the number.")
# else:
#     print("You choose Hard level, You got 5 turns to guess the number.")

def game():
    turns_remaining = True

    while turns_remaining:
        user_guess = int(input("Enter a number between 1 - 100: "))

        if user_guess > computer_pick:
            return "Too high"
            EASY_LEVEL -= 1
            HARD_LEVEL -= 1
            game()
        elif user_guess < computer_pick:
            return "Too low"
            EASY_LEVEL -= 1
            HARD_LEVEL -= 1
            game()
        elif user_guess == computer_pick:
            print("Gotcha! You Win")
            turns_remaining = False

        if EASY_LEVEL == 0 or HARD_LEVEL == 0:
            turns_remaining = False


game()
        
        

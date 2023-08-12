import random

user_wins = 0
computer_wins = 0
same_pick = 0

options = ["rock", "paper", "scissor"]

while True:
    user_input = input("select your option or 'q' to quit: ").lower()
    if user_input == 'q':
        break

    if user_input not in options:
        continue

    random_number = random.randint(0,2)
    # rock:0 , paper:1 , scissor:2
    computer_pick = options[random_number]
    print(computer_pick)

    if user_input == 'rock' and computer_pick == 'scissor':
        print("You won!")
        user_wins += 1

    elif user_input == 'paper' and computer_pick == 'rock':
        print("You won!")
        user_wins += 1
        
    elif user_input == 'scissor' and computer_pick == 'paper':
        print("You won!")
        user_wins += 1

    elif user_input == computer_pick:
        print("same pick")
        same_pick += 1

    else:
        print('computer win')
        computer_wins += 1

print("You won", user_wins, "times!")
print("Computer won", computer_wins, "times!")
print("Same picks", same_pick, "times!")
print("Good Bye!")

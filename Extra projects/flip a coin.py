import random

options = ['HEADS', 'TAILS']

random_number = random.randint(0, 1)
computer_pick = options[random_number]
print(computer_pick)


user_input = input('Pick your option or "e" to Exit: ').upper()

    
if user_input == computer_pick:
    print("You Win")
    
else:
    print("You lose")
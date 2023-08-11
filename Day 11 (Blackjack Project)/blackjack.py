#from art import logo
#print(logo)
#welcome = """
#Welcome to the Game of BLACKJACK, let Start the game and have some funnnnn!!! Cheers.\n"""
#print(welcome)

import random

def deal_card():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card

user_cards = []
computer_cards = []

for _ in range(2):
  user_cards.append(deal_card())
  computer_cards.append(deal_card())

def calculate_score():
  user_score = sum(user_cards)
  computer_score = sum(computer_cards)

  print(f"Your Cards {user_cards} Current score {user_score}")
  print(f"Your Cards {computer_cards} Current score {computer_score}")

    if (11 in computer_cards) and (10 in computer_cards):
      print("Dealer wins, You lost")
    elif (11 in user_cards) and (10 in user_cards):
      print("BLACKJACK, You Win")
    else:
      print("Keep playing")

calculate_score()
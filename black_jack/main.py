############### Blackjack Project #####################

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################
from art import logo
from replit import clear
import random
#function to draw a random card
def deal_card():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card=random.choice(cards)
  return card
  # function to compare the scores
def compare(user_score, computer_score):
  
  if user_score > 21 and computer_score > 21:
    return "You went over. You lose 😤"
    
  if user_score == computer_score:
    return "Draw 🙃"
  elif computer_score == 0:
    return "Lose, opponent has Blackjack 😱"
  elif user_score == 0:
    return "Win with a Blackjack 😎"
  elif user_score > 21:
    return "You went over. You lose 😭"
  elif computer_score > 21:
    return "Opponent went over. You win 😁"
  elif user_score > computer_score:
    return "You win 😃"
  else:
    return "You lose 😤"

# function to calculate the score
def calculate_score(cards):
  if 11 in cards and sum(cards)==21 and len(cards)==2:
    return 0
  if 11 in cards and sum(cards)>21:
    cards.remove(11)
    cards.append(1)
    
  return sum(cards)

def play_game():
  print(logo)
  is_game_over=False
  user_cards = []
  computer_cards = []
  for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())
  while not is_game_over:
    user_score=calculate_score(user_cards)
    computer_score=calculate_score(computer_cards)
    print(f"   Your cards: {user_cards}, current score: {user_score}")
    print(f"   Computer's first card: {computer_cards[0]}")
    if computer_score==0 or user_score==0 or user_score>21:
      is_game_over=True
    else:
      should_continue=input("do you wanna continue the game by drawing an another card if yes type 'y' or 'n' for end the game\n")
      if should_continue=='y':
        user_cards.append(deal_card())
      else:
        is_game_over=True
  
  while computer_score!=0 and computer_score<17:
    computer_cards.append(deal_card())
    computer_score= calculate_score(computer_cards)
  
  print(f"   Your final hand: {user_cards}, final score: {user_score}")
  print(f"   Computer's final hand: {computer_cards}, final score: {computer_score}")
  print(compare(user_score,computer_score))


while input("do you wanna play Black Jack game type 'y' for YES and 'n' for NO\n")=='y':
  clear()
  play_game()
  



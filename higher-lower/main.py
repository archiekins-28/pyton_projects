import game_data
import random
import art
from replit import clear

def random_element(data):
  random_data=random.choice(data)
  return random_data

data=game_data.data
is_continue=True
#print logo
# print(art.logo)
score=0
print(art.logo)
against=random_element(data)
# printing the compare and against elements
while is_continue:
 
  compare=against
  against=random_element(data)
  print(f"Compare A: {compare['name']}, a {compare['description']}, from {compare['country']}.")
  follower_a=compare['follower_count']
  # print(follower_a)



  print(art.vs)
  
  against=random_element(data)
  print(f"Against B: {against['name']}, a {against['description']}, from {against['country']}.")
  follower_b=against['follower_count']
  # print(follower_b)
  
  #getting user input
  
  choice=input("Who has more followers? Type 'A' or 'B':").lower()
  
  if choice=='a':
    choose=follower_a
    other=follower_b
  else:
    choose=follower_b
    other=follower_a
  
  # comparing the choose with other
  clear()
  if choose>other:
    score+=1
    print(f"You're right! Current score: {score}.")
    
  else:
    print(f"Sorry, that's wrong. Final score: {score}")
    is_continue=False




  

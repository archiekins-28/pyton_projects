#Step 1 
import random
import hangman_art
import hangman_words
word_list = hangman_words.word_list

#choosing the random word from the LIST
chosen_word=random.choice(word_list)

# generate the blanks equivalent to the choosing word
print(hangman_art.logo)
print(chosen_word)
display=[]
for i in range(len(chosen_word)):
  display+="_"
# print(display)
# for running the while loop
end_of_game= False

lives=6
while not end_of_game:
#getting the i/p from the user.
  guess=input("Guess the letter ").lower()
#let the user knows if they already they guessed this letter 
  if guess in display:
    print("you already guessed this letter")
# inserting into display if they guessed the correct word
  for i in range (len(chosen_word)):
    if chosen_word[i]==guess :
      display[i]=guess
  if guess not in chosen_word:
    print(f" {guess} is not present in the word")
    lives-=1
  
# stopping the while loop if they guessed all letters
  print(display)
  if "_" not in display:
    print("You win!")
    end_of_game= True
  else:
    end_of_game= False
  if lives==0:
    print("You loose!")
    end_of_game= True
  # print(lives)
  print(hangman_art.stages[lives])
    
  


import random
words=["weather","electricity","towers","camaouflage","python","juvenile","programming","hardware","reverse", "water", "board", "numerical"]
word_chosen=random.choice(words)

# chance available showing the number of chances left for the user to guess the whole word.
chances_available=7

# creating a list to store the letter provided by the user if they are in choosen word.

guess_word = ["_"]*len(word_chosen)
gameOver=False

# giving the information of the length of the word chosen to user.
print(len(word_chosen))


while gameOver is False:
  guess_letter=input("Guess a letter   ").lower()
  
  # going in the loop and checking each letter of the chosen word with the guessed letter .
  # If matched then placing the guessed letter at the right index.
  
  for letter_position in range(len(word_chosen)):
    if guess_letter==word_chosen[letter_position]:
      guess_word[letter_position]=guess_letter
      print(guess_word)
      
  # if the guessed letter by the user is incorrect then we will reduct the chances_availaible which means the user has now 1 less chance to guess. 
  
  if guess_letter not in word_chosen:
      chances_available=chances_available-1
      print("chances left " , chances_available)
    
    # checking if the user has used all of the chances or not before guessing the word.If yes then the user failed to guess the word.
    
      if chances_available ==0:
          print('you lose !! You ran out of chances')
          gameOver=True
        
  # checking if any blank space is left in list or not.If no then the user has guessed all the words in the given chances.
  
  if '_' not in guess_word:
          print("you guessed the word")
          break

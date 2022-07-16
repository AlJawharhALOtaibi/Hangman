import random 

logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''

                          
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

display = []
from hangman_words import words_list
chosen = random.choice(words_list)
no_lives = 6

print(logo)

#1: to print an empty list accourding to the chosen word
for n in chosen :
  display += "_"
print(display)
  
#2: testing the user input
#3: reveal user input into the list 
#e.g. apple and user enter p then, [_,p ,p ,_ ,_]

end_game = False 
while not end_game :
  guess = input("Guess a letter: ").lower()
  if guess in display :
      print(f"You've already guessed! {guess}")
      #Check guessed letter
  for n in range(len(chosen)):
      letter = chosen[n]
      if letter == guess:
          display[n] = letter
  #Check if user is wrong.
  if guess not in chosen:
      print(f"You guessed {guess}, that's not in the word. You lose a life.")
      no_lives -= 1
      if no_lives == 0:
          end_game = True
          print("You lose.")

  #Join all the elements in the list and turn it into a String.
  print(f"{' '.join(display)}")

  #Check if user has got all letters.
  if "_" not in display:
      end_game = True
      print("You win.")

  #print stages 
  print(stages[no_lives])